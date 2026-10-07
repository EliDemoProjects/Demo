# DAST CLI Kubernetes Job Configuration

## Overview

This page explains how to configure a Kubernetes job to run DAST scans. The configuration depends on whether your target application requires a tunnel.

### When to Use a Tunnel

| Scenario | Tunnel Required | Configuration |
| --- | --- | --- |
| Scanning public applications (accessible from the internet) | No | Use only the `dast-cli` container |
| Scanning private/internal applications (not accessible from the internet) | Yes | Use both `tunnel` and `dast-cli` containers with `--sidecar-mode=true` |

### Configuration Without Tunnel

Use this configuration when scanning public applications accessible from the internet.

Required components:

- `dast-cli` container only

#### Example - Without Tunnel

```
apiVersion: batch/v1
kind: Job
metadata:
  name: dast-cli-job
spec:
  backoffLimit: 3
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: dast-cli
          image: checkmarx/dast:<version>
          imagePullPolicy: IfNotPresent
          securityContext:
            runAsUser: 1000
            runAsGroup: 1000
          env:
            - name: CX_APIKEY
              value: "YOUR_API_KEY"
          args:
            - "scan"
            - "--base-url=https://your-checkmarx-instance.com/"
            - "--is-cloud-scan=true"
            - "--env-setup={...}"
```

### Configuration With Tunnel

Use this configuration when scanning private/internal applications that require a tunnel.

Required components:

- `tunnel` container
- `dast-cli` container with `--sidecar-mode=true`
- Shared volume for inter-container communication

#### Example - With Tunnel

```
apiVersion: batch/v1
kind: Job
metadata:
  name: dast-cli-job
spec:
  backoffLimit: 3
  template:
    spec:
      restartPolicy: Never
      containers:
        # Tunnel container - required for private/internal apps
        - name: tunnel
          image: checkmarx/link-client:2
          securityContext:
            runAsUser: 1000
            runAsGroup: 1000
          imagePullPolicy: IfNotPresent
          env:
            - name: HOME
              value: /tmp
          command: ["/bin/sh", "-c"]
          args:
            - |
              echo "Waiting for tunnel configuration..."
              
              # Wait for CLI to write config (max 1000 seconds)
              TIMEOUT=1000
              ELAPSED=0
              while [ ! -f /tunnel-config/ready ]; do
                if [ $ELAPSED -ge $TIMEOUT ]; then
                  echo "ERROR: Timeout waiting for tunnel configuration"
                  exit 1
                fi
                sleep 2
                ELAPSED=$((ELAPSED + 2))
              done
              
              echo "Tunnel configuration found, starting tunnel..."
              
              # Export config as environment variables (entrypoint reads these)
              export TUNNEL_NAME=$(grep TUNNEL_NAME /tunnel-config/env | cut -d'=' -f2)
              export TUNNEL_SERVER_URL=$(grep ZROK_HOST /tunnel-config/env | cut -d'=' -f2)
              export LINK_TOKEN=$(grep TOKEN /tunnel-config/env | cut -d'=' -f2)
              export TUNNEL_TYPE=socks5
              
              # Start the tunnel entrypoint in the background
              bash /app/entrypoint.sh &
              
              TUNNEL_PID=$!
              echo "Tunnel started with PID: $TUNNEL_PID"
              
              # Maximum time to wait for shutdown signal (3 hours = 10800 seconds)
              MAX_WAIT=10800
              ELAPSED=0
              
              # Monitor for shutdown signal while tunnel is running
              while kill -0 $TUNNEL_PID 2>/dev/null; do
                if [ $ELAPSED -ge $MAX_WAIT ]; then
                  echo "ERROR: Timeout - no shutdown signal received after $MAX_WAIT seconds"
                  kill -TERM $TUNNEL_PID 2>/dev/null || true
                  sleep 20
                  kill -9 $TUNNEL_PID 2>/dev/null || true
                  exit 1
                fi
                
                # Check if dast-cli signaled scan completion
                if [ -f /tunnel-config/shutdown ]; then
                  echo "Shutdown signal received, stopping tunnel gracefully..."
                  kill -TERM $TUNNEL_PID 2>/dev/null || true
                  sleep 20
                  kill -9 $TUNNEL_PID 2>/dev/null || true
                  exit 0
                fi
                
                sleep 60
                ELAPSED=$((ELAPSED + 60))
              done
              
              echo "Tunnel process exited unexpectedly"
              exit 1
          volumeMounts:
            - name: tunnel-config
              mountPath: /tunnel-config

        # DAST CLI container
        - name: dast-cli
          image: checkmarx/dast:<version>
          imagePullPolicy: IfNotPresent
          securityContext:
            runAsUser: 1000
            runAsGroup: 1000
          env:
            - name: CX_APIKEY
              value: "YOUR_API_KEY"
          args:
            - "scan"
            - "--base-url=https://your-checkmarx-instance.com/"
            - "--sidecar-mode=true"
            - "--is-cloud-scan=true"
            - "--one-time-tunnel=true"
            - "--env-setup={...}"
          volumeMounts:
            - name: tunnel-config
              mountPath: /tunnel-config

      # Shared volume for tunnel configuration
      volumes:
        - name: tunnel-config
          emptyDir: {}
```

### Tunnel Container

Use this container only when scanning private/internal applications

Creates a secure tunnel to allow DAST to scan private/internal applications.

| Property | Description |
| --- | --- |
| `image` | `checkmarx/link-client:2` |
| `securityContext` | Runs as non-root user (1000:1000) |
| `env.HOME` | Set to `/tmp` - required for writable directory |

#### Communication Flow

The tunnel container coordinates with the dast-cli container through a shared volume:

1. `dast-cli` writes tunnel config to `/tunnel-config/env`
2. `dast-cli` creates `/tunnel-config/ready` to signal the tunnel to start
3. Tunnel reads config and establishes connection
4. `dast-cli` performs a scan through the tunnel
5. `dast-cli` creates `/tunnel-config/shutdown` when scan completes
6. Tunnel terminates

### Shared Volume (Only When Tunnel is Needed)

Include the following when using the tunnel container

An `emptyDir` volume named `tunnel-config` is used for communication between the two containers.

Purpose:

- Enables configuration exchange between `dast-cli` and `tunnel` containers
- `dast-cli` writes tunnel configuration here
- `tunnel` container reads configuration from here
- Used for signaling (ready file, shutdown file)

Both containers must mount this volume at `/tunnel-config`.

### Quick Reference

| Component | Without Tunnel | With Tunnel |
| --- | --- | --- |
| `dast-cli` container | Required | Required |
| `tunnel` container | Not needed | Required |
| `tunnel-config` volume | Not needed | Required |
| `--sidecar-mode=true` | Not needed | Required |
| `--one-time-tunnel=true` | Not needed | Required |
