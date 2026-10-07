# Using the DAST CLI - Overview

## Overview

The DAST CLI (Dynamic Application Security Testing Command Line Interface) is a powerful tool for performing security scans on web applications and APIs. It supports multiple scanning modes and offers extensive configuration options to tailor scans to your specific needs. DAST CLI is supported on both Firefox and Chrome.

{% hint style="info" %}
Commands and flags are automatically maintained and updated with each CLI release. Pull the images from Docker Hub for the most current versions. Use `dast --help` or `dast [command] --help` for more details in the CLI.
{% endhint %}

## Installation and Setup

### Prerequisites

* Access to CxOne platform
* Valid authentication credentials

## Commands Overview

The DAST CLI supports the following main commands:

* `scan` - Run a scan based on the environment configuration
* `web` - Perform web application scan
* `api` - Perform API security scan
* `setup` - Set up authentication sessions
* `version` - Display version information
* `manual-results` - Upload manual results

## OAuth CLI Authentication

Instead of API Keys, use the environment variables to authenticate your login. For more information, see OAuth Client, [here](../../document/preview/116020/#UUID-46756010-b96c-6e75-e101-56f7127fb532). The following is an example where the first code bloc uses the API Key and the second uses Environment Variables.

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest api \  
--base-url=https://ast.checkmarx.net \  
--environment-id=12345678-abcd-1234-5678-123456789012 \  
--postman=./collection.json \  
--log-level=debug

docker run -e CX_CLIENT_ID=[eyJK...] -e CX_CLIENT_SECRET=[AbCd...] \  
checkmarx/dast:latest api \  
--base-auth-uri=https://iam-dev.dev.cxast.net \  
--tenant=852dd-sddd... \  
--base-url=https://ast.checkmarx.net \  
--environment-id=12345678-abcd-1234-5678-123456789012 \  
--postman=./collection.json \  
--log-level=debug
```

## Environment Variables

The CLI supports the following environment variables:

| Variable                      | Description                                               |
| ----------------------------- | --------------------------------------------------------- |
| `CX_APIKEY`                   | API key for authentication                                |
| `CX_TIMEOUT`                  | Client timeout value                                      |
| `CX_AGENT_NAME`               | Custom agent name                                         |
| `HTTP_PROXY`                  | HTTP proxy URL                                            |
| `DAST_CONSTANT_OUTPUT_FOLDER` | Use constant output folder                                |
| `CX_CLIENT_ID`                | The client ID that is used for client authentication.     |
| `CX_CLIENT_SECRET`            | The client secret that is used for client authentication. |

### Exit Codes

The CLI uses the following exit codes:

* `0` - Success
* `2` - Error (configuration, scan failure, etc.)

### Debug Mode

Enable verbose logging for detailed troubleshooting:

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest [command] --verbose --log-level debug [other-flags]
```

<details>

<summary>Examples by Use Case</summary>

#### Web Scan

```
docker run \-e CX_APIKEY={API_KEY} \
-v /downloads/directory:/dast_test \
checkmarx/dast:latest web \
--config=/dast_test/fast_scan_sample.yaml \
--base-url=<base URL>\
--output=/dast_test \
--jvm-properties=-Xmx3G \
--timeout=86400 \
--verbose \
--environment-id=ce17623b-0545-4f04-a8b1-f39c689e9ccd
```

#### API Testing with Multiple Formats

{% hint style="info" %}
In the below example, .har file are interchangeable with Postman and OpenAPI files.
{% endhint %}

```
docker run \-e CX_APIKEY={API_KEY} \
-v ${PWD}:/dast_test \
checkmarx/dast:latest api \
--config=/dast_test/configHarTest.yaml \
--har=/dast_test/harFile.har \
--base-url={CX_ONE_URL} \
--output=/dast_test \
--jvm-properties=-Xmx3G \
--timeout=86400 \
--verbose \
--environment-id=10790c6f-a16e-4018-95e9-790aae837141
```

</details>

## Global Flags

### Required Flags

These are flags that you must use for all commands. `--environment-id` flag is used for all commands except for the scan command. `-v` flag is used in any command where you need to specify a file path, for example, for configuration files, API files, or Recorder files.

| Flag               | Description                                                                                                                                            | Example                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| `--base-url`       | CxOne server base URL                                                                                                                                  | `<https://ast.checkmarx.net`>          |
| `--environment-id` | Environment ID from CxOne platform                                                                                                                     | `12345678-abcd-1234-5678-123456789012` |
| `-v`               | <p>Mounts the directory filepath<br><strong>Warning</strong> Without read and write permissions to the mounted directory, DAST CLI scan will fail.</p> | `-v ${PWD}:/dast_test`                 |

### Common Optional Flags

| Flag                          | Default    | Description                                                                                                                               |
| ----------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `--config`                    | `""`       | Path to configuration file                                                                                                                |
| `--output`                    | `""`       | Path to output directory                                                                                                                  |
| `--timeout`                   | `10000`    | Timeout in seconds                                                                                                                        |
| `--log-level`                 | `"info"`   | Log level (debug, info, warn, error)                                                                                                      |
| `--verbose`                   | `false`    | Print logs to stdout                                                                                                                      |
| `--fail-on`                   | `""`       | Lowest severity to fail execution (all, low, info, medium, high), evaluated per instance or per alert based on the tenant's display mode. |
| `--update-interval`           | `30`       | Update interval in seconds                                                                                                                |
| `--jvm-properties`            | `"-Xmx3G"` | JVM properties for heap-stack size                                                                                                        |
| `--zap-port`                  | 8090       | zap proxy port to use                                                                                                                     |
| `--preferred-credential-type` | API Key    | Preferred credential type: API Key or OAuth                                                                                               |

### Authentication & Retry Flags

| Flag            | Default | Description                                    |
| --------------- | ------- | ---------------------------------------------- |
| `--retry`       | `3`     | Number of retry attempts on connection failure |
| `--retry-delay` | `20`    | Time between retries in seconds                |

### Proxy Configuration

| Flag           | Default | Description                              |
| -------------- | ------- | ---------------------------------------- |
| `--proxy-host` | `""`    | Proxy host address                       |
| `--proxy-port` | `""`    | Proxy port number                        |
| `--no-proxy`   | `""`    | Exclude URLs matching pattern from proxy |

### Polling Configuration

| Flag             | Default | Description                     |
| ---------------- | ------- | ------------------------------- |
| `--poll-timeout` | `600`   | Poll timeout in seconds         |
| `--poll-ticker`  | `30`    | Poll ticker interval in seconds |

## Commands

{% hint style="success" icon="key" %}
ALL commands require the API Key and --base-url to run the DAST CLI
{% endhint %}

### 1. Scan Command

{% hint style="info" %}
The scan command is the recommended and most actively maintained option.
{% endhint %}

Runs a scan based on the environment settings. Ensure you mount the directory that includes the web, API, recording, authentication, and custom config files you wish to scan. Remember to confirm the filepaths are consistent with the mounted directory. See [here](dast-installing-the-dast-cli-in-a-pipeline.md#UUID-f3317c6e-4143-b348-b66c-0c5f76be35e7_sidebar-idm4542511358548833814417613735) for more information on using Docker image in the CLI.

#### Usage

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest scan --base-url <url> --environment-id <id> [flags]
```

#### Specific Flags

| Flag                     | Default | Description                                                                                                                                                                                      |
| ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--url`                  | `""`    | URL of the application to scan                                                                                                                                                                   |
| `--is-cloud-scan`        | `false` | Run a scan using cloud services instead of locally                                                                                                                                               |
| `--custom-headers`       | `[]`    | Custom HTTP headers to include in each outgoing request, in the format: `[{"header":"header-name", "value":"header-value", "url":"url-regex"}]`                                                  |
| `--env-setup`            | `""`    | JSON configuration for environment setup before the scan is run                                                                                                                                  |
| `--tunnel-name`          | `""`    | Name of the tunnel to use to access a private host (will be created if it does not exist)                                                                                                        |
| `--tunnel-ready-timeout` | `120`   | Timeout in seconds to wait for the tunnel to become ready                                                                                                                                        |
| `--one-time-tunnel`      | `false` | If true, it will create a one-time tunnel for the scan. The tunnel will be deleted at the end.                                                                                                   |
| `--browser`              | `""`    | Choose either Firefox or Chrome to run the DAST CLI. Use either `firefox-headless` or `chrome-headless`. If using Chrome, add the `--shm-size=2g` in the Docker command (before the image name). |

\--env-setup JSON Structure includes the following fields:

| Field                   | Type      | Required    | Description                                                                                                                 |
| ----------------------- | --------- | ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| `EnvironmentID`         | string    | No          | Environment ID                                                                                                              |
| `name`                  | string    | Yes         | Name of the environment                                                                                                     |
| `url`                   | string    | Yes         | URL of the application to be scanned                                                                                        |
| `scanType`              | string    | Yes         | Type of scan: `web` or `api`                                                                                                |
| `isPublic`              | boolean   | No          | Whether the target is publicly accessible (default: `false`)                                                                |
| `groups`                | string\[] | No          | List of group names to associate with the environment                                                                       |
| `tags`                  | string\[] | No          | List of tags to associate with the environment                                                                              |
| `projectIds`            | string\[] | No          | List of project IDs to associate with the environment                                                                       |
| `hasAuth`               | boolean   | No          | Whether authentication is required (default: `false`)                                                                       |
| `authMethod`            | string    | Conditional | Authentication method: `recording`, `browser`, or `customConfig`. Required when `hasAuth` is `true` and `scanType` is `web` |
| `customConfigFile`      | string    | Conditional | Path to custom ZAP configuration file. Required when `authMethod` is `customConfig`                                         |
| `recordingFile`         | string    | Conditional | Path to the authentication recording file. Required when `authMethod` is `recording`                                        |
| `browserForm`           | object    | Conditional | Browser-based authentication form data. Required when `authMethod` is `browser`                                             |
| `totp`                  | object    | No          | TOTP (Time-based One-Time Password) configuration for 2FA                                                                   |
| `apiFiles`              | array     | Conditional | List of API definition files. Required when `scanType` is `api`                                                             |
| `proxyRecorderFiles`    | string\[] | No          | Path to Proxy Recorder files                                                                                                |
| `tunnel`                | string    | No          | Tunnel name for accessing private hosts                                                                                     |
| `clientIds`             | string\[] | No          | List of clients associated with the environment                                                                             |
| `userIds`               | string\[] | No          | List of users associated with the environment                                                                               |
| `settings`              | object    | No          | Environment Settings                                                                                                        |
| `includePaths`          | string\[] | No          | List of included paths in a scan                                                                                            |
| `applicationIds`        | string\[] | No          | List of Applications to associated with the environment                                                                     |
| `primaryApplicationIds` | string\[] | No          | List of Application IDs to set an environment as a primary environment (only one can be set as a primary environment).      |

#### Settings Object

| Field                                                                                                                                                                                                                                                                          | Type   | Required | Description                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | -------- | ---------------------------------------------------------------------- |
| `configFileSettings`                                                                                                                                                                                                                                                           | object | No       | Scanner configuration file overrides (e.g., exclude paths).            |
| `CLISettings`                                                                                                                                                                                                                                                                  | object | No       | CLI behavior overrides applied before the scan starts.                 |
| `authSettings`                                                                                                                                                                                                                                                                 | object | No       | Authentication verification settings used during the auth flow.        |
| `sessionManagement`                                                                                                                                                                                                                                                            | array  | No       | HTTP headers injected into every scan request to maintain the session. |
| <p><code>scanOptions</code><br><strong>Important</strong> For more information on scan options in DAST, refer to Scan Configurations <a href="../dast-environment-setup-wizard/environment-settings.md#UUID-438f45cc-772b-67e8-7eb5-7c1b0ad987ef_N1774971492572">here</a>.</p> | object | No       | Controls the scan depth/mode and server-level inclusion.               |
| `automationScripts`                                                                                                                                                                                                                                                            | array  | No       | Automation scripts loaded into the scanner during execution.           |

**Settings Options**

{% tabs %}
{% tab title="configFileSettings" %}
| Field          | Type      | Required | Description                            |
| -------------- | --------- | -------- | -------------------------------------- |
| `excludePaths` | string\[] | No       | List of paths to exclude from the scan |
{% endtab %}

{% tab title="CLISettings" %}
| Field            | Type   | Required | Description                                    |
| ---------------- | ------ | -------- | ---------------------------------------------- |
| `JVMProperties`  | string | No       | JVM properties for heap-stack size             |
| `LogLevel`       | string | No       | Debug, info, warn, or error                    |
| `Output`         | string | No       | Path to output directory                       |
| `RetryDelay`     | int    | No       | Time between retries in seconds                |
| `Retry`          | int    | No       | Number of retry attempts on connection failure |
| `UpdateInterval` | int    | No       | Update interval in seconds                     |
{% endtab %}

{% tab title="authSettings" %}
| Field                   | Type          | Required | Description                                                                             |
| ----------------------- | ------------- | -------- | --------------------------------------------------------------------------------------- |
| `verificationUrl`       | string        | No       | URL polled to check whether the session is authenticated.                               |
| `loggedInRegex`         | string        | No       | Regex matched against the verification response to confirm authentication.              |
| `loggedOutRegex`        | string        | No       | Regex matched against the verification response to confirm unauthentication.            |
| `loginPageWait`         | int           | No       | Milliseconds to wait after loading the login page before interacting with it.           |
| `pollAdditionalHeaders` | AuthHeader\[] | No       | Extra HTTP headers sent with each verification poll request.                            |
| `includePaths`          | string\[]     | No       | URL path prefixes the scanner is allowed to crawl and test.                             |
| `pollPostData`          | string        | No       | Request body sent with POST-based verification poll requests.                           |
| `totpField`             | TotpField     | No       | Identifies the TOTP input element (`attribute`, `value`) for MFA-protected login flows. |
{% endtab %}

{% tab title="sessionManagement (authHeader)" %}
| Field    | Type   | Required | Description               |
| -------- | ------ | -------- | ------------------------- |
| `Header` | string | Yes      | Name of the HTTP header.  |
| `Value`  | string | Yes      | Value of the HTTP header. |
{% endtab %}

{% tab title="scanOptions" %}
| Field           | Type   | Required | Description                                                                  |
| --------------- | ------ | -------- | ---------------------------------------------------------------------------- |
| `scanOption`    | string | No       | Scan depth preset: `fast`, `balanced`, `deep`, or `thorough`.                |
| `includeServer` | string | No       | Whether to include server-level endpoints in the scan.                       |
| `slowApp`       | string | No       | Enables slower request pacing for apps with rate limiting or slow responses. |
{% endtab %}

{% tab title="automationScripts" %}
| Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Type   | Required | Description                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ------------------------------------------------------------------------- |
| <p><code>type</code><br><strong>Caution</strong> You are able to add a Selenium or HTTP Sender authentication script to a selected environment during environment setup, or update it later in the settings. If one or more files are already saved for this environment, uploading a file through the CLI overrides all files that are currently stored there. Any change to any file requires reuploading the entire set of files for that flow.<br>If you want to upload only a single file and you do not have the other existing files, you must use the UI. The UI allows you to download the existing files or add an additional file without deleting the others</p> | string | Yes      | Script type: `httpsender`, `active`, `passive`, `variant`, or `selenium`. |
| `action`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | string | Yes      | Path to the .js or .txt script file on disk.                              |
{% endtab %}
{% endtabs %}

#### browserForm Object

Required if the out method is browser.

| Field      | Type   | Required | Description                 |
| ---------- | ------ | -------- | --------------------------- |
| `loginUrl` | string | Yes      | The URL of the login page   |
| `username` | string | Yes      | Username for authentication |
| `password` | string | Yes      | Password for authentication |

#### totp Object

| Field       | Type    | Required | Description                                           |
| ----------- | ------- | -------- | ----------------------------------------------------- |
| `secretKey` | string  | Yes      | The TOTP secret key                                   |
| `digits`    | integer | Yes      | Number of digits in the OTP (must be > 0)             |
| `period`    | integer | Yes      | Time period in seconds for OTP rotation (must be > 0) |

#### apiFiles Array Item

| Field  | Type   | Required | Description                                      |
| ------ | ------ | -------- | ------------------------------------------------ |
| `type` | string | Yes      | Type of API file: `openapi`, `postman`, or `har` |
| `file` | string | Yes      | Path to the API definition file                  |

**Examples**

Basic local scan:

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest scan \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --output ./scan-results \
  --verbose
```

Cloud scan:

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest scan \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --is-cloud-scan
```

Scan with custom headers:

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest scan \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --custom-header "Authorization:Bearer token123" \
  --custom-header "X-API-Key:myapikey" \
  --output ./results
```

#### Cloud scan with environment setup and tunneling:

```
docker run --user=root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e CX_APIKEY=<your-api-key> \
  dast-cli:local scan \
    --base-url=https://ast.checkmarx.net \
    --is-cloud-scan=true \
    --tunnel-name=my-tunnel \
    --env-setup='{"name":"my-environment","url":"https://internal-app.local","scanType":"web","isPublic":false,"hasAuth":false}'
```

#### Cloud scan with tunneling, authentication, and TOTP:

```
docker run --user=root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e CX_APIKEY=<your-api-key> \
  dast-cli:local scan \
    --base-url=https://ast.checkmarx.net \
    --is-cloud-scan=true \
    --tunnel-name=my-tunnel \
    --env-setup='{
      "name":"my-environment",
      "url":"https://internal-app.local",
      "scanType":"web",
      "isPublic":false,
      "hasAuth":true,
      "authMethod":"browser",
      "browserForm":{
        "loginUrl":"https://internal-app.local/login",
        "username":"user@example.com",
        "password":"secret123"
      }
    }'
```

#### Cloud scan with tunneling for API scan:

```
docker run --user=root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /path/to/api-specs:/specs \
  -e CX_APIKEY=<your-api-key> \
  dast-cli:local scan \
    --base-url=https://ast.checkmarx.net \
    --is-cloud-scan=true \
    --tunnel-name=my-tunnel \
    --env-setup='{
      "name":"my-api-environment",
      "url":"https://internal-api.local",
      "scanType":"api",
      "isPublic":false,
      "hasAuth":false,
      "apiFiles":[{"type":"openapi","file":"/specs/openapi.yaml"}]
    }'
