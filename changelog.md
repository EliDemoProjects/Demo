---
description: Version history for the Checkmarx Developer Assist VS Code Extension
---

# VS Code Extension — Changelog

{% hint style="info" %}
See full documentation of this plugin [here](overview.md).
{% endhint %}

{% hint style="info" %}
As of May 31, 2026, Dev Assist remediation can be triggered via natural language chat in your AI Assistant. For more information, see [Remediation via Chat](using-developer-assist.md#remediation-via-chat).
{% endhint %}

{% updates format="full" %}

{% update date="2026-04-22" %}
# Version 1.18.0

CLI: [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) — [Plugin release](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.65.0)

General improvements and bug fixes.
{% endupdate %}

{% update date="2026-04-13" %}
# Version 1.15.0

CLI: [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) — [Plugin release](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.62.0)

Changed the behavior so that when connection to the Checkmarx MCP is not available, the remediation agent seamlessly offers remediation for all types of risks based on the IDE's LLM. A notification is displayed indicating that the recommendations are not based on Checkmarx's specialized models.
{% endupdate %}

{% update date="2026-04-02" %}
# Version 1.14.0

CLI: [2.3.48](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.48) — [Plugin release](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.61.0)

Added the option to use **Claude** for Developer Assist AI remediation, configured in the Checkmarx Developer Assist settings.

{% hint style="info" %}
When this extension is used in an IDE with a native AI Assistant (Windsurf, Cursor, or Kiro), there is an option to **Prefer Native AI Assistant**. This setting overrides the selected AI model.
{% endhint %}
{% endupdate %}

{% update date="2026-03-25" %}
# Version 1.13.0

CLI: [2.3.46](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.46) — [Plugin release](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.60.0)

General improvements and bug fixes.
{% endupdate %}

{% update date="2026-03-09" %}
# Version 1.6.0

CLI: [2.3.46](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.46) — [Plugin release](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.52.0)

General improvements and bug fixes.
{% endupdate %}

{% update date="2026-03-04" %}
# Version 1.4.0

CLI: [2.3.46](https://github.com/Checkmarx/ast-cli/releases/tag/2.3.46) — [Plugin release](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/v2.50.0)

**Updated Login Flow for Checkmarx Developer Assist Authentication.** Authentication is no longer managed through the IDE **Settings** page. A dedicated **Checkmarx Developer Assist Authentication** side panel has been introduced to handle authentication.
{% endupdate %}

{% update date="2026-02-10" %}
# Version 1.1.0 — Initial Release

[Plugin release](https://github.com/Checkmarx/ast-vscode-extension/releases/tag/DevAssist-v1.1.0)

Initial release of the plugin. This new tool empowers developers to identify risks in their code in realtime and harness the power of AI to remediate the risks on the spot.

**Realtime Scanning** — Identify vulnerabilities in realtime during IDE development. Scanners run in the background whenever you open or edit a relevant file, identifying vulnerabilities, exposed secrets, vulnerable/malicious container images, and open source packages.

**Agentic-AI Remediation** — Initiate an Agentic-AI session to receive remediation suggestions powered by the Checkmarx MCP server.
{% endupdate %}

{% endupdates %}
