# Checkmarx Developer Assist - JetBrains Plugin

{% hint style="warning" %}
The **Checkmarx Developer Assist** JetBrains plugin provides Developer Assist capabilities as a standalone experience. **Checkmarx One** customers with a Checkmarx One Assist license should use the [Checkmarx JetBrains Plugin](https://checkmarx.com), where Developer Assist is included as part of the Checkmarx One platform. The **Checkmarx Developer Assist** and **Checkmarx** JetBrains plugins are mutually exclusive. To use the Checkmarx Developer Assist plugin, ensure that the Checkmarx plugin is uninstalled before installation.
{% endhint %}

## Overview

Checkmarx Developer Assist delivers context-aware security guidance directly within your IDE, helping prevent vulnerabilities before they reach the pipeline. As developers write or refine AI-generated and existing code, it provides real-time detection, remediation, and actionable insights—ensuring security is built in from the start.

Checkmarx Developer Assist comprises two main elements:

- **Realtime Scanning -** Identify vulnerabilities in realtime during IDE development of both human-generated and AI-generated code. Our super-fast scanners run in the background whenever you edit a relevant file. Our scanners identify vulnerabilities and unmasked secrets in your code. We also identify vulnerable or malicious container images and open source packages used in your project. Results are marked as Problems which are highlighted in the code and annotated with identifying icons.
- **Agentic-AI Remediation** – Initiate an Agentic-AI session to receive remediation suggestions. Checkmarx feeds all relevant info to the AI agent which accesses our Model Context Protocol (MCP) server to gather data from our proprietary databases and customized AI models. The AI assistant then uses this data to generate remediated code for your project. You can accept the suggested changes or you can chat with the AI agent to learn more about the vulnerability and fine-tune the remediation suggestion.

In order to help you focus on actionable risks, Checkmarx Developer Assist enables marking risks as **Ignore**, so that the risks will no longer be shown in your IDE. You can **Revive** a risk at any time to resume showing that risk.

### About Model Context Protocol (MCP) Server

The **Checkmarx MCP Server** is a secure gateway that bridges AI-powered development assistants with the Checkmarx security platform. It defines the tools and APIs that allow AI agents — such as GitHub Copilot, Cursor AI, or Windsurf AI — to interact safely with Checkmarx's cloud services directly from within the IDE.

Once the developer successfully authenticates in the IDE, the MCP Service is automatically installed. It can also be installed manually if required. For installation and configuration instructions, see [Installation and Initial Setup](installation-and-initial-setup.md).

#### What is MCP?

**Model Context Protocol (MCP)** is an emerging open standard that enables communication between AI agents and external systems in a structured, secure, and context-aware way. By adopting MCP, Checkmarx ensures that any IDE-integrated AI assistant can securely access Checkmarx engines and services — including SAST, SCA, IaC, and API Security — through a unified interface.

#### Why Checkmarx Chose MCP

Checkmarx selected the MCP standard as the foundation for our agentic architecture because it provides:

- **Interoperability:** MCP is vendor-neutral and supported by a growing ecosystem of AI tools.
- **Security and Governance:** MCP enforces strict access control and contextual awareness, ensuring that only the right data is exposed to the AI agent under the right conditions.
- **Scalability:** The protocol supports multi-agent environments where different AI assistants operate across complex enterprise setups.
- **Future-readiness:** As new IDEs and AI tools adopt MCP, Checkmarx can easily integrate without changing the underlying architecture.

#### How it Works

Once enabled, the Checkmarx MCP Server:

1. Authenticates the developer's IDE session with Checkmarx.
2. Exposes the available Checkmarx tools and capabilities (e.g., code scanning, remediation, policy enforcement) as AI-accessible functions.
3. Allows the AI assistant to invoke these tools securely, analyze code, and propose context-aware fixes directly in the IDE.

### Developer Assist Data Security FAQ

<details>
<summary>Does realtime scanning send sensitive data to the cloud for analysis?</summary>

No. All analysis is performed locally within the IDE. The only information sent to the Checkmarx Cloud is minimal, non-sensitive metadata:

- OSS – Package name and version
- Containers - Image name and tag

No source code or sensitive data is sent.

</details>

<details>
<summary>Is sensitive data sent to the MCP when I click on "Fix with Developer Assist"?</summary>

No. All code-safe refactoring is performed by your trusted AI agent (for example, Copilot). When you click **Fix with Developer Assist**, the plugin instructs the AI agent to communicate with the MCP server and share only a unique identifier for the specific vulnerability instance. The identifier varies by scanner type:

- OSS – Package name and version
- Containers - Image name and tag
- IaC – Rule or policy ID and relevant resource attributes
- Secret Detection – Secret type
- ASCA – Vulnerability query ID

No source code or sensitive data is sent.

</details>

<details>
<summary>Is any customer data stored in the MCP or used to train AI models?</summary>

No. The entire process is done in real time so that no data is stored in the MCP. We also do not use any customer data to train AI models. We do maintain a log of system events for operational purposes.

</details>

### Realtime Scanning

Realtime scans run automatically as you work in your IDE. Scan triggers include:

- As soon as you open the workspace, the SCA scanner scans the manifest files.
- When you open any artifact supported for real-time scanners, it is scanned by the relevant scanner.
- When you edit any supported artifact.
- When you save a supported file to an external location.
- When you use an AI assistant (e.g. Copilot) to make changes to a supported file.

#### ASCA Realtime Scanner

The ASCA is a lightweight source code scanner that enables developers to identify secure coding best practice violations in the file they are working on as they code. The ASCA scan runs on your local machine and returns results within milliseconds.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Supported Languages:** Java, JavaScript (Node.js), C#, Go, and Python.

#### IaC Realtime Scanner

The IaC Realtime scanner (based on [KICS](https://docs.kics.io/latest/about/)) examines configuration definitions and scripts used to instantiate infrastructure.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Prerequisites:** A supported container engine (e.g., Docker, Podman) must be installed and running.

#### Open Source Realtime Scanner (OSS-Realtime)

Checkmarx's **OSS-Realtime** scanner analyzes your manifest files and quickly identifies risks associated with your open source dependencies, including vulnerable and malicious packages.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Supported Manifest Files:** `csproj`, `directory.packages.props`, `packages.config`, `pom.xml`, `package.json`, `requirements.txt`, `go.mod`

**Known Limitations:** Identifies vulnerabilities only in direct packages (not transitive dependencies). Custom version specifiers (^, ~, *) default to "latest" except for NPM (uses `package-lock.json`), Python (strips inline comments), and Maven (resolves from `properties` or `<dependencyManagement>`).

#### Containers Realtime Scanner

Checkmarx's **Containers Realtime** scanner analyzes your container images and identifies risks in Dockerfile, DockerCompose, and Helm charts (limited support).

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

#### Secret Detection Realtime Scanner

Checkmarx **Secret Detection** identifies more than 210 different types of exposed credentials including login credentials, access tokens, encryption keys, API keys, SSH keys, and webhook URLs.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

For the full list of secret detection rules, see [Secret Detection Rules](../vscode/README.md#secret-detection-rules).

{% hint style="info" %}
If you need to customize or extend secret scanning beyond the default rules, use the Secret Detection Query Editor.
{% endhint %}

### Checkmarx Dev Assist Agentic-AI Remediation

When the user initiates a remediation action for a risk, a session is opened with GitHub Copilot Chat. Checkmarx gathers all relevant data about the risk and submits it to the AI assistant. For supported risk types, the AI assistant sends a request to our MCP, which applies the relevant tools and returns suggested remediation steps.

#### Remediating Vulnerable or Malicious Images and Packages

{% hint style="info" icon="pencil" %}
Our MCP tool for identifying non-vulnerable versions is supported both for OSS and Containers. However, the MCP tool for finding **alternative** packages is not supported for containers.
{% endhint %}

When Checkmarx Dev Assist recommends updating a package version, our **Safe Refactor** feature searches your entire project for additional usage of that package and determines where and how the code needs to be refactored.

{% tabs %}
{% tab title="Vulnerable Packages" %}
| Case | Response |
| ---- | -------- |
| Package has non-vulnerable version | Secure version of the same package. Suggest that the user apply changes and help with fixing code if there were breaking changes. |
| Package has no completely non-vulnerable version, but has a more secure one and Checkmarx has alternative package suggestions | Suggest the most secure version; list alternative packages |
| Package has no non-vulnerable version, no more secure version, and Checkmarx has alternative package suggestions | List alternative packages |
| Package has no completely non-vulnerable version, but has a more secure one, and no alternative suggestions | Suggest the most secure version; offer option to run a web search |
| Package has no non-vulnerable version, no more secured version, and no alternative suggestions | Offer option to run a web search |
{% endtab %}

{% tab title="Malicious Packages" %}
| Case | Response |
| ---- | -------- |
| Package has non-vulnerable and non-malicious version | Secure version of the same package. Suggest that the user apply changes and help with fixing code if there were breaking changes. |
| Package has non-malicious but vulnerable version | Suggest the most secure version; list alternative packages |
| Package has no non-malicious version, and Checkmarx has alternative package suggestions | List alternative packages |
| Package has no non-malicious version, and no alternative suggestions | Offer option to run a web search |
{% endtab %}
{% endtabs %}

#### Remediating Exposed Secrets

Remediation is done by removing the hard coded secret from the code and replacing it with an Environment Variable.

#### Remediating ASCA and IaC Vulnerabilities

For vulnerabilities identified by the ASCA or IaC scanners, remediation is done by sending a customized prompt including all relevant data to your IDE's AI assistant (Copilot or Cursor). The AI assistant provides a remediated snippet that can be used in your code.