```

{% hint style="info" %}
* `--user=root` and `-v /var/run/docker.sock:/var/run/docker.sock` are required for tunneling because the CLI spawns a tunnel container.
* The tunnel will be created automatically if it doesn't exist.
* Use `--tunnel-ready-timeout` to adjust the wait time for tunnel connection (default: 120 seconds).
{% endhint %}

### 2. Web Command

Performs web application security scanning. Specify the path to the configuration file using the --config flag. Ensure you mount the directory that includes the web and custom config files you wish to scan. Remember to confirm the filepaths are consistent with the mounted directory.

#### Usage

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest web --base-url <url> --environment-id <id> [flags]
```

#### Examples

Basic web scan:

```
dast web \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --config ./web-config.yml \
  --output ./web-results
```

Web scan with specific timeout and fail conditions:

```
dast web \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --timeout 7200 \
  --fail-on high \
  --verbose
```

### 3. API Command

Performs API security scanning using OpenAPI, Postman collections, or HAR files. Specify the file paths for each API and their configuration files, using the --config flag. Ensure you mount the directory that includes the API and custom config files you wish to scan. Remember to confirm the filepaths are consistent with the mounted directory.

#### Usage

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest api --base-url <url> --environment-id <id> [one of: --openapi | --postman | --har] [flags]
```

#### Specific Flags (select one - required)

| Flag        | Description                        |
| ----------- | ---------------------------------- |
| `--openapi` | Path to OpenAPI specification file |
| `--postman` | Path to Postman collection file    |
| `--har`     | Path to HAR (HTTP Archive) file    |

#### Examples

API scan with OpenAPI specification:

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest api \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --openapi ./api-spec.yml \
  --output ./api-results
```

