# Using Developer Assist for Detection and Remediation

## AI Remediation

{% embed url="https://player.vimeo.com/video/1160134485" %}

### How to Remediate Risks Using AI

The following procedure explains how to remediate risks by clicking the Fix button for a particular risk. Alternatively, you can request remediation via chat with your AI Agent, as described below.

1. When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem**, marked in the code with a squiggly underline and annotated in the margin with an icon indicating the risk type.

   ![](../.gitbook/assets/img-8b30ebc58d203cf69432bb233991474a.png)

2. Hover over the vulnerable line of code. The Checkmarx dialog opens.
3. Click **Fix with Checkmarx Developer Assist**.

   ![](../.gitbook/assets/img-13fe029e47946a4efb78d53865fb74b6.png)

   A Copilot session opens in the side panel and all relevant information is sent for analysis.

   {% hint style="info" %}
   Depending on your IDE configuration, you may need to click **Continue** several times to complete the process.
   {% endhint %}

4. Copilot automatically makes the necessary changes in the code to remediate the risk.

   - If you approve the change, click **Accept**. The change is made and the code is rescanned to verify that the risk is no longer present.
   - If you want to improve on the suggestion, click **Undo**. You can then chat with Copilot to determine the best way of remediating the code.

#### Remediation via Chat

You can submit a request for Developer Assist remediation via natural language chat with your AI Agent. Just say that you want to fix a security risk and indicate which risk or risks to fix. Your AI will automatically route the request to the Checkmarx MCP and send all relevant data for analysis to generate the suggested remediation.

Some examples of valid requests:

- "Fix the vulnerability in line 26"
- "Fix all critical vulnerabilities"
- "Fix all SQL Injection risks"
- "Remediate all vulnerable packages"
- "Correct all critical issues in my JavaFile.java"

**Things to know about Dev Assist chat:**

- No need to mention "Checkmarx" explicitly; once Dev Assist is installed and running, all remediation requests are handled via the Checkmarx MCP.
- Multi-language prompts are supported.
- Effective in single-message context; improved accuracy in the context of an existing thread or finding.
- By default, requests are interpreted in the context of the current open file (e.g., line 26 of the open file). You can specify a different file in your workspace.

### How to Understand Risks Using AI

1. When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem**, marked in the code with a squiggly underline and annotated in the margin with an icon indicating the risk type.

   ![](../.gitbook/assets/img-8b30ebc58d203cf69432bb233991474a.png)

2. Hover over the vulnerable line of code. The Checkmarx dialog opens.
3. Click **View details**.

   ![](../.gitbook/assets/img-ea6756f4b9eaa29b4671b352492a359a.png)

   A Copilot session opens in the side panel and all relevant information is sent for analysis.

   {% hint style="info" %}
   Depending on your IDE configuration, you may need to click **Continue** several times to complete the process.
   {% endhint %}

4. Copilot explains the precise nature of the risk in the context of your code. You can chat with Copilot to ask for further clarification.

### Ignoring Risks

To help you focus on actionable risks, Checkmarx Developer Assist lets you mark risks as **Ignored** so they no longer appear in your IDE. You can **Revive** a risk at any time to resume showing it. This can be applied to a specific instance of a risk or to all instances of that risk in your project.

{% hint style="info" %}
For risks identified in open source packages, a risk instance refers to the entire package that the vulnerability is associated with.
{% endhint %}

**To ignore a risk:**

1. When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem**, marked in the code with a squiggly underline and annotated in the margin with an icon indicating the risk type.

   ![](../.gitbook/assets/img-8b30ebc58d203cf69432bb233991474a.png)

2. Hover over the vulnerable line of code. The Checkmarx dialog opens.

   ![](../.gitbook/assets/img-999c6f8e74bccdfdd57a2c20eb26bec9.png)

3. To ignore the risk in this particular instance, click **Ignore this vulnerability**.
4. To ignore all instances of the risk, click **Ignore all of this type**.

**To revive a risk:**

1. Click the **Ignore** icon in the bottom bar.

   ![](../.gitbook/assets/img-ebaacd1e8161e192a6584a7f20c2d22b.png)

2. The **Ignored Vulnerabilities** tab opens.

   ![](../.gitbook/assets/img-059c35009247a914982566066c4d3be5.png)

3. For the desired vulnerability, click the **Revive** button.

   {% hint style="info" %}
   This can also be done as a bulk action for all selected items.
   {% endhint %}

## Troubleshooting

<details>

<summary>Issue: <code>mcp.json</code> file opens repeatedly in my workspace</summary>

When using Developer Assist in VS Code with GitHub Copilot, there is a known issue where the `mcp.json` file automatically opens in your workspace each time the Checkmarx MCP is called.

**Solution:** Go to the **MCP** settings in VS Code, and under **Autostart** select **never**.

![](../.gitbook/assets/img-e18f8a53315e7a57d743c3a2a53a1ebc.png)

{% hint style="warning" %}
Once this workaround is implemented, the Checkmarx MCP will no longer start automatically when you restart VS Code. Whenever you restart VS Code you will need to start the MCP manually:

1. Click **View** > **Command Palette** and enter **MCP:List Servers**.
2. In the MCP servers list, select **Checkmarx**.
3. Click **Start Server**.
{% endhint %}

</details>
