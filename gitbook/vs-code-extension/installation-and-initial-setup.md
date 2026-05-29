# installation and initial setup

## Initial Setup and Configuration

### Prerequisites

* You have an API Key for authenticating with Developer Assist.
* **VS Code:** Version 1.100.0 or above (supports both `settings.json` v1.100–v1.101 and `mcp.json` v1.102+).
* **VS Code:** GitHub Copilot must be installed.
* **Kiro:** Version 0.6+ (latest version recommended).

### Installing and Configuring the Plugin

The instructions below cover the general setup for all supported IDEs. Open the collapsible section for your specific IDE for detailed steps.

{% stepper %}
{% step %}
### Install the extension

Install the **Checkmarx Developer Assist** extension from the **Marketplace**.
{% endstep %}

{% step %}
### Log in

In the IDE, open the extension, click **Log in**, and enter your **API Key**.
{% endstep %}

{% step %}
### Verify MCP

Make sure that the Checkmarx Developer Assist MCP is running.
{% endstep %}

{% step %}
### Optional settings

Optionally, adjust Checkmarx Developer Assist settings.
{% endstep %}
{% endstepper %}

{% tabs %}
{% tab title="VS Code" %}
{% embed url="https://player.vimeo.com/video/1165137006" %}
VS Code installation walkthrough
{% endembed %}

{% stepper %}
{% step %}
### Install the extension

In the VS Code IDE main navigation, click on the **Extensions** icon.

Search for the **Checkmarx Developer Assist** extension, then click **Install**.

The Developer Assist extension is installed and the Checkmarx icon appears in the left-side navigation panel.
{% endstep %}

{% step %}
### Log in

Click on the Checkmarx extension icon. The **Checkmarx One Authentication** sidebar opens.

In the sidebar, click **Log in**. The Log in window opens.

Enter your activation key in the **Checkmarx Developer Assist API Key** field and click **Log in**.

The **Checkmarx Developer Assist Authentication** sidebar will now show that you are logged in.

A welcome page is displayed after successful login. Scroll down and click **Mark Done**.
{% endstep %}

{% step %}
### Verify MCP

Click **View** > **Command Palette** and enter **MCP:List Servers**.

In the MCP servers list, select **Checkmarx Developer Assist**.

Click **Start Server**.
{% endstep %}

{% step %}
### Optional settings

Optionally adjust settings:

* Add **Additional Params** for proxy servers or debug mode.
* Enable/disable specific realtime scanners (all enabled by default).
* For IaC scanner: change the container platform (Docker by default, or Podman).
* Select the **AI Assistant** for remediation: **Copilot** (default) or **Claude**.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Cursor" %}
{% embed url="https://player.vimeo.com/video/1165343738" %}
Cursor installation walkthrough
{% endembed %}

{% stepper %}
{% step %}
### Install the extension

In the Cursor IDE, click on the **Extensions** icon.

Search for the **Checkmarx Developer Assist** extension, then click **Install**.

Click the arrow next to the Extensions icon to open the drop-down menu. Click the **pin** icon beside the **Checkmarx** extension to add it to the top navigation bar.
{% endstep %}

{% step %}
### Log in

Click on the Checkmarx extension icon. The **Checkmarx Developer Assist Authentication** sidebar opens.

Click **Log in**. The Log in window opens.

Enter your activation key in the **Checkmarx Developer Assist API Key** field and click **Log in**.

A welcome page is displayed after successful login. Scroll down and click **Mark Done**.
{% endstep %}

{% step %}
### Verify MCP

In **Cursor Settings** under **Tools & MCP** > **Installed MCP Servers**, confirm the **Checkmarx Developer Assist** toggle is enabled.
{% endstep %}

{% step %}
### Optional settings

Optionally adjust settings:

* Add **Additional Params** for proxy servers or debug mode.
* Enable/disable specific realtime scanners.
* For IaC scanner: change the container platform.
* The IDE's built-in AI assistant is enabled by default. To use a different one: disable **Prefer Native AI Assistant**, then select **Copilot** or **Claude**.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Windsurf" %}
{% embed url="https://player.vimeo.com/video/1165305636" %}
Windsurf installation walkthrough
{% endembed %}

{% stepper %}
{% step %}
### Install the extension

In the Windsurf IDE main navigation, click on the **Extensions** icon.

Search for the **Checkmarx Developer Assist** extension, then click **Install**.
{% endstep %}

{% step %}
### Log in

Click on the Checkmarx extension icon. The **Checkmarx Developer Assist Authentication** sidebar opens.

Click **Log in**. The Log in window opens.

Enter your activation key and click **Log in**.

