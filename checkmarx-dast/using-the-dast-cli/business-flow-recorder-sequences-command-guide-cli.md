# Business Flow Recorder - Sequences Command Guide (CLI)

The `sequences` command configures business flow recordings and sequences for a Checkmarx DAST environment. It uploads a set of recording files (`.zst`) and organizes them into named sequences that the scanner replays during a DAST scan. Each run fully replaces any recordings and sequences previously configured for that environment.

## Prerequisites

- Docker installed and access to the `checkmarx/dast:latest` image
- A Checkmarx API key (`CX_APIKEY`)
- The environment ID you want to configure
- Your Checkmarx One base URL
- One or more `.zst` recording files produced by the ZAP Recorder extension

To set up a recorder sequence, perform the following:

1. Prepare Your Recording File: Each recording file is a `.zst` archive of recorded UI actions, produced by the ZAP Recorder extension. Place all the files you want to upload in a local directory.

   ```
   ./
     login.zst
     checkout.zst
     logout.zst
   ```

   {% hint style="info" %}
   The name used to reference a recording inside the sequence config is always the file's **basename** - for example, `./login.zst` is referenced as `login.zst`.
   {% endhint %}

2. Define Your Sequences: A sequence is a named, ordered list of recordings. You pass sequences as a JSON array via the `--sequence-config` flag.

   Single Sequence

   ```json
   [
     {
       "name": "login-flow",
       "recordings": ["login.zst"]
     }
   ]
   ```

   Multiple Sequences

   ```json
   [
     {
       "name": "purchase-flow",
       "recordings": ["login.zst", "checkout.zst", "logout.zst"]
     },
     {
       "name": "login-only",
       "recordings": ["login.zst"]
     }
   ]
   ```

   Each `recordings` entry must match the basename of a file you pass via `--recording-file`. The order of entries in `recordings` is the order they will be replayed.

3. Run the Command

   ```bash
   docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest sequences \
     --base-url https://ast.checkmarx.net \
     --environment-id 12345678-abcd-1234-5678-123456789012 \
     --recording-file ./login.zst \
     --recording-file ./checkout.zst \
     --sequence-config '[{"name":"purchase-flow","recordings":["login.zst","checkout.zst"]}]'
   ```

   {% hint style="info" %}
   Pass `--recording-file` once per file. The command exits with code `0` on success and `2` on any error.
   {% endhint %}

   | Flag | Required | Description |
   | --- | --- | --- |
   | `--environment-id` | Yes | The ID of the environment previously created in the Checkmarx frontend |
   | `--base-url` | Yes | Your Checkmarx platform URL (e.g. `https://us.ast.checkmarx.net`) |
   | `--recording-file` | Yes (repeatable) | Path to a `.zst` recording file inside the container. Repeat the flag for each file. |
   | `--sequence-config` | Yes | JSON array defining the sequences and which recordings they include (see Step 2) |

## Example and Tips

```bash
docker run -e CX_APIKEY=[eyJK...] checkmarx/dast:latest sequences \
  --base-url https://ast.checkmarx.net \
  --environment-id 12345678-abcd-1234-5678-123456789012 \
  --recording-file ./login.zst \
  --recording-file ./checkout.zst \
  --recording-file ./logout.zst \
  --sequence-config '[{"name":"purchase-flow","recordings":["login.zst","checkout.zst","logout.zst"]},{"name":"login-only","recordings":["login.zst"]}]'
```

On success you will see: Recordings and sequences configured successfully.

- **Full replacement:** Every run deletes all existing recordings and sequences for the environment before uploading the new ones. The command is not additive.
- **Recording names:** The name used in `--sequence-config` must match the file's basename exactly, including the `.zst` extension.
- **Duplicate names:** Passing two `--recording-file` paths with the same basename, or defining two sequences with the same name, will cause the command to exit with an error before making any changes.
- **Empty sequences:** Every sequence must contain at least one recording. A sequence with an empty `recordings` array is rejected.
- **Unknown recording references:** If `--sequence-config` references a recording name that was not provided via `--recording-file`, the command will exit with an error.
- The `CX_APIKEY` environment variable is required for authentication. It is the API key generated from Checkmarx One.
