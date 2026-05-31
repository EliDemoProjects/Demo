# Installation and Initial Setup

{% hint style="warning" %}
The **Checkmarx Developer Assist** JetBrains plugin provides Developer Assist capabilities as a standalone experience. **Checkmarx One** customers with a Checkmarx One Assist license should use the [Checkmarx JetBrains Plugin](https://checkmarx.com), where Developer Assist is included as part of the Checkmarx One platform. The **Checkmarx Developer Assist** and **Checkmarx** JetBrains plugins are mutually exclusive. To use the Checkmarx Developer Assist plugin, ensure that the Checkmarx plugin is uninstalled before installation.
{% endhint %}

## Prerequisites

* You have a Checkmarx Developer Activation Key.
* You are running IntelliJ version 2022.2+.
* You have **GitHub Copilot Chat** (AI Agent) version 1.5.62-243+ installed.

## Installing and Configuring the Plugin

The Checkmarx Developer Assist JetBrains Plugin is available on the JetBrains Marketplace and can be installed directly from your JetBrains IDE.

**To install the plugin from the marketplace:**

1. Open your JetBrains IDE (e.g., IntelliJ IDEA).
2. Go to **Plugins** and click the **Marketplace** tab.
3. Search for **Checkmarx Developer Assist**, then click **Install**.

**To configure the plugin:**

1. Open the IDE **Settings**.
2. Navigate to **Tools** > **Checkmarx Developer Assist**.
3. Enter your activation key in the **Developer Assist API Key** field and click **Sign in**.
4. A Checkmarx Developer Assist welcome page is displayed after a successful login. Close the window to proceed.
5. You can optionally add **Additional Params** to set up custom configurations such as proxy servers or debug mode.
6.  Click **Go to Realtime Scanners** and select **Install MCP**.

    The Checkmarx MCP is added to your `mcp.json` file.

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>In some cases the MCP is installed automatically when you authenticate with Checkmarx. However, best practice is to click <strong>Install MCP</strong> so that the MCP file opens and you can ensure that it starts running.</p></div>
7. You can enable or disable specific realtime scanners. By default, all scanners are enabled.
8. For the IaC Realtime scanner, select the **Containers Management Tool** used in your environment — either **docker** or **podman**.
   * **Windows**: Verify that the Container Management Tool selected is installed on your system.
   *   **macOS** and **Linux**: Verify that docker or podman is installed in `/usr/local/bin`.

       If docker or podman is installed in a different location, create a symbolic link:

       **For docker:**

       1. Check the installation path (in terminal, _not_ in IntelliJ): `which docker`
       2. Create a symbolic link: `sudo ln -s <PASTE_THE_PATH_HERE> /usr/local/bin/docker` For example, if `which docker` returned `/opt/homebrew/bin/docker`, run `sudo ln -s /opt/homebrew/bin/docker /usr/local/bin/docker`.
       3.  Pull the required KICS images: `docker pull checkmarx/kics:v2.1.29`

           <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>The change will not register until you close and restart the IDE.</p></div>

       **For podman:**

       1. Check the installation path (in terminal, _not_ in IntelliJ): `which podman`
       2. Create a symbolic link: `sudo ln -s <PASTE_THE_PATH_HERE> /usr/local/bin/podman` For example, if `which podman` returned `/opt/homebrew/bin/podman`, run `sudo ln -s /opt/homebrew/bin/podman /usr/local/bin/podman`.
       3.  Pull the required KICS images: `podman pull checkmarx/kics:v2.1.29`

           <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>The change will not register until you close and restart the IDE.</p></div>

## Troubleshooting – Manually Configuring the MCP Server

If the automatic MCP installation fails, you can manually configure access to the Checkmarx MCP server.

1.  If it does not already exist, create an `mcp.json` file at the following location:

    ```
    ${homeDir}\AppData\Local\github-copilot\intellij\mcp.json
    ```
2.  Add the Checkmarx Developer Assist MCP entry using the following snippet, replacing `<Activation_Key>` with your Developer Assist Activation Key:

    ```json
    {
      "servers": {
        "Checkmarx Developer Assist": {
          "url": "https://mea.ast.checkmarx.net/api/security-mcp/mcp",
          "headers": {
            "cx-origin": "Jetbrains",
            "Authorization": "<Activation_Key>"
          }
        }
      }
    }
    ```
