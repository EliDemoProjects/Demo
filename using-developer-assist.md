---
description: How to detect and remediate security risks using Checkmarx Developer Assist in JetBrains IDEs
---

# Using Developer Assist for Detection and Remediation (JetBrains)

## AI Remediation

### How to Remediate Risks Using AI

The following procedure explains how to remediate risks by clicking the Fix button. You can also request remediation via chat with your AI Agent.

{% stepper %}
{% step %}
### Open a project

Open a project in IntelliJ IDEA.
{% endstep %}

{% step %}
### Identify the risk

When Checkmarx realtime scanners identify a risk, it is flagged as a **Problem** — marked in the code with a squiggly underline and an icon in the margin.

![Risk flagged in JetBrains](../.gitbook/assets/img-4f3f94be7ca1c8f0ce2b8faccbe8d496.png)
{% endstep %}

{% step %}
### Open the dialog

Hover over the vulnerable line. The Checkmarx dialog opens.

![Checkmarx dialog in JetBrains](../.gitbook/assets/img-d896b154664bf2bfe2fdd4594c952435.png)
{% endstep %}

{% step %}
### Initiate remediation

Click **Fix with Checkmarx Developer Assist**.

![Fix with Developer Assist button](../.gitbook/assets/img-c44e70f4834374a710812e32c758bdbb.png)

A Copilot session opens in the side panel.

{% hint style="info" %}
Depending on your IDE configuration, you may need to click **Continue** several times to complete the process.
{% endhint %}
{% endstep %}

{% step %}
### Accept or refine

Copilot automatically makes the necessary code changes.

![Accept All or Discard All options](../.gitbook/assets/img-d2088e3d0874c3b51abeafbbd7f04a71.png)

- To approve: click **Accept All**.
- To reject: click **Discard All**.
- You can also chat with Copilot to improve upon the suggestion.
{% endstep %}
{% endstepper %}

### Remediation via Chat

You can submit a request for Dev Assist remediation via natural language chat with your AI Agent:

- "Fix the vulnerability in line 26"
- "Fix all critical vulnerabilities"
- "Fix all SQL Injection risks"
- "Remediate all vulnerable packages"
- "Correct all critical issues in my JavaFile.java"

**Things to know about Dev Assist Chat:**

- No need to mention "Checkmarx" explicitly — Dev Assist is integrated with all remediation requests.
- Multi-language prompts are supported.
- By default, requests are interpreted in the context of the current open file.

---

## The Checkmarx Developer Assist Findings Window

![Checkmarx Developer Assist Findings Window](../.gitbook/assets/img-7c4a2407cf99756d42fbe12660d6f9ce.png)

The **Checkmarx Developer Assist Findings Window** provides a centralized view of all detected issues within a project. It displays vulnerabilities per file along with the count of issues grouped by severity and file location. You can navigate directly to the exact line in the editor with a single click, and use filtering and sorting to streamline issue review.

To open the **Findings Window**, click on the Checkmarx icon in the left navigation bar and select the **Checkmarx Developer Assist Findings** tab.

---

## How to Understand Risks Using AI

{% stepper %}
{% step %}
### Identify the risk

When a risk is flagged as a **Problem**, hover over the vulnerable line. The Checkmarx dialog opens.
{% endstep %}

{% step %}
### View details

Click **View details**.

![View details button](../.gitbook/assets/img-638b072f4e89de112ca36a27fc9d63e1.png)

A Copilot session opens in the side panel.
{% endstep %}

{% step %}
### Chat for clarification

Copilot explains the precise nature of the risk in context. You can chat for further clarification.
{% endstep %}
{% endstepper %}

---

## Ignoring Risks

Checkmarx Developer Assist enables marking risks as **Ignored** so they no longer appear in your IDE. You can **Revive** a risk at any time. This can be applied to a specific instance or all instances of that risk.

{% hint style="info" %}
For risks identified in open source packages, a risk instance refers to the entire package associated with the vulnerability.
{% endhint %}

**To ignore a risk:**

{% stepper %}
{% step %}
### Hover over the vulnerability

Hover over the vulnerable line to open the Checkmarx dialog.
{% endstep %}

{% step %}
### Choose ignore scope

- Click **Ignore this vulnerability** to ignore this specific instance.
- Click **Ignore all of this type** to ignore all instances.
{% endstep %}
{% endstepper %}

**To revive a risk:**

{% hint style="info" %}
This can also be done as a bulk action for all selected items.
{% endhint %}

1. Click the **Ignored Findings** tab in the Checkmarx window.

   ![Ignored Findings tab](../.gitbook/assets/img-02475afec7b97d2db724130403743d6d.png)

2. For the desired vulnerability, click the **Revive** button.
