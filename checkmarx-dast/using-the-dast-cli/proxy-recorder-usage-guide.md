# Proxy Recorder Usage Guide

The Proxy Recorder captures HTTP traffic flowing through the Checkmarx DAST ZAP proxy and exports it as a ZST file. This creates the server-side recording which is uploaded to the Checkmarx platform for use in DAST scans. After it's created in the CLI, it will be viewable in the Checkmarx One platform. You cannot create a server-side recorder file in the UI and it cannot be dragged into flows in the UI (see [here](../business-flow-recorder/business-flow-recorder.md) for more information on flows).

## Prerequisites

* Docker installed and access to the `checkmarx/dast:latest` image
* A Checkmarx API key (`CX_APIKEY`)
* The environment ID you want to associate the recording with
* Your Checkmarx platform base URL

Perform the following to run the Proxy Recorder:

> `<container-name-or-id>` is either the container name (e.g. `proxy-recorder` if you used `--name proxy-recorder`) or the container ID from `docker ps`.

1.  Start the Proxy Recorder:

    ```bash
    docker run -it \
      --pull=always \
      --name proxy-recorder \
      -p 8090:8090 \
      -p 8092:8092 \
      -v /tmp/pr-output:/tmp/dast-output \
      -e CX_APIKEY=<your-api-key> \
      checkmarx/dast:latest \
      proxy-recorder \
      --url=https://your-target-app.com \
      --output=/tmp/dast-output \
      --proxy-recorder-port=8092 \
      --duration=60 \
      --dump-cert=true \
      --upload=true \
      --environment-id=<your-environment-id> \
      --base-url=<your-checkmarx-base-url>
    ```

    > **Note:** `-it` runs the container in the foreground with an interactive terminal so you can see live logs. Use `-d` instead if you prefer to run it in the background (detached). `--pull=always` ensures you always use the latest image.

    | Flag                    | Required                 | Description                                                                                                                                                                  |
    | ----------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `--url`                 | Yes                      | URL of the application to record traffic against                                                                                                                             |
    | `--base-url`            | Yes                      | Your Checkmarx platform URL (e.g. `https://us.ast.checkmarx.net`)                                                                                                            |
    | `--environment-id`      | Yes (if `--upload=true`) | Environment ID to associate the recording with                                                                                                                               |
    | `--proxy-recorder-port` | No (default: `8092`)     | Port for the proxy recorder control API                                                                                                                                      |
    | `--duration`            | No (default: `1440` min) | Maximum recording duration in minutes before auto-stop                                                                                                                       |
    | `--output-file`         | No                       | Label for the output file (e.g. `session1` → `proxy-recorder_session1.zst`). Must be unique — uploading with the same label will override the previously uploaded recording. |
    | `--upload`              | No (default: `true`)     | Upload the HAR recording to the Checkmarx platform when done                                                                                                                 |
    | `--dump-cert`           | No (default: `false`)    | Export the ZAP root CA certificate (required to trust the proxy in your browser/client)                                                                                      |
2.  Wait Until the Proxy is Ready: Before routing traffic, confirm ZAP has finished initializing.

    **Option A — curl**

    ```bash
    curl -s -o /dev/null -w "%{http_code}" http://localhost:8092/ready
    # 200 = ready, 503 = still starting
    ```

    **Option B — docker exec**

    ```bash
    docker exec <container-name-or-id> /app/bin proxy-recorder ready --proxy-recorder-port=8092 --base-url=<your-checkmarx-base-url>
    # Exit code 0 = ready, exit code 1 = not ready yet
    ```
3.  Trust the ZAP Certificate (if using --dump-cert): For the proxy to intercept HTTPS traffic your browser or client must trust the ZAP root CA certificate.

    **Option A — curl**

    ```bash
    curl http://localhost:8092/cert -o zap-root-ca.crt
    ```

    **Option B — docker exec**

    ```bash
    docker exec <container-name-or-id> /app/bin proxy-recorder cert --proxy-recorder-port=8092 --base-url=<your-checkmarx-base-url> > zap-root-ca.crt
    ```

    Then install `zap-root-ca.crt` as a trusted CA in your browser or HTTP client.
4.  Record Traffic: Route your HTTP traffic through the ZAP proxy on port `8090` from inside the container using `docker exec`:

    ```bash
    docker exec -it <container-name-or-id> curl -k -x http://localhost:8090 https://your-target-app.com/some-path
    ```

    Repeat this for every request you want to record. ZAP captures all traffic passing through it.
5.  Stop the Recording: When you have finished recording, send the stop signal.

    **Option A — curl**

    ```bash
    curl -X POST http://localhost:8092/stop
    ```

    **Option B — docker exec**

    ```bash
    docker exec <container-name-or-id> /app/bin proxy-recorder stop --proxy-recorder-port=8092 --base-url=<your-checkmarx-base-url>
    ```

    The recorder will finalize the HAR export and, if `--upload=true`, upload it to Checkmarx One automatically.

## Example and Tips

```bash
# 1. Start
docker run -it \
  --pull=always \
  --name proxy-recorder \
  -p 8090:8090 \
  -p 8092:8092 \
  -v /tmp/pr-output:/tmp/dast-output \
  -e CX_APIKEY=<your-api-key> \
  checkmarx/dast:latest \
  proxy-recorder \
  --url=<your-target-app> \
  --output=/tmp/dast-output \
  --proxy-recorder-port=8092 \
  --duration=60 \
  --dump-cert=true \
  --upload=true \
  --environment-id=<your-environment-id> \
  --base-url=<your-checkmarx-base-url>

# 2. Wait for ready
curl -s -o /dev/null -w "%{http_code}" http://localhost:8092/ready

# 3. Get the certificate
curl http://localhost:8092/cert -o zap-root-ca.crt

# 4. Browse your app with the proxy configured...

# 5. Stop
curl -X POST http://localhost:8092/stop
```

* The `CX_APIKEY` environment variable is required for authentication. It is the API key generated from Checkmarx.
* The output ZST file is saved inside the container under `/tmp/dast-output/dast-output-<random>/`. With the volume mount shown above it will appear on the host at `/tmp/pr-output/dast-output-<random>/proxy-recorder.zst`. The `--output=/tmp/dast-output` flag is required to ensure the file lands inside the mounted directory.
* Sending `SIGTERM` or `SIGINT` to the container (e.g. `docker stop`) will also trigger a clean stop.
