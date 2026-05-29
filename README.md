---
description: Context-aware security guidance directly within your IDE
metaLinks:
  alternates:
    - https://app.gitbook.com/s/Upiv3KOTza7CaZSrBSOL/
---

# Overview

Checkmarx Developer Assist delivers context-aware security guidance directly within your IDE, helping prevent vulnerabilities before they reach the pipeline. As developers write or refine AI-generated and existing code, it provides real-time detection, remediation, and actionable insights — ensuring security is built in from the start.

## Available Plugins

{% hint style="info" %}
**Checkmarx One customers** with a Checkmarx One Assist license should use the dedicated Checkmarx IDE extension for their platform (VS Code or JetBrains), where Developer Assist is included as part of Checkmarx One. The **Checkmarx Developer Assist** and **Checkmarx** extensions are mutually exclusive.
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>VS Code Extension</strong></td><td>For VS Code and related IDEs: Cursor, Windsurf, and Kiro</td><td><a href="vscode/overview.md">overview.md</a></td></tr><tr><td><strong>JetBrains Plugin</strong></td><td>For IntelliJ IDEA and other JetBrains IDEs</td><td><a href="jetbrains/overview.md">overview.md</a></td></tr></tbody></table>

## Key Capabilities

**Realtime Scanning** — Identify vulnerabilities as you code. Scanners run in the background whenever you edit a relevant file, detecting vulnerabilities, exposed secrets, vulnerable open source packages, and container image risks.

**Agentic-AI Remediation** — Initiate an Agentic-AI session to receive remediation suggestions. Checkmarx feeds all relevant info to the AI agent, which accesses our Model Context Protocol (MCP) server to gather data from proprietary databases and customized AI models.

**Ignore & Revive** — Mark risks as **Ignored** to remove noise and focus on what matters. Revive any risk at any time to resume showing it.