API scan with Postman collection:

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest api \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --postman ./collection.json \
  --log-level debug
```

API scan with HAR file:

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest api \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --har ./traffic.har \
  --fail-on medium
```

### 4. Setup Command

Sets up authentication sessions for scanning.

#### Usage

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest setup --base-url <url> --environment-id <id> [flags]
```

#### Specific Flags

| Flag                   | Default | Description                    |
| ---------------------- | ------- | ------------------------------ |
| `--url`                | `""`    | URL of the application         |
| `--auth-session-uuid`  | `""`    | UUID of authentication session |
| `--setup-timeout`      | `300`   | Setup timeout in seconds       |
| `--setup-poll-ticker`  | `5`     | Setup poll ticker in seconds   |
| `--setup-poll-timeout` | `900`   | Setup poll timeout in seconds  |

#### Examples

Basic setup:

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest setup \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --url https://example.com
```

Setup with custom timeouts:

```
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest setup \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --url https://example.com \
  --setup-timeout 600 \
  --setup-poll-timeout 1200
```

### 5. Version Command

Displays the version information of the DAST CLI.

#### Usage

```
docker run checkmarx/dast:latest version
```

#### Example

```
docker run checkmarx/dast:latest version
# Output: DAST CLI version: 1.2.3
```

### 6. Manual Results

