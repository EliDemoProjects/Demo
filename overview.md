---
description: Context-aware security for IntelliJ IDEA and other JetBrains IDEs
---

# Checkmarx Developer Assist - JetBrains Plugin

{% hint style="warning" %}
The **Checkmarx Developer Assist** JetBrains plugin provides Developer Assist capabilities as a standalone experience. **Checkmarx One** customers with a Checkmarx One Assist license should use the [Checkmarx JetBrains Plugin](https://checkmarx.com), where Developer Assist is included as part of the Checkmarx One platform. The **Checkmarx Developer Assist** and **Checkmarx** JetBrains plugins are mutually exclusive — ensure the Checkmarx plugin is uninstalled before installing Developer Assist.
{% endhint %}

## Overview

Checkmarx Developer Assist delivers context-aware security guidance directly within your IDE, helping prevent vulnerabilities before they reach the pipeline. As developers write or refine AI-generated and existing code, it provides real-time detection, remediation, and actionable insights — ensuring security is built in from the start.

Checkmarx Developer Assist comprises two main elements:

**Realtime Scanning** — Identify vulnerabilities in realtime during IDE development of both human-generated and AI-generated code. Scanners run in the background whenever you edit a relevant file, identifying vulnerabilities, unmasked secrets, vulnerable/malicious container images, and open source packages. Results are marked as Problems highlighted in the code and annotated with identifying icons.

**Agentic-AI Remediation** — Initiate an Agentic-AI session to receive remediation suggestions. Checkmarx feeds all relevant info to the AI agent, which accesses our Model Context Protocol (MCP) server to gather data from our proprietary databases and customized AI models. The AI assistant generates remediated code for your project. You can accept suggested changes or chat with the AI agent to learn more and fine-tune the remediation.

To help you focus on actionable risks, you can mark risks as **Ignored** so they no longer appear in your IDE. You can **Revive** any risk at any time to resume showing it.

---

## About Model Context Protocol (MCP) Server

The **Checkmarx MCP Server** is a secure gateway that bridges AI-powered development assistants with the Checkmarx security platform. It defines the tools and APIs that allow AI agents to interact safely with Checkmarx's cloud services directly from within the IDE.

Once the developer successfully authenticates in the IDE, the MCP Service is automatically installed. It can also be installed manually if required.

### What is MCP?

**Model Context Protocol (MCP)** is an emerging open standard that enables communication between AI agents and external systems in a structured, secure, and context-aware way. By adopting MCP, Checkmarx ensures that any IDE-integrated AI assistant can securely access Checkmarx engines and services — including SAST, SCA, IaC, and API Security — through a unified interface.

### Why Checkmarx Chose MCP

- **Interoperability:** MCP is vendor-neutral and supported by a growing ecosystem of AI tools.
- **Security and Governance:** MCP enforces strict access control and contextual awareness.
- **Scalability:** The protocol supports multi-agent environments across complex enterprise setups.
- **Future-readiness:** As new IDEs and AI tools adopt MCP, Checkmarx can integrate without changing the underlying architecture.

### How it Works

{% stepper %}
{% step %}
### Authenticate

Authenticates the developer's IDE session with Checkmarx.
{% endstep %}

{% step %}
### Expose capabilities

Exposes the available Checkmarx tools as AI-accessible functions.
{% endstep %}

{% step %}
### Enable AI-driven fixes

Allows the AI assistant to invoke these tools securely, analyze code, and propose context-aware fixes directly in the IDE.
{% endstep %}
{% endstepper %}

---

## Developer Assist Data Security FAQ

<details>
<summary>Does realtime scanning send sensitive data to the cloud for analysis?</summary>

No. All analysis is performed locally within the IDE. The only information sent to the Checkmarx Cloud is minimal, non-sensitive metadata:

- OSS — Package name and version
- Containers — Image name and tag

No source code or sensitive data is sent.

</details>

<details>
<summary>Is sensitive data sent to the MCP when I click "Fix with Developer Assist"?</summary>

No. When you click **Fix with Developer Assist**, the plugin instructs the AI agent to communicate with the MCP server and share only a unique identifier for the specific vulnerability instance:

- OSS — Package name and version
- Containers — Image name and tag
- IaC — Rule or policy ID and relevant resource attributes
- Secret Detection — Secret type
- ASCA — Vulnerability query ID

No source code or sensitive data is sent.

</details>

<details>
<summary>Is any customer data stored in the MCP or used to train AI models?</summary>

No. The entire process is done in real time so that no data is stored in the MCP. We do not use any customer data to train AI models. We do maintain a log of system events for operational purposes.

</details>

---

## Realtime Scanning

Realtime scans run automatically as you work in your IDE. Scan triggers include:

- When you open the workspace, the SCA scanner scans manifest files.
- When you open any artifact supported by realtime scanners.
- When you edit any supported artifact.
- When you save a supported file to an external location.
- When you use an AI assistant to make changes to a supported file.

### ASCA — AI Secure Coding Assistant Realtime Scanner

The ASCA is a lightweight source code scanner that identifies secure coding best practice violations. It runs locally in the background and returns results within milliseconds.

{% hint style="info" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Supported Languages:** Java, JavaScript (Node.js), C#, Go, and Python.

### IaC Realtime Scanner

The IaC Realtime scanner (based on the [KICS](https://docs.kics.io/latest/about/) open source project) examines infrastructure configuration definitions and scripts. A scan runs automatically whenever you edit a [supported infrastructure file type](https://docs.kics.io/latest/platforms/).

**Prerequisites:** A supported container engine (e.g., Docker, Podman) must be installed and running.

### Open Source Realtime Scanner (OSS-Realtime)

Analyzes manifest files and quickly identifies risks in open source dependencies, including vulnerable and malicious packages.

**Supported manifest files:** `csproj`, `directory.packages.props`, `packages.config`, `pom.xml`, `package.json`, `requirements.txt`, `go.mod`.

### Containers Realtime Scanner

Analyzes container image files and identifies risks from vulnerable or malicious packages in container images.

**Supported file types:** Dockerfile, DockerCompose, Helm chart (limited support).

### Secret Detection Realtime Scanner

Identifies sensitive credentials exposed in your code. Checkmarx identifies more than 210 different types of secrets including login credentials, access tokens, encryption keys, API keys, SSH keys, and webhook URLs.

---

## Agentic-AI Remediation

When you initiate remediation, a session is opened with GitHub Copilot Chat. Checkmarx gathers all relevant data about the risk and submits it to the AI assistant. The AI assistant sends a request to our MCP server, which applies the relevant tools and returns suggested remediation steps.

### Remediating Vulnerable or Malicious Images and Packages

The **Safe Refactor** feature searches your entire project for additional usage of a package and determines where and how code needs to be refactored to accommodate the update.

<details>
<summary>Remediation Logic — Vulnerable Packages</summary>

| Case | Response |
|------|----------|
| Package has a non-vulnerable version | Suggest the secure version; help fix breaking changes |
| No fully non-vulnerable version, but more secure version exists + Checkmarx has alternatives | Suggest most secure version + list alternatives |
| No non-vulnerable version + Checkmarx has alternatives | List alternative packages |
| No fully non-vulnerable version, but more secure version exists + no alternatives | Suggest most secure version + offer web search |
| No non-vulnerable or more secure version + no alternatives | Offer web search |

</details>

<details>
<summary>Remediation Logic — Malicious Packages</summary>

| Case | Response |
|------|----------|
| Package has a non-vulnerable and non-malicious version | Suggest the secure version; help fix breaking changes |
| Package has a non-malicious but vulnerable version | Suggest most secure version + list alternatives |
| No non-malicious version + Checkmarx has alternatives | List alternative packages |
| No non-malicious version + no alternatives | Offer web search |

</details>

### Remediating Exposed Secrets

Remediation removes the hard-coded secret from the code and replaces it with an Environment Variable for secure storage.

### Remediating ASCA and IaC Vulnerabilities

Remediation sends a customized prompt with all relevant vulnerability data to your IDE's AI assistant (Copilot). The AI assistant provides a remediated snippet.
