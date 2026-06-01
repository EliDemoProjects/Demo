# Checkmarx Developer Assist JetBrains Plugin - Changelog

The following table lists of improvements and bug fixes have been implemented for the Checkmarx Developer Assist JetBrains Plugin with the relevant version release.

{% hint style="info" icon="pencil" %}
See full documentation of this plugin [here](README.md).
{% endhint %}

{% hint style="info" %}
As of May 31, 2026, Dev Assist remediation can be triggered via natural language chat in your AI Assistant. For more information, see [Remediation Via Chat](../vs-code-extension/using-developer-assist-for-detection-and-remediation.md).
{% endhint %}

| **Plugin Version** | **Release Date** | **CLI Version** | **Improvements** | **Bug Fixes** |
| --- | --- | --- | --- | --- |
| [1.0.2](https://github.com/Checkmarx/ast-jetbrains-plugin/releases/tag/2.3.6) | Apr 14, 2026 | [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) | Changed the behavior so that when connection to the Checkmarx MCP is not available, the remediation agent seamlessly offers remediation for all types of risks based on the IDE's LLM. When this occurs, we provide a notification indicating that the recommendations are not based on Checkmarx's specialized models. | |
| [1.0.1](https://github.com/Checkmarx/ast-jetbrains-plugin/releases/tag/2.3.5) | Apr 9, 2026 | [2.3.45](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.45) | General improvements and bug fixes | |
| [1.0.0](https://github.com/Checkmarx/ast-jetbrains-plugin/releases) | Mar 2, 2026 | [2.3.45](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.45) | **Initial release of the plugin**. This new tool empowers developers to identify risks in their code in realtime and harness the power of AI to remediate the risks on the spot.<br><br>**Checkmarx Developer Assist** comprises two main elements:<br><br>• **Realtime Scanning -** Identify vulnerabilities in realtime during IDE development of both human-generated and AI-generated code. Our super-fast scanners run in the background whenever you open or edit a relevant file. Our scanners identify vulnerabilities and unmasked secrets in your code. We also identify vulnerable or malicious container images and open source packages used in your project. Results are marked as Problems which are highlighted in the code and annotated with identifying icons.<br>• **Agentic-AI Remediation** – Initiate an Agentic-AI session to receive remediation suggestions. Checkmarx feeds all relevant info to the AI agent which accesses our MCP server to gather data from our proprietary databases and customized AI models. The AI assistant then uses this data to generate remediated code for your project. You can accept the suggested changes or you can chat with the AI agent to learn more about the vulnerability and fine-tune the remediation suggestion. | |