Use the `dast-cli manual-results` command to upload a JSON file of manual findings against a specific scan:

bash

```
dast-cli manual-results \
  --environment-id 75d4fe35-965a-4506-b226-e0155ec84c34 \
  --scan-id <SCAN_ID> \
  --path ./manual-findings.json \
  --all-future-scans
```

Use the following tables to understand and align your uploaded JSON file:

Finding object (findings\[])

\--indent-- Risk object (findings\[].risks\[]) add example too

#### Finding object (findings\[])

| Field         | Type            | Required | Allowed values / constraints                                                                                                                                                                                          |
| ------------- | --------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | string          | Required | non-empty                                                                                                                                                                                                             |
| `severity`    | string          | Required | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`                                                                                                                                                                           |
| `state`       | string          | Optional | Built-in: `To Verify`, `Not Exploitable`, `Proposed Not Exploitable`, `Urgent`, `Confirmed` — or a custom state name (only valid if the tenant has custom-states enabled and the caller has permission on that state) |
| `status`      | string          | Optional | `New`, `Recurrent`                                                                                                                                                                                                    |
| `description` | string          | Optional | free text                                                                                                                                                                                                             |
| `compliance`  | array of string | Optional | no further constraints                                                                                                                                                                                                |
| `resolution`  | string          | Optional | free text                                                                                                                                                                                                             |
| `confidence`  | string          | Optional | `LOW`, `MEDIUM`, `HIGH`                                                                                                                                                                                               |
| `cwe_id`      | string          | Optional | free text, no format check                                                                                                                                                                                            |
| `wasc_id`     | string          | Optional | free text                                                                                                                                                                                                             |
| `risks`       | array of Risk   | Optional | each item validated if present                                                                                                                                                                                        |

**Risk object (findings\[].risks\[])**

| Field             | Type   | Required | Allowed values / constraints                       |
| ----------------- | ------ | -------- | -------------------------------------------------- |
| `severity`        | string | Required | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`        |
| `state`           | string | Optional | Same rules as Finding's `state`                    |
| `status`          | string | Optional | `New`, `Recurrent`                                 |
| `method`          | string | Required | `GET`, `PUT`, `POST`, `DELETE`, `OPTIONS`, `PATCH` |
| `url`             | string | Required | non-empty (no URL-format validation)               |
| `path`            | string | Required | non-empty                                          |
| `evidence`        | string | Optional | free text                                          |
| `attack`          | string | Optional | free text                                          |
| `other_info`      | string | Optional | free text                                          |
| `request_header`  | string | Optional | free text                                          |
| `request_body`    | string | Optional | free text                                          |
| `response_header` | string | Optional | free text                                          |
| `response_body`   | string | Optional | free text                                          |

