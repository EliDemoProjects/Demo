# Installation and Initial Setup

## Initial Setup and Configuration

### Prerequisites

- You have an API Key for authenticating with Developer Assist
- For **VS Code**: supported for version 1.100.0 or above (supports both `settings.json` (v1.100–1.101) and `mcp.json` (v1.102+))
- For **VS Code**: you must have GitHub Copilot installed
- For **Kiro**: supported for version 0.6+ (latest version recommended)

### Installing and Configuring the Plugin

The instructions below cover the general setup for all supported IDEs. For detailed, IDE-specific steps, select the tab for your IDE.

1. Install the **Checkmarx Developer Assist** extension from the **Marketplace**.
2. In the IDE, open the extension, click on **Log in**, and enter your **API Key**.
3. Make sure that the Checkmarx Developer Assist MCP is running.
4. Optionally, adjust Checkmarx Developer Assist settings.

{% tabs %}
{% tab title="VS Code" %}
1. In the VS Code IDE main navigation, click on the **Extensions** icon.
2. Search for the **Checkmarx Developer Assist** extension, then click **Install** for that extension.

   ![ ](../.gitbook/assets/img-01cd9d9ffe8671d61fcc3ff7f72aadd7.png)

   The Developer Assist extension is installed and the Checkmarx icon appears in the left-side navigation panel.

3. Click on the Checkmarx extension icon.

   The **Checkmarx One Authentication** sidebar opens:

   ![ ](../.gitbook/assets/img-d6b6760b1203a07cad8e324f7c81786d.png)

4. In the **Checkmarx One Authentication** sidebar, click **Log in**.

   The Log in window opens:

   ![ ](../.gitbook/assets/img-558e508297b81530776c63c0918c7f63.png)

5. Enter your activation key in the **Checkmarx Developer Assist API Key** field and click **Log in**.

   The **Checkmarx Developer Assist Authentication** sidebar will now show that you are logged in:

   ![ ](../.gitbook/assets/img-d5d55c9d3c80613ae335039ba75f6d9c.png)

6. A Checkmarx Developer Assist welcome page is displayed immediately after a successful login. Scroll down and click on **Mark Done**.
7. Click **View** > **Command Palette** and enter **MCP:List Servers**.

   ![ ](../.gitbook/assets/img-39c7693cacb308149e58168a10d11ebd.png)

8. In the MCP servers list, select **Checkmarx Developer Assist**.
9. Click on **Start Server**.
10. You can optionally adjust the Checkmarx Developer Assist Settings as follows:
    1. Add **Additional Params** to set up custom configurations, such as proxy servers or to run in debug mode.
    2. Enable/disable specific realtime scanners. By default, all scanners are enabled.
    3. For IaC realtime scanner you can change the container platform used, Docker (default) or Podman.
    4. Select the **AI Assistant** to use for remediation. Options are **Copilot** (default) or **Claude**.
{% endtab %}

{% tab title="Cursor" %}
1. In the Cursor IDE, click on the **Extensions** icon.
2. Search for the **Checkmarx Developer Assist** extension, then click **Install** for that extension.

   The Developer Assist extension is installed.

3. Click the arrow next to the **Extensions** icon to open the drop-down menu. Then click the **pin** icon beside the **Checkmarx** extension to add it to the top navigation bar.
4. Click on the Checkmarx extension icon.

   The **Checkmarx Developer Assist Authentication** sidebar opens:

   ![ ](../.gitbook/assets/img-5eef0a2616e60ef6a18690774a5f2614.png)

5. In the **Checkmarx Developer Assist Authentication** sidebar, click **Log in**.

   The Log in window opens:

   ![ ](../.gitbook/assets/img-4c6ed2af31cf1bf9795da8d0fe826bdd.png)

6. Enter your activation key in the **Checkmarx Developer Assist API Key** field and click **Log in**.

   The **Checkmarx Developer Assist Authentication** sidebar will now show that you are logged in:

   ![ ](../.gitbook/assets/img-a744e5e8e8901caa5276e68a9ede5909.png)

7. A Checkmarx Developer Assist welcome page is displayed immediately after a successful login. Scroll down and click on **Mark Done**.
8. To verify that your MCP server is running: in **Cursor Settings** under **Tools & MCP** > **Installed MCP Servers**, confirm that the **Checkmarx Developer Assist** toggle is enabled.

   ![ ](../.gitbook/assets/img-5ecbd5e52c5fb5161fc8eb1a0f3c0a00.png)

