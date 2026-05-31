# Overview

Checkmarx Developer Assist empowers developers to identify risks in their code in realtime and harness the power of AI to remediate those risks on the spot, directly within their IDE.

## Key Capabilities

**Realtime Scanning** identifies vulnerabilities as you write or edit code — covering both human-generated and AI-generated code. The scanners run in the background whenever you open or edit a relevant file and flag the following risk types:

* Code vulnerabilities (SAST/ASCA)
* Unmasked secrets
* Vulnerable or malicious open source packages (SCA)
* Vulnerable or malicious container images
* Infrastructure-as-Code (IaC) misconfigurations

Results are marked as Problems, highlighted in the code with a squiggly underline, and annotated in the margin with an icon that indicates the risk type.

**Agentic-AI Remediation** lets you initiate an AI session to receive remediation suggestions. Checkmarx feeds all relevant information to the AI agent, which accesses the Checkmarx MCP server to gather data from proprietary databases and customized AI models. The AI assistant then uses this data to generate remediated code. You can accept the suggested changes or chat with the agent to learn more about the vulnerability and fine-tune the suggestion.

## Supported IDEs

The VS Code extension supports the following IDEs:

* VS Code
* Cursor
* Windsurf
* Kiro

## In This Section

* [Installation and Initial Setup](vs-code/installation-and-initial-setup.md)
* [Using Developer Assist for Detection and Remediation](vs-code/using-developer-assist.md)
* [Tutorial Videos](vs-code/tutorial-videos.md)
* [Changelog](vs-code/changelog.md)