**Example**

```
{
  "only_current_scan": true,
  "findings": [
    {
      "name": "Reflected XSS in search parameter",
      "severity": "HIGH",
      "state": "Confirmed",
      "status": "New",
      "description": "User input is reflected without encoding.",
      "compliance": ["OWASP-A03"],
      "resolution": "Encode output before rendering.",
      "confidence": "HIGH",
      "cwe_id": "CWE-79",
      "wasc_id": "WASC-08",
      "risks": [
        {
          "severity": "HIGH",
          "state": "Confirmed",
          "status": "New",
          "method": "GET",
          "url": "https://target.example.com/search",
          "path": "/search",
          "evidence": "<script>alert(1)</script> reflected in response body",
          "attack": "q=<script>alert(1)</script>",
          "other_info": "",
          "request_header": "GET /search?q=%3Cscript%3E HTTP/1.1",
          "request_body": "",
          "response_header": "HTTP/1.1 200 OK",
          "response_body": "<html>...search results for <script>alert(1)</script>...</html>"
        }
      ]
    }
  ]
}
```

| Flag                 | Description                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| `--environment-id`   | Required The environment ID of your scan.                                                              |
| `--scan-id`          | Required The scan ID of the scan you are linking your results to.                                      |
| `--path`             | Required The path to the JSON file.                                                                    |
| `--all-future-scans` | Applies the uploaded results to future scans in the same environment in addition to the specified scan |
