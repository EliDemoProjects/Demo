---
description: Install and configure the Checkmarx Developer Assist extension for VS Code, Cursor, Windsurf, and Kiro
---

# Installation and Initial Setup

## Initial Setup and Configuration

### Prerequisites

- You have an API Key for authenticating with Developer Assist.
- **VS Code:** Version 1.100.0 or above (supports both `settings.json` v1.100–1.101 and `mcp.json` v1.102+).
- **VS Code:** GitHub Copilot must be installed.
- **Kiro:** Version 0.6+ (latest version recommended).

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

1. In the VS Code IDE main navigation, click on the **Extensions** icon.

2. Search for the **Checkmarx Developer Assist** extension, then click **Install**.

   ![Install the Checkmarx Developer Assist extension from the VS Code Marketplace](.gitbook/assets/img-01cd9d9ffe8671d61fcc3ff7f72aadd7.png)

   The Developer Assist extension is installed and the Checkmarx icon appears in the left-side navigation panel.

3. Click on the Checkmarx extension icon. The **Checkmarx One Authentication** sidebar opens.

   ![Checkmarx One Authentication sidebar](.gitbook/assets/img-d6b6760b1203a07cad8e324f7c81786d.png)

4. In the sidebar, click **Log in**. The Log in window opens.

   ![Log in window](.gitbook/assets/img-558e508297b81530776c63c0918c7f63.png)

5. Enter your activation key in the **Checkmarx Developer Assist API Key** field and click **Log in**.

   The **Checkmarx Developer Assist Authentication** sidebar will now show that you are logged in.

   ![Logged in state](.gitbook/assets/img-d5d55c9d3c80613ae335039ba75f6d9c.png)

6. A welcome page is displayed after successful login. Scroll down and click **Mark Done**.

7. Click **View** > **Command Palette** and enter **MCP:List Servers**.

   ![MCP List Servers command](.gitbook/assets/img-39c7693cacb308149e58168a10d11ebd.png)

8. In the MCP servers list, select **Checkmarx Developer Assist**.

9. Click **Start Server**.

10. Optionally adjust settings:
    - Add **Additional Params** for proxy servers or debug mode.
    - Enable/disable specific realtime scanners (all enabled by default).
    - For IaC scanner: change the container platform (Docker by default, or Podman).
    - Select the **AI Assistant** for remediation: **Copilot** (default) or **Claude**.

{% endtab %}
{% tab title="Cursor" %}

{% embed url="https://player.vimeo.com/video/1165343738" %}
Cursor installation walkthrough
{% endembed %}

1. In the Cursor IDE, click on the **Extensions** icon.

2. Search for the **Checkmarx Developer Assist** extension, then click **Install**.

3. Click the arrow next to the Extensions icon to open the drop-down menu. Click the **pin** icon beside the **Checkmarx** extension to add it to the top navigation bar.

4. Click on the Checkmarx extension icon. The **Checkmarx Developer Assist Authentication** sidebar opens.

   ![Cursor authentication sidebar](.gitbook/assets/img-5eef0a2616e60ef6a18690774a5f2614.png)

5. Click **Log in**. The Log in window opens.

   ![Log in window](.gitbook/assets/img-4c6ed2af31cf1bf9795da8d0fe826bdd.png)

6. Enter your activation key in the **Checkmarx Developer Assist API Key** field and click **Log in**.

   ![Logged in state](.gitbook/assets/img-a744e5e8e8901caa5276e68a9ede5909.png)

7. A welcome page is displayed after successful login. Scroll down and click **Mark Done**.

8. Verify MCP is running: in **Cursor Settings** under **Tools & MCP** > **Installed MCP Servers**, confirm the **Checkmarx Developer Assist** toggle is enabled.

   ![Cursor MCP Servers list](.gitbook/assets/img-5ecbd5e52c5fb5161fc8eb1a0f3c0a00.png)

9. Optionally adjust settings:
    - Add **Additional Params** for proxy servers or debug mode.
    - Enable/disable specific realtime scanners.
    - For IaC scanner: change the container platform.
    - The IDE's built-in AI assistant is enabled by default. To use a different one: disable **Prefer Native AI Assistant**, then select **Copilot** or **Claude**.

{% endtab %}
{% tab title="Windsurf" %}

{% embed url="https://player.vimeo.com/video/1165305636" %}
Windsurf installation walkthrough
{% endembed %}

1. In the Windsurf IDE main navigation, click on the **Extensions** icon.

2. Search for the **Checkmarx Developer Assist** extension, then click **Install**.

   ![Installing in Windsurf](.gitbook/assets/img-ee0ba170f46e470180d7e774093b1b14.png)

3. Click on the Checkmarx extension icon. The **Checkmarx Developer Assist Authentication** sidebar opens.

   ![Windsurf authentication sidebar](.gitbook/assets/img-1b22d947c20665ceaae9387e769d5636.png)

4. Click **Log in**. The Log in window opens.

   ![Log in window](.gitbook/assets/img-6c78f6d3a6a4a427b75640846c3e2b9f.png)

