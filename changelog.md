---
description: Version history for the Checkmarx Developer Assist JetBrains Plugin
---

# JetBrains Plugin — Changelog

{% hint style="info" %}
See full documentation of this plugin [here](overview.md).
{% endhint %}

{% hint style="info" %}
As of May 31, 2026, Dev Assist remediation can be triggered via natural language chat in your AI Assistant. For more information, see [Remediation via Chat](using-developer-assist.md#remediation-via-chat).
{% endhint %}

{% updates format="full" %}

{% update date="2026-04-14" %}
# Version 1.0.2

CLI: [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) — [Plugin release](https://github.com/Checkmarx/ast-jetbrains-plugin/releases/tag/2.3.6)

Changed the behavior so that when connection to the Checkmarx MCP is not available, the remediation agent seamlessly offers remediation for all types of risks based on the IDE's LLM. A notification is displayed indicating that the recommendations are not based on Checkmarx's specialized models.
{% endupdate %}

{% update date="2026-04-09" %}
# Version 1.0.1

CLI: [2.3.45](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.45) — [Plugin release](https://github.com/Checkmarx/ast-jetbrains-plugin/releases/tag/2.3.5)

General improvements and bug fixes.
{% endupdate %}

{% update date="2026-03-02" %}
# Version 1.0.0 — Initial Release

CLI: [2.3.45](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.45) — [Plugin release](https://github.com/Checkmarx/ast-jetbrains-plugin/releases)

Initial release of the plugin. This new tool empowers developers to identify risks in their code in realtime and harness the power of AI to remediate the risks on the spot.

**Realtime Scanning** — Identify vulnerabilities in realtime during IDE development. Scanners run in the background whenever you open or edit a relevant file, identifying vulnerabilities, exposed secrets, vulnerable/malicious container images, and open source packages.

**Agentic-AI Remediation** — Initiate an Agentic-AI session to receive remediation suggestions powered by the Checkmarx MCP server.
{% endupdate %}

{% endupdates %}
