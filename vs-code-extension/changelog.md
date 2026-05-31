# Checkmarx Developer Assist JetBrains Plugin – Changelog

The following table lists improvements and bug fixes implemented for the Checkmarx Developer Assist JetBrains Plugin with the relevant version release.

{% hint style="info" %}
See full documentation of this plugin [here](README.md).
{% endhint %}

{% hint style="info" %}
As of May 31, 2026, Developer Assist remediation can be triggered via natural language chat in your AI Assistant. For more information, see [Remediation via Chat](using-developer-assist.md#remediation-via-chat).
{% endhint %}

| Plugin Version | Release Date | CLI Version | Improvements | Bug Fixes |
| -------------- | ------------ | ----------- | ------------ | --------- |
| [1.0.2](https://github.com/Checkmarx/ast-jetbrains-plugin/releases/tag/2.3.6) | Apr 14, 2026 | [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) | Changed the behavior so that when connection to the Checkmarx MCP is not available, the remediation agent seamlessly offers remediation for all types of risks based on the IDE's LLM. When this occurs, a notification is provided indicating that the recommendations are not based on Checkmarx's specialized models. | |
| [1.0.1](https://github.com/Checkmarx/ast-jetbrains-plugin/releases/tag/2.3.5) | Apr 9, 2026 | [2.3.45](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.45) | General improvements and bug fixes | |
| [1.0.0](https://github.com/Checkmarx/ast-jetbrains-plugin/releases) | Mar 2, 2026 | [2.3.45](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.45) | **Initial release of the plugin.** Includes Realtime Scanning and Agentic-AI Remediation. | |
