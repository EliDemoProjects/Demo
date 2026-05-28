---
description: Version history for the Checkmarx Developer Assist JetBrains Plugin
---

# JetBrains Plugin — Changelog

The following table lists improvements and bug fixes implemented for the Checkmarx Developer Assist JetBrains Plugin with the relevant version release.

{% hint style="info" %}
See full documentation of this plugin [here](overview.md).
{% endhint %}

{% hint style="info" %}
As of May 31, 2026, Dev Assist remediation can be triggered via natural language chat in your AI Assistant. For more information, see [Remediation via Chat](using-developer-assist.md#remediation-via-chat).
{% endhint %}

{% updates %}

{% update date="Apr 14, 2026" %}
**Version 1.0.2** — CLI 2.3.48

Changed the behavior so that when connection to the Checkmarx MCP is not available, the remediation agent seamlessly offers remediation for all types of risks based on the IDE's LLM. A notification is displayed indicating that the recommendations are not based on Checkmarx's specialized models.

[Release notes on GitHub](https://github.com/Checkmarx/ast-jetbrains-plugin/releases/tag/2.3.6)
{% endupdate %}

{% update date="Apr 9, 2026" %}
**Version 1.0.1** — CLI 2.3.45

General improvements and bug fixes.

[Release notes on GitHub](https://github.com/Checkmarx/ast-jetbrains-plugin/releases/tag/2.3.5)
{% endupdate %}

{% update date="Mar 2, 2026" %}
**Version 1.0.0** — CLI 2.3.45 — Initial release

**Initial release of the plugin.** This new tool empowers developers to identify risks in their code in realtime and harness the power of AI to remediate the risks on the spot.

Checkmarx Developer Assist comprises two main elements:

**Realtime Scanning** — Identify vulnerabilities in realtime during IDE development. Scanners run in the background whenever you open or edit a relevant file, identifying vulnerabilities, exposed secrets, vulnerable/malicious container images, and open source packages.

**Agentic-AI Remediation** — Initiate an Agentic-AI session to receive remediation suggestions powered by the Checkmarx MCP server.

[Release notes on GitHub](https://github.com/Checkmarx/ast-jetbrains-plugin/releases)
{% endupdate %}

{% endupdates %}
