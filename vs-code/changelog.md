# Checkmarx Developer Assist VS Code Extension – Changelog

The following table lists improvements and bug fixes implemented for the Checkmarx Developer Assist VS Code extension with the relevant version release.

{% hint style="info" %}
See full documentation of this extension [here](README.md).
{% endhint %}

{% hint style="info" %}
As of May 31, 2026, Developer Assist remediation can be triggered via natural language chat in your AI Assistant. For more information, see [Remediation via Chat](using-developer-assist.md#remediation-via-chat).
{% endhint %}

| Plugin Version | Release Date | CLI Version | Improvements | Bug Fixes |
| -------------- | ------------ | ----------- | ------------ | --------- |
| [1.18.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.65.0) | Apr 22, 2026 | [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) | General improvements and bug fixes | |
| [1.15.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.62.0) | Apr 13, 2026 | [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) | Changed the behavior so that when connection to the Checkmarx MCP is not available, the remediation agent seamlessly offers remediation for all types of risks based on the IDE's LLM. When this occurs, a notification is provided indicating that the recommendations are not based on Checkmarx's specialized models. | |
| [1.14.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.61.0) | Apr 2, 2026 | [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) | Added the option to use **Claude** for Developer Assist AI remediation. This is configured in the Checkmarx Developer Assist settings. When this extension is used in an IDE that has a native AI Assistant (Windsurf, Cursor, or Kiro), there is an option to **Prefer Native AI Assistant**. This setting overrides the selected AI model. | |
| [1.13.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.60.0) | Mar 25, 2026 | [2.3.46](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.46) | General improvements and bug fixes | |
| [1.6.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.52.0) | Mar 9, 2026 | [2.3.46](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.46) | General improvements and bug fixes | |
| [1.4.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.50.0) | Mar 4, 2026 | [2.3.46](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.46) | **Updated Login Flow for Checkmarx Developer Assist Authentication.** Authentication is no longer managed through the IDE Settings page. Instead, a dedicated **Checkmarx Developer Assist Authentication** side panel has been introduced. | |
| [1.1.0](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/DevAssist-v1.1.0) | Feb 10, 2026 | | **Initial release of the plugin.** Includes Realtime Scanning and Agentic-AI Remediation. | |
