---
description: Install and configure the Checkmarx Developer Assist plugin for JetBrains IDEs
---

# Installation and Initial Setup

{% hint style="warning" %}
The **Checkmarx Developer Assist** JetBrains plugin provides Developer Assist capabilities as a standalone experience. **Checkmarx One** customers with a Checkmarx One Assist license should use the [Checkmarx JetBrains Plugin](https://checkmarx.com), where Developer Assist is included as part of the Checkmarx One platform. The two plugins are mutually exclusive — ensure the Checkmarx plugin is uninstalled before installation.
{% endhint %}

## Prerequisites

- You have a Checkmarx Developer Activation Key.
- You are running IntelliJ version 2022.2+.
- **GitHub Copilot Chat** (AI Agent) version 1.5.62-243+ must be installed.

---

## Installing and Configuring the Plugin

The Checkmarx Developer Assist JetBrains Plugin is available on the JetBrains Marketplace and can be installed directly from your JetBrains IDE console.

**To install the plugin:**

{% stepper %}
{% step %}
### Open Plugins

Open your JetBrains IDE console (e.g., IntelliJ IDEA). Go to **Plugins** and click the **Marketplace** tab.
{% endstep %}

{% step %}
### Install

Search for the **Checkmarx Developer Assist** plugin, then click **Install**.

![Installing the plugin from JetBrains Marketplace](../.gitbook/assets/img-d13e82645c7fc7dc70e6909e160012bd.png)
{% endstep %}
{% endstepper %}

**To configure the plugin:**

{% stepper %}
{% step %}
### Open Settings

Open the IDE **settings**.
{% endstep %}

{% step %}
### Navigate to plugin settings

Drill down to **Tools** > **Checkmarx Developer Assist**.
{% endstep %}

{% step %}
### Enter activation key

Enter your activation key in the **Developer Assist API Key** field and click **Sign in**.

![Entering the API key](../.gitbook/assets/img-de0f163499e76b0588b5084d9ca2ca9d.png)
{% endstep %}

{% step %}
### Welcome page

A Checkmarx Developer Assist welcome page is displayed immediately after successful login. Close the window to proceed.

![Welcome page](../.gitbook/assets/img-8804289f11edc112f9fd85a1021d7a43.png)
{% endstep %}

{% step %}
### Optional additional params

You can optionally add **Additional Params** to set up custom configurations, such as proxy servers or debug mode.
{% endstep %}

{% step %}
### Install MCP

Click on **Go to Realtime Scanners** and select **Install MCP**.

The Checkmarx MCP is added to your `mcp.json` file.

{% hint style="info" %}
In some cases the MCP is installed automatically when you authenticate. Best practice is to click **Install MCP** so the MCP file opens and you can verify it starts running.
{% endhint %}
{% endstep %}

{% step %}
### Configure scanners

You can enable/disable specific realtime scanners. By default, all scanners are enabled.
{% endstep %}

{% step %}
### Configure IaC container tool

For the IaC Realtime scanner, select the **Containers Management Tool** used in your environment: **docker** or **podman**.

For **Windows:** Verify that the selected Container Management Tool is installed on your system.

For **macOS and Linux:** Verify that docker or podman is installed in `/usr/local/bin`. If installed in a different location, create a symbolic link:

**For docker:**

1. Check the path: `which docker`
2. Create a symbolic link: `sudo ln -s <PATH_FROM_ABOVE> /usr/local/bin/docker`
3. Pull the required KICS image: `docker pull checkmarx/kics:v2.1.29`

{% hint style="warning" %}
The change will not register until you close and restart the IDE.
{% endhint %}

**For podman:**

1. Check the path: `which podman`
2. Create a symbolic link: `sudo ln -s <PATH_FROM_ABOVE> /usr/local/bin/podman`
3. Pull the required KICS image: `podman pull checkmarx/kics:v2.1.29`

{% hint style="warning" %}
The change will not register until you close and restart the IDE.
{% endhint %}
{% endstep %}
{% endstepper %}

---

## Troubleshooting — Manually Configuring the MCP Server

If the automatic installation procedure fails, you can manually configure access to the Checkmarx MCP server.

1. If it does not already exist, create an `mcp.json` file at: `${homeDir}\AppData\Local\github-copilot\intellij\mcp.json`

2. Add the Checkmarx Developer Assist MCP using the following snippet, replacing `<Activation_Key>` with your Developer Assist Activation Key:

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
