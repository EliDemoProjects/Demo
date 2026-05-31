# Using Developer Assist for Detection and Remediation (JetBrains)

## AI Remediation

### How to Remediate Risks Using AI

The following procedure explains how to remediate risks by clicking the Fix button for a particular risk. Alternatively, you can request remediation via chat with your AI Agent, as described below.

1. Open a project in IntelliJ IDEA.
2. When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem**, marked in the code with a squiggly underline and annotated in the margin with an icon indicating the risk type.

   ![](../.gitbook/assets/img-4f3f94be7ca1c8f0ce2b8faccbe8d496.png)

3. Hover over the vulnerable line of code. The Checkmarx dialog opens.

   ![](../.gitbook/assets/img-d896b154664bf2bfe2fdd4594c952435.png)

4. Click **Fix with Checkmarx Developer Assist**.

   ![](../.gitbook/assets/img-c44e70f4834374a710812e32c758bdbb.png)

   A Copilot session opens in the side panel and all relevant information is sent for analysis.

   {% hint style="info" %}
   Depending on your IDE configuration, you may need to click **Continue** several times to complete the process.
   {% endhint %}

5. Copilot automatically makes the necessary changes in the code to remediate the risk.

   ![](../.gitbook/assets/img-d2088e3d0874c3b51abeafbbd7f04a71.png)

   - If you approve the changes, click **Accept All**.
   - If you do not want to implement the suggestion, click **Discard All**.
   - You can also chat with Copilot to improve upon the suggestion.

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

### The Checkmarx Developer Assist Findings Window

![](../.gitbook/assets/img-7c4a2407cf99756d42fbe12660d6f9ce.png)

The **Checkmarx Developer Assist Findings Window** provides a centralized view of all detected issues within a project. It displays vulnerabilities per file along with the count of issues grouped by severity and file location. You can navigate directly to the exact line in the editor with a single click, and the window supports filtering and sorting to streamline issue review.

To open the Findings Window, click the Checkmarx icon in the left navigation bar and select the **Checkmarx Developer Assist Findings** tab.

### How to Understand Risks Using AI

1. When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem**, marked in the code with a squiggly underline and annotated in the margin with an icon indicating the risk type.

   ![](../.gitbook/assets/img-4f3f94be7ca1c8f0ce2b8faccbe8d496.png)

2. Hover over the vulnerable line of code. The Checkmarx dialog opens.

   ![](../.gitbook/assets/img-d896b154664bf2bfe2fdd4594c952435.png)

3. Click **View details**.

   ![](../.gitbook/assets/img-638b072f4e89de112ca36a27fc9d63e1.png)

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

   ![](../.gitbook/assets/img-4f3f94be7ca1c8f0ce2b8faccbe8d496.png)

2. Hover over the vulnerable line of code. The Checkmarx dialog opens.

   ![](../.gitbook/assets/img-d896b154664bf2bfe2fdd4594c952435.png)

3. To ignore the risk in this particular instance, click **Ignore this vulnerability**.
4. To ignore all instances of the risk, click **Ignore all of this type**.

**To revive a risk:**

{% hint style="info" %}
This can also be done as a bulk action for all selected items.
{% endhint %}

1. Click the **Ignored Findings** tab in the Checkmarx window. The Ignored Findings tab opens.

   ![](../.gitbook/assets/img-02475afec7b97d2db724130403743d6d.png)

2. For the desired vulnerability, click the **Revive** button.