9. You can optionally adjust the Checkmarx Developer Assist Settings as follows:
    1. Add **Additional Params** to set up custom configurations, such as proxy servers or to run in debug mode.
    2. Enable/disable specific realtime scanners. By default, all scanners are enabled.
    3. For IaC realtime scanner you can change the container platform used, Docker (default) or Podman.
    4. The IDE's built-in AI assistant is enabled by default. To use a different AI Assistant:
       - Disable **Prefer Native AI Assistant**.
       - Select the **AI Assistant** to use for remediation. Options are **Copilot** (default) or **Claude**.
{% endtab %}

{% tab title="Windsurf" %}
1. In the Windsurf IDE main navigation, click on the **Extensions** icon.
2. Search for the **Checkmarx Developer Assist** extension, then click **Install** for that extension.

   ![ ](../.gitbook/assets/img-ee0ba170f46e470180d7e774093b1b14.png)

   The Developer Assist extension is installed and the Checkmarx icon appears in the left-side navigation panel.

3. Click on the Checkmarx extension icon.

   The **Checkmarx Developer Assist Authentication** sidebar opens:

   ![ ](../.gitbook/assets/img-1b22d947c20665ceaae9387e769d5636.png)

4. In the **Checkmarx Developer Assist Authentication** sidebar, click **Log in**.

   The Log in window opens:

   ![ ](../.gitbook/assets/img-6c78f6d3a6a4a427b75640846c3e2b9f.png)

5. Enter your activation key in the **Checkmarx Developer Assist API Key** field and click **Log in**.

   The **Checkmarx Developer Assist Authentication** sidebar will now show that you are logged in:

   ![ ](../.gitbook/assets/img-25b9ce1269bea01209f77eb047315959.png)

6. A Checkmarx Developer Assist welcome page is displayed immediately after a successful login. Scroll down and click on **Mark Done**.
7. To verify that your MCP server is running:

   ![ ](../.gitbook/assets/img-73f8858306e005194cc779ea1f7f46cc.png)

   1. Go to **Settings** > **Windsurf Settings**.
   2. Under **Cascade**, click **Open MCP Marketplace**, and make sure that the **Checkmarx Developer Assist** MCP is installed and enabled.

8. You can optionally adjust the Checkmarx Developer Assist Settings as follows:
    1. Add **Additional Params** to set up custom configurations, such as proxy servers or to run in debug mode.
    2. Enable/disable specific realtime scanners. By default, all scanners are enabled.
    3. For IaC realtime scanner you can change the container platform used, Docker (default) or Podman.
    4. The IDE's built-in AI assistant is enabled by default. To use a different AI Assistant:
       - Disable **Prefer Native AI Assistant**.
       - Select the **AI Assistant** to use for remediation. Options are **Copilot** (default) or **Claude**.
{% endtab %}

{% tab title="Kiro" %}
1. In the Kiro IDE main navigation, click on the **Extensions** icon.
2. Search for the **Checkmarx Developer Assist** extension, then click **Install** for that extension.

   ![ ](../.gitbook/assets/img-3ba1d9fab93658e70d7adcc073efa658.png)

3. In the pop-up window, click **Trust Publisher and Install**.

   The Developer Assist extension is installed and the **Checkmarx** icon appears in the left-side navigation panel.

4. Click on the Checkmarx extension icon.

   The **Checkmarx Developer Assist Authentication** sidebar opens:

   ![ ](../.gitbook/assets/img-3618c003af0cefb85b2fe568a4c6605e.png)

5. In the **Checkmarx Developer Assist Authentication** sidebar, click **Log in**.

   The Log in window opens:

   ![ ](../.gitbook/assets/img-1a7b7107dc538758e993fab2d93f7aec.png)

6. Enter your activation key in the **Checkmarx Developer Assist API Key** field and click **Log in**.

   The **Checkmarx Developer Assist Authentication** sidebar will now show that you are logged in:

   ![ ](../.gitbook/assets/img-c5195b57a94266c197a67bd07cdf29f8.png)

7. A Checkmarx Developer Assist welcome page is displayed immediately after a successful login. Scroll down and click on **Mark Done**.
8. To verify that your MCP server is connected:

   ![ ](../.gitbook/assets/img-106b2291cb519d405901758f13bc9113.png)

   1. Select the **Kiro** icon in the left-side navigation panel.
   2. Under **MCP servers**, confirm that **Checkmarx Developer Assist** is connected.

