# overview

{% hint style="warning" %}
The **Checkmarx Developer Assist** VS Code extension provides Developer Assist capabilities as a standalone experience. **Checkmarx One** customers with a Checkmarx One Assist license should use the [Checkmarx VS Code extension](https://checkmarx.com/), where Developer Assist is included as part of the Checkmarx One platform. The **Checkmarx Developer Assist** and **Checkmarx** VS Code extensions are mutually exclusive — ensure the Checkmarx extension is uninstalled before installing Developer Assist.
{% endhint %}

## About Developer Assist

### Overview

Checkmarx Developer Assist delivers context-aware security guidance directly within your IDE, helping prevent vulnerabilities before they reach the pipeline. As developers write or refine AI-generated and existing code, it provides real-time detection, remediation, and actionable insights — ensuring security is built in from the start.

Checkmarx Developer Assist comprises two main elements:

**Realtime Scanning** — Identify vulnerabilities in realtime during IDE development of both human-generated and AI-generated code. Scanners run in the background whenever you edit a relevant file, identifying vulnerabilities, unmasked secrets, vulnerable/malicious container images, and open source packages. Results are marked as Problems, highlighted in the code with squiggly underlines and annotated with identifying icons.

**Agentic-AI Remediation** — Initiate an Agentic-AI session to receive remediation suggestions. Checkmarx feeds all relevant info to the AI agent, which accesses our Model Context Protocol (MCP) server to gather data from our proprietary databases and customized AI models. The AI assistant generates remediated code for your project. You can accept suggested changes or chat with the AI agent to learn more and fine-tune the remediation.

To help you focus on actionable risks, you can mark risks as **Ignored** so they no longer appear in your IDE. You can **Revive** any risk at any time to resume showing it.

#### Key Features

* An advanced security agent that delivers real-time, context-aware prevention, remediation, and guidance from the IDE.
* Realtime scanners that identify risks as you code:
  * **AI Secure Coding Assistant (ASCA)** — a lightweight source code scanner that identifies secure coding best practice violations in the file you're working on.
  * Specialized realtime scanners for vulnerable open source packages, container images, exposed secrets, and IaC risks.
* MCP-based agentic AI remediation.
* AI-powered explanation of risk details.
* Reduce noise by marking false positives as ignored.

***

## About Model Context Protocol (MCP) Server

The **Checkmarx MCP Server** is a secure gateway that bridges AI-powered development assistants with the Checkmarx security platform. It defines the tools and APIs that allow AI agents — such as GitHub Copilot, Cursor AI, or Windsurf AI — to interact safely with Checkmarx's cloud services directly from within the IDE.

Once the developer successfully authenticates in the IDE, the MCP Service is automatically installed. It can also be installed manually if required.

### What is MCP?

**Model Context Protocol (MCP)** is an emerging open standard that enables communication between AI agents and external systems in a structured, secure, and context-aware way. By adopting MCP, Checkmarx ensures that any IDE-integrated AI assistant can securely access Checkmarx engines and services — including SAST, SCA, IaC, and API Security — through a unified interface.

### Why Checkmarx Chose MCP

* **Interoperability:** MCP is vendor-neutral and supported by a growing ecosystem of AI tools, allowing Checkmarx to connect seamlessly with multiple AI assistants and IDEs.
* **Security and Governance:** MCP enforces strict access control and contextual awareness, ensuring that only the right data is exposed under the right conditions.
* **Scalability:** The protocol supports multi-agent environments across complex enterprise setups.
* **Future-readiness:** As new IDEs and AI tools adopt MCP, Checkmarx can integrate without changing the underlying architecture.

### How it Works

Once enabled, the Checkmarx MCP Server:

{% stepper %}
{% step %}
### Authenticate

Authenticates the developer's IDE session with Checkmarx.
{% endstep %}

{% step %}
### Expose capabilities

Exposes the available Checkmarx tools (code scanning, remediation, policy enforcement) as AI-accessible functions.
{% endstep %}

{% step %}
### Enable AI-driven fixes

Allows the AI assistant to invoke these tools securely, analyze code, and propose context-aware fixes directly in the IDE.
{% endstep %}
{% endstepper %}

***

## Recommended Models for Code Remediation

Based on internal evaluation and publicly available coding benchmarks, the following models currently provide the most reliable results for complex remediation tasks.

{% hint style="warning" %}
Even the most advanced models currently struggle to consistently generate fully secure and production-ready backend code. Research benchmarks show that a large proportion of generated solutions still contain vulnerabilities or functional issues. These recommendations are based on current model performance and may change over time.
{% endhint %}

<details>

<summary>Tier 1 — Best performance for complex remediation</summary>

Recommended for complex remediation tasks such as multi-file refactoring, vulnerability fixes, and test generation.

* Claude Opus (4.5 / 4.6 class)
* GPT-5 / GPT-5 Codex
* OpenAI o3
* Claude Sonnet (latest versions)

</details>

<details>

<summary>Tier 2 — Strong general coding performance</summary>

* GPT-4.1
* Gemini Pro models
* DeepSeek R1
* Claude 3.7 Sonnet

</details>

<details>

<summary>Tier 3 — Suitable for simpler tasks</summary>

* GPT-4o
* Codestral
* Qwen-Coder models
* Llama-family coding models

</details>

### Recommendation Methodology

These recommendations are based on a combination of **internal evaluation** and **publicly available coding benchmarks**. Internally, we assess models in secure code remediation scenarios, evaluating their ability to generate correct code fixes, perform safe refactoring across multiple files, maintain compilation integrity, and preserve or generate tests.

In addition, we review industry and academic benchmarks such as **BaxBench**, which evaluates LLMs on generating secure and correct backend applications across multiple frameworks and languages.

***

## Developer Assist Data Security FAQ

<details>

<summary>Does realtime scanning send sensitive data to the cloud for analysis?</summary>

No. All analysis is performed locally within the IDE. The only information sent to the Checkmarx Cloud is minimal, non-sensitive metadata:

* OSS — Package name and version
* Containers — Image name and tag

No source code or sensitive data is sent.

</details>

<details>

<summary>Is sensitive data sent to the MCP when I click "Fix with Developer Assist"?</summary>

No. All code-safe refactoring is performed by your trusted AI agent (e.g., Copilot). When you click **Fix with Developer Assist**, the plugin instructs the AI agent to communicate with the MCP server and share only a unique identifier for the specific vulnerability instance:

* OSS — Package name and version
* Containers — Image name and tag
* IaC — Rule or policy ID and relevant resource attributes
* Secret Detection — Secret type
* ASCA — Vulnerability query ID

No source code or sensitive data is sent.

</details>

<details>

<summary>Is any customer data stored in the MCP or used to train AI models?</summary>

No. The entire process is done in real time so that no data is stored in the MCP. We do not use any customer data to train AI models. We do maintain a log of system events for operational purposes.

</details>

***

## Realtime Scanning

Realtime scans run automatically as you work in your IDE. Scan triggers include:

* When you open the workspace, the SCA scanner scans manifest files.
* When you open any artifact supported by realtime scanners.
* When you edit any supported artifact.
* When you save a supported file to an external location.
* When you use an AI assistant (e.g., Copilot) to make changes to a supported file.

### ASCA — AI Secure Coding Assistant Realtime Scanner

The ASCA is a lightweight source code scanner that identifies secure coding best practice violations in the file you're working on. It runs locally in the background and returns results within milliseconds.

{% hint style="info" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Supported Languages:** Java, JavaScript (Node.js), C#, Go, and Python.

### IaC Realtime Scanner

The IaC Realtime scanner (based on the [KICS](https://docs.kics.io/latest/about/) open source project powered by Checkmarx) examines infrastructure configuration definitions and scripts. A scan runs automatically whenever you edit a [supported infrastructure file type](https://docs.kics.io/latest/platforms/).

{% hint style="info" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Prerequisites:** A supported container engine (e.g., Docker, Podman) must be installed and running.

### Open Source Realtime Scanner (OSS-Realtime)

Checkmarx's **OSS-Realtime** scanner analyzes manifest files and quickly identifies risks associated with open source dependencies, including vulnerable and malicious packages.

Scans are triggered when you open a project with a manifest file (e.g., `package.json`, `requirements.txt`), or whenever you add, move, or edit a manifest file.

{% hint style="info" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Supported manifest files:** `csproj`, `directory.packages.props`, `packages.config`, `pom.xml`, `package.json`, `requirements.txt` (limited), `go.mod`.

{% hint style="warning" %}
The OSS realtime scanner is less comprehensive than the full Checkmarx One SCA scanner. It identifies vulnerabilities only in direct packages, not transitive dependencies. Many package managers use custom version specifiers (^, \~, \*, etc.) that the scanner does not support — it defaults to analyzing the "latest" version when these are encountered.

**Exceptions:** NPM uses `package-lock.json` for actual versions; Python strips trailing comments; Maven resolves property-defined and `<dependencyManagement>` versions.
{% endhint %}

### Containers Realtime Scanner

Checkmarx's **Containers Realtime** scanner analyzes container image files and quickly identifies risks. Scans are triggered when you edit a project containing a container image file (e.g., Dockerfile), or when you add, move, or edit such files.

**Supported file types:** Dockerfile, DockerCompose, Helm chart (limited support).

### Secret Detection Realtime Scanner

Checkmarx **Secret Detection** identifies sensitive credentials exposed in your code. Checkmarx identifies more than 210 different types of credentials, including login credentials, access tokens, encryption keys, API keys, SSH keys, and webhook URLs.

{% hint style="info" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

<details>

<summary>Secret Detection Rules Table</summary>

| Name                    | Description                                            | Type                  | Validity Check |
| ----------------------- | ------------------------------------------------------ | --------------------- | -------------- |
| adafruit-api-key        | Identified a potential Adafruit API Key                | api-key               |                |
| adobe-client-id         | Detected an Adobe OAuth Web Client ID pattern          | client-id             |                |
| adobe-client-secret     | Discovered a potential Adobe Client Secret             | client-secret         |                |
| age-secret-key          | Discovered a potential Age encryption tool secret key  | secret-key            |                |
| airtable-api-key        | Uncovered a possible Airtable API Key                  | api-key               |                |
| algolia-api-key         | Identified an Algolia API Key                          | api-key               |                |
| alibaba-access-key-id   | Detected an Alibaba Cloud AccessKey ID                 | access-key, access-id | ✓              |
| alibaba-secret-key      | Discovered a potential Alibaba Cloud Secret Key        | secret-key            | ✓              |
| anthropic-admin-api-key | Detected an Anthropic Admin API Key                    | api-key               |                |
| anthropic-api-key       | Identified an Anthropic API Key                        | api-key               |                |
| asana-client-id         | Discovered a potential Asana Client ID                 | client-id             |                |
| asana-client-secret     | Identified an Asana Client Secret                      | client-secret         |                |
| atlassian-api-token     | Detected an Atlassian API token                        | api-token             |                |
| aws-access-token        | Identified a pattern that may indicate AWS credentials | access-token          |                |
| azure-ad-client-secret  | Azure AD Client Secret                                 | client-secret         |                |
| bitbucket-client-id     | Discovered a potential Bitbucket Client ID             | client-id             |                |
| bitbucket-client-secret | Discovered a potential Bitbucket Client Secret         | client-secret         |                |
| github-pat              | Uncovered a GitHub Personal Access Token               | access-token          | ✓              |
| github-fine-grained-pat | Found a GitHub Fine-Grained Personal Access Token      | access-token          | ✓              |
| gitlab-pat              | Identified a GitLab Personal Access Token              | access-token          | ✓              |
| gcp-api-key             | Uncovered a GCP API key                                | api-key               | ✓              |
| openai-api-key          | Found an OpenAI API Key                                | api-key               |                |
| private-key             | Identified a Private Key                               | private-key           |                |
| slack-webhook-url       | Discovered a Slack Webhook                             | webhook               |                |
| stripe-access-token     | Found a Stripe Access Token                            | access-token          |                |
| ... and 180+ more rules |                                                        |                       |                |

{% hint style="info" %}
If you need to customize or extend secret scanning beyond the default rules, use the Secret Detection Query Editor.
{% endhint %}

</details>

***

## Agentic-AI Remediation

When you initiate remediation for a risk, a session is opened with the IDE's AI assistant (GitHub Copilot for VS Code or the local AI in Cursor). Checkmarx gathers all relevant data about the risk and submits it to the AI assistant. For supported risk types, the AI assistant sends a request to our MCP server, which applies the relevant tools and returns suggested remediation steps.

{% hint style="info" %}
If the Checkmarx MCP connection is unavailable, the remediation agent automatically falls back to the IDE's LLM to provide remediation suggestions. A notification is displayed indicating that the recommendations are not based on Checkmarx's specialized security models.
{% endhint %}

### Remediating Vulnerable or Malicious Images and Packages

Remediation for OSS and Container risks identifies the best non-vulnerable package with the same functionality. When our proprietary databases indicate a remediated version is available, the closest version to the current one is used. When no remediated version is available, our MCP server uses a dedicated AI tool to identify alternative packages.

{% hint style="info" %}
The MCP tool for identifying non-vulnerable versions supports both OSS and Containers. The MCP tool for finding **alternative** packages is not supported for containers.
{% endhint %}

The **Safe Refactor** feature searches your entire project for additional usage of a package and determines where and how the code needs to be refactored to accommodate the update.

<details>

<summary>Remediation Logic — Vulnerable Packages</summary>

| Case                                                                                         | Response                                                               |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Package has a non-vulnerable version                                                         | Suggest the secure version; help fix breaking changes                  |
| No fully non-vulnerable version, but more secure version exists + Checkmarx has alternatives | Suggest most secure version + list alternatives                        |
| No non-vulnerable version, no more secure version + Checkmarx has alternatives               | List alternative packages                                              |
| No fully non-vulnerable version, but more secure version exists + no alternatives            | Suggest most secure version + offer web search (user's responsibility) |
| No non-vulnerable or more secure version + no alternatives                                   | Offer web search (user's responsibility)                               |

</details>

<details>

<summary>Remediation Logic — Malicious Packages</summary>

| Case                                                   | Response                                              |
| ------------------------------------------------------ | ----------------------------------------------------- |
| Package has a non-vulnerable and non-malicious version | Suggest the secure version; help fix breaking changes |
| Package has a non-malicious but vulnerable version     | Suggest most secure version + list alternatives       |
| No non-malicious version + Checkmarx has alternatives  | List alternative packages                             |
| No non-malicious version + no alternatives             | Offer web search (user's responsibility)              |

</details>

### Remediating Exposed Secrets

Remediation removes the hard-coded secret from the code and replaces it with an Environment Variable for secure storage.

### Remediating ASCA and IaC Vulnerabilities

For ASCA or IaC vulnerabilities, remediation sends a customized prompt including all relevant data about the vulnerability instance to your IDE's AI assistant (Copilot or Cursor). The AI assistant provides a remediated snippet that can be used in your code.
