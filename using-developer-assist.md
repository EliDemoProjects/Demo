# Checkmarx Developer Assist – JetBrains Plugin

The Checkmarx Developer Assist JetBrains Plugin provides Developer Assist capabilities as a standalone experience within JetBrains IDEs.

{% hint style="warning" %}
**Checkmarx One** customers with a Checkmarx One Assist license should use the [Checkmarx JetBrains Plugin](https://checkmarx.com), where Developer Assist is included as part of the Checkmarx One platform. The **Checkmarx Developer Assist** and **Checkmarx** JetBrains plugins are mutually exclusive. To use the Checkmarx Developer Assist plugin, ensure that the Checkmarx plugin is uninstalled before installation.
{% endhint %}

## Key Capabilities

**Realtime Scanning** identifies vulnerabilities as you write or edit code — covering both human-generated and AI-generated code. The scanners run in the background whenever you open or edit a relevant file and flag the following risk types:

- Code vulnerabilities (SAST/ASCA)
- Unmasked secrets
- Vulnerable or malicious open source packages (SCA)
- Vulnerable or malicious container images
- Infrastructure-as-Code (IaC) misconfigurations

Results are marked as Problems, highlighted in the code with a squiggly underline, and annotated in the margin with an icon that indicates the risk type.

**Agentic-AI Remediation** lets you initiate an AI session to receive remediation suggestions. Checkmarx feeds all relevant information to the AI agent, which accesses the Checkmarx MCP server to gather data from proprietary databases and customized AI models. The AI assistant then uses this data to generate remediated code. You can accept the suggested changes or chat with the agent to learn more about the vulnerability and fine-tune the suggestion.

## In This Section

- [Installation and Initial Setup](installation-and-initial-setup.md)
- [Using Developer Assist for Detection and Remediation](using-developer-assist.md)
- [Changelog](changelog.md)