A welcome page is displayed after successful login. Scroll down and click **Mark Done**.
{% endstep %}

{% step %}
### Verify MCP

Go to **Settings** > **Windsurf Settings**. Under **Cascade**, click **Open MCP Marketplace** and confirm the **Checkmarx Developer Assist** MCP is installed and enabled.
{% endstep %}

{% step %}
### Optional settings

Optionally adjust settings:

* Add **Additional Params** for proxy servers or debug mode.
* Enable/disable specific realtime scanners.
* For IaC scanner: change the container platform.
* The IDE's built-in AI assistant is enabled by default. To use a different one: disable **Prefer Native AI Assistant**, then select **Copilot** or **Claude**.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Kiro" %}
{% embed url="https://player.vimeo.com/video/1166288643" %}
Kiro installation walkthrough
{% endembed %}

{% stepper %}
{% step %}
### Install the extension

In the Kiro IDE main navigation, click on the **Extensions** icon.

Search for the **Checkmarx Developer Assist** extension, then click **Install**.

In the pop-up window, click **Trust Publisher and Install**.
{% endstep %}

{% step %}
### Log in

Click on the Checkmarx extension icon. The **Checkmarx Developer Assist Authentication** sidebar opens.

Click **Log in**. The Log in window opens.

Enter your activation key and click **Log in**.

A welcome page is displayed after successful login. Scroll down and click **Mark Done**.
{% endstep %}

{% step %}
### Verify MCP

Select the **Kiro** icon in the left-side navigation panel. Under **MCP servers**, confirm that **Checkmarx Developer Assist** is connected.
{% endstep %}

{% step %}
### Optional settings

Optionally adjust settings:

* Add **Additional Params** for proxy servers or debug mode.
* Enable/disable specific realtime scanners.
* For IaC scanner: change the container platform.
* The IDE's built-in AI assistant is enabled by default. To use a different one: disable **Prefer Native AI Assistant**, then select **Copilot** or **Claude**.
{% endstep %}
{% endstepper %}
{% endtab %}
{% endtabs %}

***

## Troubleshooting — Manually Configuring the MCP Server

If the automatic installation procedure fails, you can manually configure access to the Checkmarx MCP server.

{% tabs %}
{% tab title="VS Code" %}
{% stepper %}
{% step %}
### Create the MCP file

If it does not already exist, create an `mcp.json` file at: `${homeDir}\AppData\Roaming\Code\User\mcp.json`
{% endstep %}

{% step %}
### Add the MCP configuration

Add the Checkmarx Developer Assist MCP using the following snippet, replacing `<Activation_Key>` with your Developer Assist Activation Key:

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
{% endstep %}

{% step %}
### Start the MCP server

* Click **View** > **Command Palette** and enter **MCP:List Servers**.
* Select **Checkmarx Developer Assist**.
* Click **Start Server**.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Cursor" %}
{% stepper %}
{% step %}
### Create the MCP file

If it does not already exist, create an `mcp.json` file at: `${homeDir}\.cursor\mcp.json`
{% endstep %}

{% step %}
### Add the MCP configuration

Add the following snippet, replacing `<Activation_Key>` with your key:

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
{% endstep %}

{% step %}
### Verify MCP

In **Cursor Settings** under **Tools & MCP** > **Installed MCP Servers** confirm the **Checkmarx Developer Assist** toggle is enabled.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Windsurf" %}
{% stepper %}
{% step %}
### Create the MCP file

If it does not already exist, create an `mcp_config.json` file at: `${homeDir}\.codeium\windsurf\mcp_config.json`

{% hint style="info" %}
If you are using windsurf-next, the file location should be `${homeDir}\.codeium\windsurf-next\mcp_config.json`
{% endhint %}
{% endstep %}

{% step %}
### Add the MCP configuration

Add the following snippet, replacing `<Activation_Key>` with your key:

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
{% endstep %}

{% step %}
### Verify MCP

Go to **Settings** > **Windsurf Settings**. Under **Cascade**, click **Open MCP Marketplace** and make sure the Checkmarx Developer Assist MCP is installed and enabled.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="Kiro" %}
{% stepper %}
{% step %}
### Create the MCP file

If it does not already exist, create an `mcp.json` file at: `${homeDir}\.kiro\settings\mcp.json`
{% endstep %}

{% step %}
### Add the MCP configuration

Add the following snippet, replacing `<Activation_Key>` with your key:

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
{% endstep %}

{% step %}
### Verify MCP

Click on the **Kiro** icon in the left-side navigation. Under **MCP servers**, confirm that Checkmarx Developer Assist is connected.
{% endstep %}
{% endstepper %}
{% endtab %}
{% endtabs %}