9. You can optionally adjust the Checkmarx Developer Assist Settings as follows:
    1. Add **Additional Params** to set up custom configurations, such as proxy servers or to run in debug mode.
    2. Enable/disable specific realtime scanners. By default, all scanners are enabled.
    3. For IaC realtime scanner you can change the container platform used, Docker (default) or Podman.
    4. The IDE's built-in AI assistant is enabled by default. To use a different AI Assistant:
       - Disable **Prefer Native AI Assistant**.
       - Select the **AI Assistant** to use for remediation. Options are **Copilot** (default) or **Claude**.
{% endtab %}
{% endtabs %}

## Troubleshooting - Manually Configuring the MCP Server

In case the automatic procedure fails, you can manually configure access to the Checkmarx MCP server using the appropriate procedure for your IDE.

{% tabs %}
{% tab title="VS Code" %}
1. If it does not already exist, create an `mcp.json` file at the following location: `${homeDir}\AppData\Roaming\Code\User\mcp.json`
2. Add the "Checkmarx Developer Assist" MCP using the following snippet, replacing **\<Activation\_Key\>** with your Developer Assist Activation Key.

```json
{
   "servers": {
      "Checkmarx Developer Assist": {
         "url": "https://mea.ast.checkmarx.net/api/security-mcp/mcp",
         "headers": {
            "cx-origin": "VsCode",
            "Authorization": "<Activation_Key>"
         }
      }
   }
}
```

3. Start running the MCP server as follows:
   1. Click **View** > **Command Palette** and enter **MCP:List Servers**.

      ![ ](../.gitbook/assets/img-39c7693cacb308149e58168a10d11ebd.png)

   2. In the MCP servers list, select **Checkmarx Developer Assist**.
   3. Click on **Start Server**.
{% endtab %}

{% tab title="Cursor" %}
1. If it does not already exist, create an `mcp.json` file at the following location: `${homeDir}\.cursor\mcp.json`
2. Add the "Checkmarx Developer Assist" MCP using the following snippet, replacing **\<Activation\_Key\>** with your Developer Assist Activation Key.

```json
{
   "mcpServers": {
      "checkmarx Developer Assist": {
         "url": "https://mea.ast.checkmarx.net/api/security-mcp/mcp",
         "headers": {
            "cx-origin": "Cursor",
            "Authorization": "<Activation_Key>"
         }
      }
   }
}
```

3. Verify that your MCP server is running by opening **Cursor Settings** and under **Tools & MCP** > **Installed MCP Servers**, confirm that the **Checkmarx Developer Assist** toggle is enabled.

   ![ ](../.gitbook/assets/img-5ecbd5e52c5fb5161fc8eb1a0f3c0a00.png)
{% endtab %}

{% tab title="Windsurf" %}
1. If it does not already exist, create an `mcp_config.json` file at the following location: `${homeDir}\.codeium\windsurf\mcp_config.json`

   {% hint style="info" icon="pencil" %}
   If you are using windsurf-next, the file location should be `${homeDir}\.codeium\windsurf-next\mcp_config.json`
   {% endhint %}

2. Add the "Checkmarx Developer Assist" MCP using the following snippet, replacing **\<Activation\_Key\>** with your Developer Assist Activation Key.

```json
{
   "mcpServers": {
      "checkmarx Developer Assist": {
         "url": "https://mea.ast.checkmarx.net/api/security-mcp/mcp",
         "headers": {
            "cx-origin": "Windsurf",
            "Authorization": "<Activation_Key>"
         }
      }
   }
}
```

3. Go to **Settings** > **Windsurf Settings**, and under **Cascade**, click **Open MCP Marketplace**. Make sure that the Checkmarx Developer Assist MCP is installed and enabled.

   ![ ](../.gitbook/assets/img-a6a716d64adfffc1b755586fd8cdd84a.png)
{% endtab %}

{% tab title="Kiro" %}
1. If it does not already exist, create an `mcp.json` file at the following location: `${homeDir}\.kiro\settings\mcp.json`
2. Add the "Checkmarx Developer Assist" MCP using the following snippet, replacing **\<Activation\_Key\>** with your Developer Assist Activation Key.

```json
{
   "mcpServers": {
      "checkmarx Developer Assist": {
         "url": "https://mea.ast.checkmarx.net/api/security-mcp/mcp",
         "headers": {
            "cx-origin": "Kiro",
            "Authorization": "<Activation_Key>"
         }
      }
   }
}
```

3. Click on the **Kiro** icon in the left-side navigation, and under **MCP servers**, confirm that Checkmarx Developer Assist is connected.

   ![ ](../.gitbook/assets/img-fc56ec476d6b1e9093674b814e31c5e5.png)
{% endtab %}
{% endtabs %}
