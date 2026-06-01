# Checkmarx Developer Assist - VS Code Extension

**For VS Code and related IDEs (Cursor, Windsurf, and Kiro)**

{% hint style="warning" %}
The **Checkmarx Developer Assist** VS Code extension provides Developer Assist capabilities as a standalone experience. **Checkmarx One** customers with a Checkmarx One Assist license should use the [Checkmarx VS Code extension](https://checkmarx.com), where Developer Assist is included as part of the Checkmarx One platform. The **Checkmarx Developer Assist** and **Checkmarx** VS Code extensions are mutually exclusive. To use the Checkmarx Developer Assist extension, ensure that the Checkmarx extension is uninstalled before installation.
{% endhint %}

To learn about installation, see [Installation and Initial Setup](installation-and-initial-setup.md).

To learn about the JetBrains plugin, see [Checkmarx Developer Assist - JetBrains Plugin](../jetbrains/README.md).

## About Developer Assist

### Overview

Checkmarx Developer Assist delivers context-aware security guidance directly within your IDE, helping prevent vulnerabilities before they reach the pipeline. As developers write or refine AI-generated and existing code, it provides real-time detection, remediation, and actionable insights—ensuring security is built in from the start.

Checkmarx Developer Assist comprises two main elements:

- **Realtime Scanning -** Identify vulnerabilities in realtime during IDE development of both human-generated and AI-generated code. Our super-fast scanners run in the background whenever you edit a relevant file. Our scanners identify vulnerabilities and unmasked secrets in your code. We also identify vulnerable or malicious container images and open source packages used in your project. Results are marked as Problems which are highlighted in the code and annotated with identifying icons.
- **Agentic-AI Remediation** – Initiate an Agentic-AI session to receive remediation suggestions. Checkmarx feeds all relevant info to the AI agent which accesses our Model Context Protocol (MCP) server to gather data from our proprietary databases and customized AI models. The AI assistant then uses this data to generate remediated code for your project. You can accept the suggested changes or you can chat with the AI agent to learn more about the vulnerability and fine-tune the remediation suggestion.

In order to help you focus on actionable risks, Checkmarx Developer Assist enables marking risks as **Ignore**, so that the risks will no longer be shown in your IDE. You can **Revive** a risk at any time to resume showing that risk.

#### Key Features

- An advanced security agent that delivers real-time context-aware prevention, remediation, and guidance to developers from the IDE.
- Realtime scanners identify risks as you code.
  - AI Secure Coding Assistant (ASCA), a lightweight source code scanner, enables developers to identify secure coding best practice violations in the file that they are working on as they code.
  - Specialized realtime scanners identify vulnerable open source packages and container images, as well as exposed secrets and IaC risks.
- MCP-based agentic AI remediation.
- AI powered explanation of risk details.
- Reduce noise by marking false positives as ignored.

### About Model Context Protocol (MCP) Server

The **Checkmarx MCP Server** is a secure gateway that bridges AI-powered development assistants with the Checkmarx security platform. It defines the tools and APIs that allow AI agents — such as GitHub Copilot, Cursor AI, or Windsurf AI — to interact safely with Checkmarx's cloud services directly from within the IDE.

Once the developer successfully authenticates in the IDE, the MCP Service is automatically installed. It can also be installed manually if required. For installation and configuration instructions, see [Installation and Initial Setup](installation-and-initial-setup.md).

#### What is MCP?

**Model Context Protocol (MCP)** is an emerging open standard that enables communication between AI agents and external systems in a structured, secure, and context-aware way. By adopting MCP, Checkmarx ensures that any IDE-integrated AI assistant can securely access Checkmarx engines and services — including SAST, SCA, IaC, and API Security — through a unified interface.

#### Why Checkmarx Chose MCP

Checkmarx selected the MCP standard as the foundation for our agentic architecture because it provides:

- **Interoperability:** MCP is vendor-neutral and supported by a growing ecosystem of AI tools. It allows Checkmarx to connect seamlessly with multiple AI assistants and IDEs using a consistent communication layer.
- **Security and Governance:** MCP enforces strict access control and contextual awareness, ensuring that only the right data is exposed to the AI agent under the right conditions. This aligns with enterprise-grade compliance and governance models.
- **Scalability:** The protocol supports multi-agent environments where different AI assistants operate across complex enterprise setups, making it ideal for large-scale deployments.
- **Future-readiness:** As new IDEs and AI tools adopt MCP, Checkmarx can easily integrate without changing the underlying architecture — ensuring long-term compatibility and innovation flexibility.

#### How it Works

Once enabled, the Checkmarx MCP Server:

1. Authenticates the developer's IDE session with Checkmarx.
2. Exposes the available Checkmarx tools and capabilities (e.g., code scanning, remediation, policy enforcement) as AI-accessible functions.
3. Allows the AI assistant to invoke these tools securely, analyze code, and propose context-aware fixes directly in the IDE.

This creates a secure, AI-augmented development experience — where Checkmarx intelligence powers real-time risk identification and remediation during coding.

### Recommended Models for Code Remediation

Based on a combination of internal evaluation and publicly available coding benchmarks, we have determined that the following models currently provide the most reliable results when performing complex remediation tasks.

{% hint style="warning" %}
Even the most advanced models currently struggle to consistently generate fully secure and production-ready backend code. Research benchmarks show that a large proportion of generated solutions still contain vulnerabilities or functional issues.

Also, keep in mind that these recommendations are based on current performance of available models. However, since this is a constantly fluctuating market, the list of preferred models is likely to change over time.
{% endhint %}

{% tabs %}
{% tab title="Tier 1 - Best performance" %}
{% hint style="info" %}
Recommended for complex remediation tasks, such as multi-file refactoring, vulnerability fixes, and test generation.
{% endhint %}

- Claude Opus (4.5 / 4.6 class)
- GPT-5 / GPT-5 Codex
- OpenAI o3
- Claude Sonnet (latest versions)
{% endtab %}

{% tab title="Tier 2 - Strong general coding" %}
- GPT-4.1
- Gemini Pro models
- DeepSeek R1
- Claude 3.7 Sonnet
{% endtab %}

{% tab title="Tier 3 - Simpler tasks" %}
- GPT-4o
- Codestral
- Qwen-Coder models
- Llama-family coding models
{% endtab %}
{% endtabs %}

#### Recommendation Methodology

These recommendations are based on a combination of **internal evaluation** and **publicly available coding benchmarks**. Internally, we assess models in secure code remediation scenarios, evaluating their ability to:

- generate correct code fixes
- perform safe refactoring across multiple files
- maintain compilation integrity
- preserve existing tests and generate additional tests when necessary

In addition to internal testing, we review results from industry and academic benchmarks such as BaxBench, which evaluates the ability of LLMs to generate secure and correct backend applications across multiple frameworks and programming languages.

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

Realtime scans run automatically as you work in your IDE. The following is a list of scan triggers:

- As soon as you open the workspace, the SCA scanner scans the manifest files.
- When you open any artifact that is supported for real-time scanners it is scanned by the relevant scanner.
- When you edit any supported artifact.
- When you save a supported file to an external location.
- When you use an AI assistant (e.g. Copilot), to make changes to a supported file.

#### Checkmarx AI Secure Coding Assistant (ASCA) Realtime Scanner

The ASCA is a lightweight source code scanner that enables developers to identify secure coding best practice violations in the file that they are working on as they code. The ASCA scanner runs in the background as you work in your IDE. Unlike SAST engines that scan entire projects and analyze complex source code flows, ASCA focuses on individual files and short code snippets, including AI-generated code.

Whenever you edit a file in VS Code the ASCA scanner automatically scans that file. The ASCA scan runs on your local machine as a running process and returns results within milliseconds.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Supported Languages**

ASCA currently supports Java, JavaScript (Node.js), C#, Go and Python.

#### IaC Realtime Scanner

The IaC Realtime scanner (based on the [KICS](https://docs.kics.io/latest/about/) open source project powered by Checkmarx) examines configuration definitions and scripts used to instantiate infrastructure to ensure the resulting resources are secure.

A scan runs automatically whenever you edit an infrastructure file of a [supported type](https://docs.kics.io/latest/platforms/).

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Prerequisites**

- You must have a supported container engine (e.g., Docker, Podman etc.) installed and running in your environment.

#### Open Source Realtime Scanner (OSS-Realtime)

Checkmarx's **OSS-Realtime** scanner is a lightweight version of our SCA scanner that analyzes your manifest files and quickly identifies risks associated with your open source dependencies. This includes vulnerable packages as well as packages that we have identified as malicious.

{% hint style="warning" %}
The OSS realtime scanner is less comprehensive than the full Checkmarx One SCA scanner. See Supported Manifest Files and Known Limitations below.
{% endhint %}

Scans are triggered when the developer opens a project in the IDE that includes a manifest file (e.g., `package.json`, `requirements.txt`). In addition, whenever the developer adds, moves or edits a manifest file within the IDE the project is re-scanned.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Supported Manifest Files**

- **Dotnet:** `csproj`, `directory.packages.props`, `packages.config`
- **Maven:** `pom.xml`
- **npm:** `package.json`
- **Pip:** `requirements.txt` (limited support, see Known Limitations below)
- **Go:** `go.mod`

**Known Limitations**

- Identifies vulnerabilities only in direct packages not in transitive dependencies.
- For **Python** `requirements.txt` files, only traditional, manually created files are supported (i.e., `package==version` format). Auto-generated formats such as those produced by pip freeze, pip-tools, Poetry etc. are not supported.
- Many package managers use custom version specifiers (e.g., ^, ~, *, etc.) to indicate which version to use. OSS scanner does not support these characters. Aside from the cases listed below, when it encounters these characters the scanner defaults to analyzing the "latest" version of the package. Similarly, when no version is provided, the scanner defaults to "latest".

  **Exceptions:**
  - **NPM** - If a `package-lock.json` file is provided, we get the actual version from that file. If the `package-lock.json` does not exist, run `npm install` to generate a `package-lock.json`.
  - **Python** - If the version includes a comment after it, the comment will be removed and only the specific version will be used. For example: `requests==2.25.1  # my comment`
  - **Maven** - If the version is defined via a property, it will be retrieved from `properties`. If the version is empty, the resolved version from `<dependencyManagement>` will be used.

#### Containers Realtime Scanner

Checkmarx's **Containers Realtime** scanner is a lightweight version of our Container Security scanner that analyzes your container images and quickly identifies risks associated with your images and associated packages.

Scans are triggered when the developer edits a project in the IDE that includes a container image file (e.g., Dockerfile). In addition, whenever the developer adds, moves or edits an image file within the IDE the project is re-scanned.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Supported File Types**

- Dockerfile
- DockerCompose
- Helm chart (limited support)

#### Checkmarx Secret Detection Realtime Scanner

Checkmarx **Secret Detection** reduces risk by quickly identifying sensitive credentials that are exposed in your code. Checkmarx identifies more than 210 different types of login credentials, access tokens, encryption keys, API keys, SSH keys, webhook URLs, and other unsecured sensitive information.

Whenever you edit a file in the IDE, Secret Detection is run on that file.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

**Secret Detection Rules**

The following table shows the list of rules used to detect various types of secrets.

<details>
<summary>Rules Table</summary>

| Name | Description | Type | Validity Check |
| ---- | ----------- | ---- | -------------- |
| adafruit-api-key | Identified a potential Adafruit API Key, which could lead to unauthorized access to Adafruit services and sensitive data exposure. | api-key | |
| adobe-client-id | Detected a pattern that resembles an Adobe OAuth Web Client ID, posing a risk of compromised Adobe integrations and data breaches. | client-id | |
| adobe-client-secret | Discovered a potential Adobe Client Secret, which, if exposed, could allow unauthorized Adobe service access and data manipulation. | client-secret | |
| age-secret-key | Discovered a potential Age encryption tool secret key, risking data decryption and unauthorized access to sensitive information. | secret-key | |
| airtable-api-key | Uncovered a possible Airtable API Key, potentially compromising database access and leading to data leakage or alteration. | api-key | |
| algolia-api-key | Identified an Algolia API Key, which could result in unauthorized search operations and data exposure on Algolia-managed platforms. | api-key | |
| alibaba-access-key-id | Detected an Alibaba Cloud AccessKey ID, posing a risk of unauthorized cloud resource access and potential data compromise. | access-key, access-id | V |
| alibaba-secret-key | Discovered a potential Alibaba Cloud Secret Key, potentially allowing unauthorized operations and data access within Alibaba Cloud. | secret-key | V |
| anthropic-admin-api-key | Detected an Anthropic Admin API Key, risking unauthorized access to administrative functions and sensitive AI model configurations. | api-key | |
| anthropic-api-key | Identified an Anthropic API Key, which may compromise AI assistant integrations and expose sensitive data to unauthorized access. | api-key | |
| asana-client-id | Discovered a potential Asana Client ID, risking unauthorized access to Asana projects and sensitive task information. | client-id | |
| asana-client-secret | Identified an Asana Client Secret, which could lead to compromised project management integrity and unauthorized access. | client-secret | |
| atlassian-api-token | Detected an Atlassian API token, posing a threat to project management and collaboration tool security and data confidentiality. | api-token | |
| aws-access-token | Identified a pattern that may indicate AWS credentials, risking unauthorized cloud resource access and data breaches on AWS platforms. | access-token | |
| azure-ad-client-secret | Azure AD Client Secret | client-secret | |
| github-pat | Uncovered a GitHub Personal Access Token, potentially leading to unauthorized repository access and sensitive content exposure. | access-token | V |
| github-fine-grained-pat | Found a GitHub Fine-Grained Personal Access Token, risking unauthorized repository access and code manipulation. | access-token | V |
| gitlab-pat | Identified a GitLab Personal Access Token, risking unauthorized access to GitLab repositories and codebase exposure. | access-token | V |
| gcp-api-key | Uncovered a GCP API key, which could lead to unauthorized access to Google Cloud services and data breaches. | api-key | V |
| openai-api-key | Found an OpenAI API Key, posing a risk of unauthorized access to AI services and data manipulation. | api-key | |
| private-key | Identified a Private Key, which may compromise cryptographic security and sensitive data encryption. | private-key | |
| slack-bot-token | Identified a Slack Bot token, which may compromise bot integrations and communication channel security. | access-token | |
| slack-webhook-url | Discovered a Slack Webhook, which could lead to unauthorized message posting and data leakage in Slack channels. | webhook | |
| stripe-access-token | Found a Stripe Access Token, posing a risk to payment processing services and sensitive financial data. | access-token | |
| authenticated-url | Identify username:password inside URLs | sensitive-url | |

</details>

{% hint style="info" %}
If you need to customize or extend secret scanning beyond the default rules, use the Secret Detection Query Editor.
{% endhint %}

### Checkmarx Dev Assist Agentic-AI Remediation

When the user initiates a remediation action for a risk, a session is opened with the IDE's AI assistant (GitHub Copilot for VS Code or the local AI in Cursor). Checkmarx gathers all relevant data about the risk and submits it to the AI assistant. For supported risk types, the AI assistant sends a request to our MCP which applies the relevant tools and returns a response with suggested remediation steps. The AI assistant implements the changes and offers the user the option to accept the changes or continue a chat session to refine the remediation.

{% hint style="info" icon="pencil" %}
If for some reason the Checkmarx MCP connection is unavailable, the remediation agent automatically falls back to the IDE's LLM to provide remediation suggestions. In this case, a notification is displayed indicating that the recommendations are not based on Checkmarx's specialized security models.
{% endhint %}

#### Remediating Vulnerable or Malicious Images and Packages

Remediation for OSS and Container risks is done by identifying the best non-vulnerable package that provides the same functionality as the vulnerable package.

{% hint style="info" icon="pencil" %}
Our MCP tool for identifying non-vulnerable versions is supported both for OSS and Containers. However, the MCP tool for finding **alternative** packages is not supported for containers.
{% endhint %}

When Checkmarx Dev Assist recommends updating a package version, our **Safe Refactor** feature searches your entire project for additional usage of that package and determines where and how the code needs to be refactored to accommodate the package update.

**Remediation Logic**

{% hint style="info" icon="pencil" %}
When suggesting a non-vulnerable version or a more secure version, the MCP always recommends the smallest effective upgrade, rather than jumping to a higher version.
{% endhint %}

{% tabs %}
{% tab title="Vulnerable Packages" %}
| Case | Response |
| ---- | -------- |
| Package has non-vulnerable version | Secure version of the same package. Suggest that the user apply changes and help with fixing code if there were breaking changes. |
| Package has no completely non-vulnerable version, but has a more secure one and Checkmarx has alternative package suggestions | Suggest the most secure version of the same package; list alternative packages |
| Package has no non-vulnerable version, and no more secure version, and Checkmarx has alternative package suggestions | List alternative packages |
| Package has no completely non-vulnerable version, but has a more secure one, and Checkmarx does not have alternative package suggestions | Suggest the most secure version of the same package; offer user option to run a web search |
| Package has no non-vulnerable version, no more secured version, and Checkmarx does not have alternative package suggestions | Offer user option to run a web search |
{% endtab %}

{% tab title="Malicious Packages" %}
| Case | Response |
| ---- | -------- |
| Package has non-vulnerable and non-malicious version | Secure version of the same package. Suggest that the user apply changes and help with fixing code if there were breaking changes. |
| Package has non-malicious but vulnerable version | Suggest the most secure version of the same package; list alternative packages |
| Package has no non-malicious version, and Checkmarx has alternative package suggestions | List alternative packages |
| Package has no non-malicious version, and Checkmarx does not have alternative package suggestions | Offer user option to run a web search |
{% endtab %}
{% endtabs %}

#### Remediating Exposed Secrets

Remediation is done by removing the hard coded secret from the code and replacing it with an Environment Variable that can be used to store the secret in a secure manner.

#### Remediating ASCA and IaC Vulnerabilities

For vulnerabilities identified by the ASCA or IaC Realtime scanners, remediation is done by sending a customized prompt including all relevant data about the vulnerability instance to your IDE's AI assistant (Copilot or Cursor). The AI assistant then provides a remediated snippet that can be used in your code.
