---
description: How to detect and remediate security risks using Checkmarx Developer Assist in VS Code
---

# Using Developer Assist for Detection and Remediation

## AI Remediation

{% embed url="https://player.vimeo.com/video/1160134485" %}
AI Remediation demo
{% endembed %}

### How to Remediate Risks Using AI

The following procedure explains how to remediate risks by clicking the Fix button for a particular risk. You can also request remediation via chat with your AI Agent.

{% stepper %}
{% step %}
### Identify the risk

When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem** — marked in the code with a squiggly underline and annotated in the margin with an icon indicating the risk type.

![Risk flagged in code](../.gitbook/assets/img-8b30ebc58d203cf69432bb233991474a.png)
{% endstep %}

{% step %}
### Open the dialog

Hover over the vulnerable line of code. The Checkmarx dialog opens.
{% endstep %}

{% step %}
### Initiate remediation

Click **Fix with Checkmarx Developer Assist**.

![Fix with Developer Assist option](../.gitbook/assets/img-13fe029e47946a4efb78d53865fb74b6.png)

A Copilot session opens in the side panel and all relevant info is sent for analysis.

{% hint style="info" %}
Depending on your IDE configuration, you may need to click **Continue** several times to complete the process.
{% endhint %}
{% endstep %}

{% step %}
### Accept or refine

Copilot automatically makes the necessary code changes to remediate the risk.

- If you approve the change, click **Accept**. The change is made and the code is rescanned to verify the risk is no longer present.
- If you want to improve the suggestion, click **Undo**. You can then chat with Copilot to determine the best remediation approach.
{% endstep %}
{% endstepper %}

### Remediation via Chat

You can submit a request for Dev Assist remediation via natural language chat with your AI Agent. Just say that you want to fix a security risk and indicate which risk(s) you want to fix. Your AI will automatically route the request to the Checkmarx MCP.

Example chat requests:

- "Fix the vulnerability in line 26"
- "Fix all critical vulnerabilities"
- "Fix all SQL Injection risks"
- "Remediate all vulnerable packages"
- "Correct all critical issues in my JavaFile.java"

**Things to know about Dev Assist Chat:**

- No need to mention "Checkmarx" explicitly — once Dev Assist is installed and running, all remediation requests are handled via Checkmarx MCP.
- Multi-language prompts are supported.
- Effective in a single message context; improved accuracy in the context of an existing thread or finding.
- By default, requests are interpreted in the context of the current open file. You can specify a different file in your workspace.

---

### How to Understand Risks Using AI

{% stepper %}
{% step %}
### Identify the risk

When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem** in the code.

![Risk flagged in code](../.gitbook/assets/img-8b30ebc58d203cf69432bb233991474a.png)
{% endstep %}

{% step %}
### Open the dialog

Hover over the vulnerable line of code. The Checkmarx dialog opens.
{% endstep %}

{% step %}
### View details

Click **View details**.

![View details option](../.gitbook/assets/img-ea6756f4b9eaa29b4671b352492a359a.png)

A Copilot session opens in the side panel.

{% hint style="info" %}
Depending on your IDE configuration, you may need to click **Continue** several times to complete the process.
{% endhint %}
{% endstep %}

{% step %}
### Chat for clarification

Copilot explains the precise nature of the risk in the context of your code. You can chat with Copilot to ask for further clarification.
{% endstep %}
{% endstepper %}

---

## Ignoring Risks

To help you focus on actionable risks, Checkmarx Dev Assist enables marking risks as **Ignored** so they no longer appear in your IDE. You can **Revive** a risk at any time. This can be applied to a specific instance of a risk or to all instances of that risk in your project.

{% hint style="info" %}
For risks identified in open source packages, a risk instance refers to the entire package that the vulnerability is associated with.
{% endhint %}

**To ignore a risk:**

{% stepper %}
{% step %}
### Identify the risk

When a risk is flagged, hover over the vulnerable line of code. The Checkmarx dialog opens.

![Checkmarx dialog with ignore options](../.gitbook/assets/img-999c6f8e74bccdfdd57a2c20eb26bec9.png)
{% endstep %}

{% step %}
### Choose ignore scope

- To ignore this particular instance: click **Ignore this vulnerability**.
- To ignore all instances of this risk: click **Ignore all of this type**.
{% endstep %}
{% endstepper %}

**To revive a risk:**

1. Click the **Ignore** icon in the bottom bar.

   ![Ignore icon in bottom bar](../.gitbook/assets/img-ebaacd1e8161e192a6584a7f20c2d22b.png)

2. The **Ignored Vulnerabilities** tab opens.

   ![Ignored Vulnerabilities tab](../.gitbook/assets/img-059c35009247a914982566066c4d3be5.png)

3. For the desired vulnerability, click the **Revive** button.

   {% hint style="info" %}
   Reviving can also be done as a bulk action for all selected items.
   {% endhint %}

---

## Troubleshooting

<details>
<summary>Issue: <code>mcp.json</code> file opens repeatedly in my workspace</summary>

When using Developer Assist in **VS Code** with **GitHub Copilot**, there is a known issue where the `mcp.json` file automatically opens in your workspace each time you call the Checkmarx MCP.

**Solution:** Go to the **MCP** settings in VS Code, and under **Autostart** select **never**.

![MCP Autostart setting](../.gitbook/assets/img-e18f8a53315e7a57d743c3a2a53a1ebc.png)

{% hint style="warning" %}
Once this workaround is implemented, the Checkmarx MCP will no longer start automatically when you restart VS Code. You will need to start the MCP manually each restart:

1. Click **View** > **Command Palette** and enter **MCP:List Servers**.
2. Select **Checkmarx**.
3. Click **Start Server**.
{% endhint %}

</details>
