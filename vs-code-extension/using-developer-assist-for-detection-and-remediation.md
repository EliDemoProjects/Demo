# Using Developer Assist for Detection and Remediation

## AI Remediation

{% embed url="https://player.vimeo.com/video/1160134485" %}

### How to Remediate Risks Using AI

The following procedure explains how to remediate risks by clicking on the Fix button for a particular risk. Alternatively, you can request remediation via chat with your AI Agent, as described below.

1. When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem**, which is marked in the code with a squiggly underline and annotated in the margin with an icon that indicates the type of risk.

   ![](../.gitbook/assets/img-8b30ebc58d203cf69432bb233991474a.png)
2. Hover over the vulnerable line of code.

   The Checkmarx dialog opens.
3. Click on **Fix with Checkmarx Developer Assist**.

   ![](../.gitbook/assets/img-13fe029e47946a4efb78d53865fb74b6.png)

   A Copilot session opens in the side panel and all relevant info is sent for analysis.

   {% hint style="info" icon="pencil" %}
   Depending on your IDE configuration, you may need to click **Continue** several times in order to complete the process.
   {% endhint %}
4. Copilot automatically makes the necessary changes in the code in order to remediate the risk.
   - If you approve the change, click **Accept**. The change is made and the code is rescanned to verify that the risk is no longer present.
   - If you want to improve on the suggestion, click **Undo**. You can then chat with Copilot to determine the best way of remediating the code.

#### Remediation via Chat

You can submit a request for CxOne Dev Assist remediation via natural language chat with your AI Agent. Just say that you want to fix a security risk and indicate which risk or risks you want to fix. Your AI will automatically route the request to the Checkmarx MCP and send all relevant data for analysis in order to generate the suggested remediation. The following are some examples of valid requests:

- "Fix the vulnerability in line 26"
- "Fix all critical vulnerabilities"
- "Fix all SQL Injection risks"
- "Remediate all vulnerable packages"
- "Correct all critical issues in my JavaFile.java"

##### Things to Know About Dev Assist Chat

- No need to mention "Checkmarx" explicitly; once Dev Assist is installed and running all remediation requests are handled via Checkmarx MCP
- Support for multi-language prompts
- Effective in single message context. Improved accuracy in context of an existing thread or finding.
- By default, requests are interpreted in the context of the current open file (e.g., line 26 of the open file). You can specify a different file in your workspace.

### How to Understand Risks Using AI

1. When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem**, which is marked in the code with a squiggly underline and annotated in the margin with an icon that indicates the type of risk.

   ![](../.gitbook/assets/img-8b30ebc58d203cf69432bb233991474a.png)
2. Hover over the vulnerable line of code.

   The Checkmarx dialog opens.
3. Click on **View details**.

   ![](../.gitbook/assets/img-ea6756f4b9eaa29b4671b352492a359a.png)

   A Copilot session opens in the side panel and all relevant info is sent for analysis.

   {% hint style="info" icon="pencil" %}
   Depending on your IDE configuration, you may need to click **Continue** several times in order to complete the process.
   {% endhint %}
4. Copilot explains the precise nature of the risk in the context of your code. You can chat with Copilot to ask for further clarification.

### Ignoring Risks

In order to help you focus on actionable risks, Checkmarx Dev Assist enables marking risks as **Ignore**, so that the risks will no longer be shown in your IDE. You can **Revive** a risk at any time to resume showing that risk. This can be applied to a specific instance of a risk or it can be applied to all instances of that risk in your project. You can revive the risk at any time to resume showing risks for that package.

{% hint style="info" icon="pencil" %}
For risks identified in open source packages, a risk instance refers to the entire package that the vulnerability is associated with.
{% endhint %}

**To Ignore a risk**

1. When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem**, which is marked in the code with a squiggly underline and annotated in the margin with an icon that indicates the type of risk.

   ![](../.gitbook/assets/img-8b30ebc58d203cf69432bb233991474a.png)
2. Hover over the vulnerable line of code.

   The Checkmarx dialog opens.

   ![](../.gitbook/assets/img-999c6f8e74bccdfdd57a2c20eb26bec9.png)
3. To ignore the risk in this particular instance, click on **Ignore this vulnerability**.
4. To ignore all instances of the risk, click on **Ignore all of this type**.

**To revive a package:**

1. Click on the **Ignore** icon in the bottom bar.

   ![](../.gitbook/assets/img-ebaacd1e8161e192a6584a7f20c2d22b.png)
2. The **Ignored Vulnerabilities** tab opens.

   ![](../.gitbook/assets/img-059c35009247a914982566066c4d3be5.png)
3. For the desired vulnerability click on the **Revive** button.

   {% hint style="info" icon="pencil" %}
   This can also be done as a bulk action for all selected items.
   {% endhint %}

## Troubleshooting

<details>

<summary>Issue: <code>mcp.json</code> file opens repeatedly in my workspace</summary>

When using Developer Assist in **VS Code** with **GitHub Copilot**, there is a known issue that each time that you call the Checkmarx MCP, the mcp.json file automatically opens in your workspace. The unnecessary clutter can be an annoyance.

**Solution:** The workaround for this issue is to go to the **MCP** settings in VS Code, and under **Autostart** select **never**.

![](../.gitbook/assets/img-e18f8a53315e7a57d743c3a2a53a1ebc.png)

{% hint style="warning" %}
Once this workaround is implemented, the Checkmarx MCP will no longer start automatically each time that you restart VS Code. Whenever you restart VS Code you will need to start the MCP manually, as follows:

1. Click **View** > **Command Palette** and enter **MCP:List Servers**.
2. In the MCP servers list, select **Checkmarx**.
3. Click on **Start Server**.
{% endhint %}

</details>