5. Enter your activation key and click **Log in**.

   ![Logged in state](.gitbook/assets/img-25b9ce1269bea01209f77eb047315959.png)

6. A welcome page is displayed after successful login. Scroll down and click **Mark Done**.

7. Verify MCP is running:

   ![Windsurf MCP settings](.gitbook/assets/img-73f8858306e005194cc779ea1f7f46cc.png)

   Go to **Settings** > **Windsurf Settings**. Under **Cascade**, click **Open MCP Marketplace** and confirm the **Checkmarx Developer Assist** MCP is installed and enabled.

8. Optionally adjust settings:
    - Add **Additional Params** for proxy servers or debug mode.
    - Enable/disable specific realtime scanners.
    - For IaC scanner: change the container platform.
    - The IDE's built-in AI assistant is enabled by default. To use a different one: disable **Prefer Native AI Assistant**, then select **Copilot** or **Claude**.

{% endtab %}
{% tab title="Kiro" %}

{% embed url="https://player.vimeo.com/video/1166288643" %}
Kiro installation walkthrough
{% endembed %}

1. In the Kiro IDE main navigation, click on the **Extensions** icon.

2. Search for the **Checkmarx Developer Assist** extension, then click **Install**.

   ![Installing in Kiro](.gitbook/assets/img-3ba1d9fab93658e70d7adcc073efa658.png)

3. In the pop-up window, click **Trust Publisher and Install**.

4. Click on the Checkmarx extension icon. The **Checkmarx Developer Assist Authentication** sidebar opens.

   ![Kiro authentication sidebar](.gitbook/assets/img-3618c003af0cefb85b2fe568a4c6605e.png)

5. Click **Log in**. The Log in window opens.

   ![Log in window](.gitbook/assets/img-1a7b7107dc538758e993fab2d93f7aec.png)

6. Enter your activation key and click **Log in**.

   ![Logged in state](.gitbook/assets/img-c5195b57a94266c197a67bd07cdf29f8.png)

7. A welcome page is displayed after successful login. Scroll down and click **Mark Done**.

8. Verify MCP is connected:

   ![Kiro MCP servers](.gitbook/assets/img-106b2291cb519d405901758f13bc9113.png)

   Select the **Kiro** icon in the left-side navigation panel. Under **MCP servers**, confirm that **Checkmarx Developer Assist** is connected.

9. Optionally adjust settings:
    - Add **Additional Params** for proxy servers or debug mode.
    - Enable/disable specific realtime scanners.
    - For IaC scanner: change the container platform.
    - The IDE's built-in AI assistant is enabled by default. To use a different one: disable **Prefer Native AI Assistant**, then select **Copilot** or **Claude**.

{% endtab %}
{% endtabs %}

---

## Troubleshooting — Manually Configuring the MCP Server

If the automatic installation procedure fails, you can manually configure access to the Checkmarx MCP server.

{% tabs %}
{% tab title="VS Code" %}

1. If it does not already exist, create an `mcp.json` file at: `${homeDir}\AppData\Roaming\Code\User\mcp.json`

2. Add the Checkmarx Developer Assist MCP using the following snippet, replacing `<Activation_Key>` with your Developer Assist Activation Key:

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

3. Start the MCP server:
   - Click **View** > **Command Palette** and enter **MCP:List Servers**.
   - Select **Checkmarx Developer Assist**.
   - Click **Start Server**.

{% endtab %}
{% tab title="Cursor" %}

1. If it does not already exist, create an `mcp.json` file at: `${homeDir}\.cursor\mcp.json`

2. Add the following snippet, replacing `<Activation_Key>` with your key:

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

3. Verify in **Cursor Settings** under **Tools & MCP** > **Installed MCP Servers** that the **Checkmarx Developer Assist** toggle is enabled.

   ![Cursor MCP enabled](.gitbook/assets/img-5ecbd5e52c5fb5161fc8eb1a0f3c0a00.png)

{% endtab %}
{% tab title="Windsurf" %}

1. If it does not already exist, create an `mcp_config.json` file at: `${homeDir}\.codeium\windsurf\mcp_config.json`

   {% hint style="info" %}
   If you are using windsurf-next, the file location should be `${homeDir}\.codeium\windsurf-next\mcp_config.json`
   {% endhint %}

2. Add the following snippet, replacing `<Activation_Key>` with your key:

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

3. Go to **Settings** > **Windsurf Settings**. Under **Cascade**, click **Open MCP Marketplace** and make sure the Checkmarx Developer Assist MCP is installed and enabled.

{% endtab %}
{% tab title="Kiro" %}

1. If it does not already exist, create an `mcp.json` file at: `${homeDir}\.kiro\settings\mcp.json`

2. Add the following snippet, replacing `<Activation_Key>` with your key:

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

3. Click on the **Kiro** icon in the left-side navigation. Under **MCP servers**, confirm that Checkmarx Developer Assist is connected.

   ![Kiro MCP connected](.gitbook/assets/img-fc56ec476d6b1e9093674b814e31c5e5.png)

{% endtab %}
{% endtabs %}
