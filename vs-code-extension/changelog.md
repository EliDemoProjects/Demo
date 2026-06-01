---
description: Improvements and bug fixes for the Checkmarx Developer Assist VS Code plugin.
---

# Checkmarx Developer Assist VS Code Extension - Changelog

The following table lists of improvements and bug fixes have been implemented for the Checkmarx Developer Assist VS Code plugin with the relevant version release.

{% hint style="info" icon="pencil" %}
See full documentation of this plugin [here](README.md).
{% endhint %}

{% hint style="info" %}
As of May 31, 2026, Dev Assist remediation can be triggered via natural language chat in your AI Assistant. For more information, see [Remediation Via Chat](/document/preview/405960#UUID-dc8b3418-3999-ee6b-e5e0-4ea1247d34b4_section-id23559746076479).
{% endhint %}

| Plugin Version | Release Date | CLI Version | Improvements | Bug Fixes |
| --- | --- | --- | --- | --- |
| [1.18.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.65.0) | Apr 22, 2026 | [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) | General improvements and bug fixes | |
| [1.15.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.62.0) | Apr 13, 2026 | [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) | Changed the behavior so that when connection to the Checkmarx MCP is not available, the remediation agent seamlessly offers remediation for all types of risks based on the IDE's LLM. When this occurs, we provide a notification indicating that the recommendations are not based on Checkmarx's specialized models. | |
| [1.14.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.61.0) | Apr 2, 2026 | [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) | Added the option to use **Claude** for Developer Assist AI remediation. This is configured in the Checkmarx Developer Assist settings. **Tip:** When this extension is used in an IDE that has a native AI Assistant (Windsurf, Cursor or Kiro), there is an option to **Prefer Native AI Assistant**. This setting overrides the selected AI model. | |
| [1.13.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.60.0) | Mar 25, 2026 | [2.3.46](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.46) | General improvements and bug fixes | |
| [1.6.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.52.0) | Mar 9, 2026 | [2.3.46](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.46) | General improvements and bug fixes | |
| [1.4.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.50.0) | Mar 4, 2026 | [2.3.46](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.46) | **Updated Login Flow for Checkmarx Developer Assist Authentication.** Authentication is no longer managed through the IDE **Settings** page. Instead, a dedicated **Checkmarx Developer Assist Authentication** side panel has been introduced to handle authentication. | |
| [1.1.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/DevAssist-v1.1.0) | Feb 10 2026 | | | **Initial release of the plugin.** This new tool empowers developers to identify risks in their code in realtime and harness the power of AI to remediate the risks on the spot. **Checkmarx Developer Assist** comprises two main elements: **Realtime Scanning -** Identify vulnerabilities in realtime during IDE development of both human-generated and AI-generated code. Our super-fast scanners run in the background whenever you open or edit a relevant file. **Agentic-AI Remediation** – Initiate an Agentic-AI session to receive remediation suggestions. Checkmarx feeds all relevant info to the AI agent which accesses our MCP server to gather data from our proprietary databases and customized AI models. |
