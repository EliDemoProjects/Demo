---
description: For VS Code and related IDEs (Cursor, Windsurf and Kiro)
---

# Checkmarx Developer Assist - VS Code Extension

{% hint style="warning" %}
The **Checkmarx Developer Assist** VS Code extension provides Developer Assist capabilities as a standalone experience. **Checkmarx One** customers with a Checkmarx One Assist license should use the [Checkmarx VS Code extension](/document/preview/68742#UUID-40c069db-cf3d-be0b-7622-6f57caf5f55a), where Developer Assist is included as part of the Checkmarx One platform. The **Checkmarx Developer Assist** and **Checkmarx** VS Code extensions are mutually exclusive. To use the Checkmarx Developer Assist extension, ensure that the Checkmarx extension is uninstalled before installation.
{% endhint %}

To learn about installation, see [Installation and Initial Setup](installation-and-initial-setup.md).

To learn about the JetBrains plugin, see [here](../jetbrains-plugin/README.md).

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

Once the developer successfully authenticates in the IDE, the MCP Service is automatically installed. It can also be installed manually if required. For installation and configuration instructions, see below.

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

See below for additional details as well as instructions for installing and using the MCP server as part of Checkmarx Dev Assist.

### Recommended Models for Code Remediation

Based on a combination of internal evaluation and publicly available coding benchmarks, we have determined that the following models currently provide the most reliable results when performing complex remediation tasks.

{% hint style="warning" %}
Even the most advanced models currently struggle to consistently generate fully secure and production-ready backend code. Research benchmarks show that a large proportion of generated solutions still contain vulnerabilities or functional issues.

Also, keep in mind that these recommendations are based on current performance of available models. However, since this is a constantly fluctuating market, the list of preferred models is likely to change over time.
{% endhint %}

<details>

<summary>Tier 1 - Best performance for complex remediation</summary>

{% hint style="info" icon="pencil" %}
Recommended for complex remediation tasks, such as multi-file refactoring, vulnerability fixes, and test generation.
{% endhint %}

- Claude Opus (4.5 / 4.6 class)
- GPT-5 / GPT-5 Codex
- OpenAI o3
- Claude Sonnet (latest versions)

</details>

<details>

<summary>Tier 2 - Strong general coding performance</summary>

- GPT-4.1
- Gemini Pro models
- DeepSeek R1
- Claude 3.7 Sonnet

</details>

<details>

<summary>Tier 3 - Suitable for simpler tasks</summary>

- GPT-4o
- Codestral
- Qwen-Coder models
- Llama-family coding models

</details>

#### Recommendation Methodology

These recommendations are based on a combination of **internal evaluation** and **publicly available coding benchmarks**. Internally, we assess models in secure code remediation scenarios, evaluating their ability to:

- generate correct code fixes
- perform safe refactoring across multiple files
- maintain compilation integrity
- preserve existing tests and generate additional tests when necessary

In addition to internal testing, we review results from industry and academic benchmarks that evaluate LLM performance on code generation, reasoning, and secure backend development. These include benchmarks such as BaxBench, which evaluates the ability of LLMs to generate secure and correct backend applications across multiple frameworks and programming languages.

BaxBench results highlight that even state-of-the-art models still struggle to consistently produce both correct and secure code, with many generated solutions containing vulnerabilities or functional errors. By combining insights from these benchmarks with internal testing, we identify models that currently provide the most reliable outcomes for code remediation and security-aware refactoring workflows.

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

The following sections describe the various realtime scanners that are included in Checkmarx Dev Assist.

#### Checkmarx AI Secure Coding Assistant (ASCA) Realtime Scanner

The ASCA is a lightweight source code scanner that enables developers to identify secure coding best practice violations in the file that they are working on as they code. The ASCA scanner runs in the background as you work in your IDE. Unlike SAST engines that scan entire projects and analyze complex source code flows, ASCA focuses on individual files and short code snippets, including AI-generated code.

Whenever you edit a file in VS Code the ASCA scanner automatically scans that file. The ASCA scan runs on your local machine as a running process and returns results within milliseconds.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

##### Supported Languages

ASCA currently supports Java, JavaScript (Node.js), C#, Go and Python.

#### IaC Realtime Scanner

The IaC Realtime scanner (based on the [KICS](https://docs.kics.io/latest/about/) open source project powered by Checkmarx) examines configuration definitions and scripts used to instantiate infrastructure to ensure the resulting resources are secure.

A scan runs automatically whenever you edit an infrastructure file of a [supported type](https://docs.kics.io/latest/platforms/).

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

##### Prerequisites

- You must have a supported container engine (e.g., Docker, Podman etc.) installed and running in your environment.

#### Open Source Realtime Scanner (OSS-Realtime)

Checkmarx's **OSS-Realtime** scanner is a lightweight version of our SCA scanner that analyzes your manifest files and quickly identifies risks associated with your open source dependencies. This includes vulnerable packages as well as packages that we have identified as malicious.

{% hint style="warning" %}
The OSS realtime scanner is less comprehensive than the full Checkmarx One SCA scanner, see [Supported Manifest Files](#supported-manifest-files) and [Known Limitations](#known-limitations) below.
{% endhint %}

Scans are triggered when the developer opens a project in the IDE that includes a manifest file (e.g., package.json, requirements.txt). In addition, whenever the developer adds, moves or edits a manifest file within the IDE the project is re-scanned.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

##### Supported Manifest Files

In the initial phase, the plugin supports the following popular manifest files:

- **Dotnet:** `csproj`, `directory.packages.props`, `packages.config`
- **Maven:** `pom.xml`
- **npm:** `package.json`
- **Pip:** `requirements.txt` (limited support, see [Known Limitations](#known-limitations) below)
- **Go:** `go.mod`

##### Known Limitations

- Identifies vulnerabilities only in direct packages not in transitive dependencies.
- For **Python** `requirements.txt` files, only traditional, manually created files are supported (i.e., package==version format). Auto-generated formats such as those generated by pip freeze, pip-tools, Poetry etc. are not supported.
- Many package managers use custom version specifiers (e.g., ^, ~, *, etc.) to indicate which version to use. OSS scanner does not support these characters. Aside from the cases listed below, when it encounters these characters the scanner defaults to analyzing the "latest" version of the package. Similarly, when no version is provided, the scanner defaults to "latest".

  **Exceptions:**

  - **NPM** - If a `package-lock.json` file is provided, we get the actual version from that file. If the `package-lock.json` does not exist, you run `npm install`, to generate a `package-lock.json`.
  - **Python** - If the version includes a comment after it, the comment will be removed and only the specific version will be used. For example: requests==2.25.1  # my comment
  - **Maven** -
    - If the version is defined via a property, it will be retrieved from the `properties`.
    - If the version is empty, the resolved version from `<dependencyManagement>` will be used.

#### Containers Realtime Scanner

Checkmarx's **Containers Realtime** scanner is a lightweight version of our Container Security scanner that analyzes your container images and quickly identifies risks associated with your images and associated packages. This includes images that use vulnerable packages or packages that we have identified as malicious.

Scans are triggered when the developer edits a project in the IDE that includes a container image file (e.g., Dockerfile). In addition, whenever the developer adds, moves or edits an image file within the IDE the project is re-scanned.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

##### Supported File Types

In the initial phase, the plugin supports the following popular image files:

- Dockerfile
- DockerCompose
- Helm chart (limited support)

#### Checkmarx Secret Detection Realtime Scanner

Checkmarx **Secret Detection** reduces risk by quickly identifying sensitive credentials that are exposed in your code, enabling your development and security teams to remove and change the discovered secrets. Checkmarx identifies more than 210 different types of login credentials, access tokens, encryption keys, API keys, SSH keys, webhook URLs, and other unsecured sensitive information.

Whenever you edit a file in the IDE, Secret Detection is run on that file.

{% hint style="info" icon="pencil" %}
Editing a file triggers new detection after 1 second of inactivity.
{% endhint %}

##### Secret Detection Rules

The following table shows the list of rules that are used to detect various types of secrets.

<details>

<summary>Rules Table</summary>

| Name | Description | Type | Validity Check |
| --- | --- | --- | --- |
| adafruit-api-key | Identified a potential Adafruit API Key, which could lead to unauthorized access to Adafruit services and sensitive data exposure. | api-key | |
| adobe-client-id | Detected a pattern that resembles an Adobe OAuth Web Client ID, posing a risk of compromised Adobe integrations and data breaches. | client-id | |
| adobe-client-secret | Discovered a potential Adobe Client Secret, which, if exposed, could allow unauthorized Adobe service access and data manipulation. | client-secret | |
| age-secret-key | Discovered a potential Age encryption tool secret key, risking data decryption and unauthorized access to sensitive information. | secret-key | |
| airtable-api-key | Uncovered a possible Airtable API Key, potentially compromising database access and leading to data leakage or alteration. | api-key | |
| algolia-api-key | Identified an Algolia API Key, which could result in unauthorized search operations and data exposure on Algolia-managed platforms. | api-key | |
| alibaba-access-key-id | Detected an Alibaba Cloud AccessKey ID, posing a risk of unauthorized cloud resource access and potential data compromise. | access-key,access-id | V |
| alibaba-secret-key | Discovered a potential Alibaba Cloud Secret Key, potentially allowing unauthorized operations and data access within Alibaba Cloud. | secret-key | V |
| anthropic-admin-api-key | Detected an Anthropic Admin API Key, risking unauthorized access to administrative functions and sensitive AI model configurations. | api-key | |
| anthropic-api-key | Identified an Anthropic API Key, which may compromise AI assistant integrations and expose sensitive data to unauthorized access. | api-key | |
| asana-client-id | Discovered a potential Asana Client ID, risking unauthorized access to Asana projects and sensitive task information. | client-id | |
| asana-client-secret | Identified an Asana Client Secret, which could lead to compromised project management integrity and unauthorized access. | client-secret | |
| atlassian-api-token | Detected an Atlassian API token, posing a threat to project management and collaboration tool security and data confidentiality. | api-token | |
| authress-service-client-access-key | Uncovered a possible Authress Service Client Access Key, which may compromise access control services and sensitive data. | access-token | |
| aws-access-token | Identified a pattern that may indicate AWS credentials, risking unauthorized cloud resource access and data breaches on AWS platforms. | access-token | |
| azure-ad-client-secret | Azure AD Client Secret | client-secret | |
| bitbucket-client-id | Discovered a potential Bitbucket Client ID, risking unauthorized repository access and potential codebase exposure. | client-id | |
| bitbucket-client-secret | Discovered a potential Bitbucket Client Secret, posing a risk of compromised code repositories and unauthorized access. | client-secret | |
| bittrex-access-key | Identified a Bittrex Access Key, which could lead to unauthorized access to cryptocurrency trading accounts and financial loss. | access-key | |
| bittrex-secret-key | Detected a Bittrex Secret Key, potentially compromising cryptocurrency transactions and financial security. | secret-key | |
| beamer-api-token | Detected a Beamer API token, potentially compromising content management and exposing sensitive notifications and updates. | api-token | |
| cisco-meraki-api-key | Cisco Meraki is a cloud-managed IT solution that provides networking, security, and device management through an easy-to-use interface. | api-key | |
| codecov-access-token | Found a pattern resembling a Codecov Access Token, posing a risk of unauthorized access to code coverage reports and sensitive data. | access-token | |
| coinbase-access-token | Detected a Coinbase Access Token, posing a risk of unauthorized access to cryptocurrency accounts and financial transactions. | access-token | |
| clickhouse-cloud-api-secret-key | Identified a pattern that may indicate clickhouse cloud API secret key, risking unauthorized clickhouse cloud api access and data breaches on ClickHouse Cloud platforms. | secret-key | |
| clojars-api-token | Uncovered a possible Clojars API token, risking unauthorized access to Clojure libraries and potential code manipulation. | api-token | |
| cloudflare-api-key | Detected a Cloudflare API Key, potentially compromising cloud application deployments and operational security. | api-key | |
| cloudflare-global-api-key | Detected a Cloudflare Global API Key, potentially compromising cloud application deployments and operational security. | api-key | |
| cloudflare-origin-ca-key | Detected a Cloudflare Origin CA Key, potentially compromising cloud application deployments and operational security. | encryption-key | |
| cohere-api-token | Identified a Cohere Token, posing a risk of unauthorized access to AI services and data manipulation. | api-token | |
| confluent-access-token | Identified a Confluent Access Token, which could compromise access to streaming data platforms and sensitive data flow. | access-token | |
| confluent-secret-key | Found a Confluent Secret Key, potentially risking unauthorized operations and data access within Confluent services. | secret-key | |
| contentful-delivery-api-token | Discovered a Contentful delivery API token, posing a risk to content management systems and data integrity. | api-token | |
| curl-auth-user | Discovered a potential basic authorization token provided in a curl command, which could compromise the curl accessed resource. | access-token | |
| curl-auth-header | Discovered a potential authorization token provided in a curl command header, which could compromise the curl accessed resource. | access-token | |
| databricks-api-token | Uncovered a Databricks API token, which may compromise big data analytics platforms and sensitive data processing. | api-token | |
| datadog-access-token | Detected a Datadog Access Token, potentially risking monitoring and analytics data exposure and manipulation. | access-token,client-id | |
| defined-networking-api-token | Identified a Defined Networking API token, which could lead to unauthorized network operations and data breaches. | api-token | |
| digitalocean-pat | Discovered a DigitalOcean Personal Access Token, posing a threat to cloud infrastructure security and data privacy. | access-token | |
| digitalocean-access-token | Found a DigitalOcean OAuth Access Token, risking unauthorized cloud resource access and data compromise. | access-token | |
| digitalocean-refresh-token | Uncovered a DigitalOcean OAuth Refresh Token, which could allow prolonged unauthorized access and resource manipulation. | refresh-token | |
| discord-api-token | Detected a Discord API key, potentially compromising communication channels and user data privacy on Discord. | api-key,api-token | |
| discord-client-id | Identified a Discord client ID, which may lead to unauthorized integrations and data exposure in Discord applications. | client-id | |
| discord-client-secret | Discovered a potential Discord client secret, risking compromised Discord bot integrations and data leaks. | client-secret | |
| doppler-api-token | Discovered a Doppler API token, posing a risk to environment and secrets management security. | api-token | |
| dropbox-api-token | Identified a Dropbox API secret, which could lead to unauthorized file access and data breaches in Dropbox storage. | api-token | |
| dropbox-short-lived-api-token | Discovered a Dropbox short-lived API token, posing a risk of temporary but potentially harmful data access and manipulation. | api-token | |
| dropbox-long-lived-api-token | Found a Dropbox long-lived API token, risking prolonged unauthorized access to cloud storage and sensitive data. | api-token | |
| droneci-access-token | Detected a Droneci Access Token, potentially compromising continuous integration and deployment workflows. | access-token | |
| duffel-api-token | Uncovered a Duffel API token, which may compromise travel platform integrations and sensitive customer data. | api-token | |
| dynatrace-api-token | Detected a Dynatrace API token, potentially risking application performance monitoring and data exposure. | api-token | |
| easypost-api-token | Identified an EasyPost API token, which could lead to unauthorized postal and shipment service access and data exposure. | api-token | |
| easypost-test-api-token | Detected an EasyPost test API token, risking exposure of test environments and potentially sensitive shipment data. | api-token | |
| etsy-access-token | Found an Etsy Access Token, potentially compromising Etsy shop management and customer data. | access-token | |
| facebook-secret | Discovered a Facebook Application secret, posing a risk of unauthorized access to Facebook accounts and personal data exposure. | client-secret | |
| facebook-access-token | Discovered a Facebook Access Token, posing a risk of unauthorized access to Facebook accounts and personal data exposure. | api-token | |
| facebook-page-access-token | Discovered a Facebook Page Access Token, posing a risk of unauthorized access to Facebook accounts and personal data exposure. | access-token | |
| fastly-api-token | Uncovered a Fastly API key, which may compromise CDN and edge cloud services, leading to content delivery and security issues. | api-token,api-key | |
| finicity-client-secret | Identified a Finicity Client Secret, which could lead to compromised financial service integrations and data breaches. | client-secret | |
| finicity-api-token | Detected a Finicity API token, potentially risking financial data access and unauthorized financial operations. | api-token | |
| flickr-access-token | Discovered a Flickr Access Token, posing a risk of unauthorized photo management and potential data leakage. | access-token | |
| finnhub-access-token | Found a Finnhub Access Token, risking unauthorized access to financial market data and analytics. | access-token | |
| flutterwave-public-key | Detected a Finicity Public Key, potentially exposing public cryptographic operations and integrations. | public-key | |
| flutterwave-secret-key | Identified a Flutterwave Secret Key, risking unauthorized financial transactions and data breaches. | secret-key | |
| flutterwave-encryption-key | Uncovered a Flutterwave Encryption Key, which may compromise payment processing and sensitive financial information. | encryption-key | |
| flyio-access-token | Uncovered a Fly.io API key | access-token | |
| frameio-api-token | Found a Frame.io API token, potentially compromising video collaboration and project management. | api-token | |
| freemius-secret-key | Detected a Freemius secret key, potentially exposing sensitive information. | secret-key | |
| freshbooks-access-token | Discovered a Freshbooks Access Token, posing a risk to accounting software access and sensitive financial data exposure. | access-token | |
| gcp-api-key | Uncovered a GCP API key, which could lead to unauthorized access to Google Cloud services and data breaches. | api-key | V |
| generic-api-key | Detected a Generic API Key, potentially exposing access to various services and sensitive operations. | api-key | |
| github-pat | Uncovered a GitHub Personal Access Token, potentially leading to unauthorized repository access and sensitive content exposure. | access-token | V |
| github-fine-grained-pat | Found a GitHub Fine-Grained Personal Access Token, risking unauthorized repository access and code manipulation. | access-token | V |
| github-oauth | Discovered a GitHub OAuth Access Token, posing a risk of compromised GitHub account integrations and data leaks. | access-token | |
| github-app-token | Identified a GitHub App Token, which may compromise GitHub application integrations and source code security. | access-token | |
| github-refresh-token | Detected a GitHub Refresh Token, which could allow prolonged unauthorized access to GitHub services. | refresh-token | |
| gitlab-cicd-job-token | Identified a GitLab CI/CD Job Token, potential access to projects and some APIs on behalf of a user while the CI job is running. | access-token | |
| gitlab-deploy-token | Identified a GitLab Deploy Token, risking access to repositories, packages and containers with write access. | access-token | |
| gitlab-feature-flag-client-token | Identified a GitLab feature flag client token, risks exposing user lists and features flags used by an application. | access-token | |
| gitlab-feed-token | Identified a GitLab feed token, risking exposure of user data. | access-token | |
| gitlab-incoming-mail-token | Identified a GitLab incoming mail token, risking manipulation of data sent by mail. | access-token | |
| gitlab-kubernetes-agent-token | Identified a GitLab Kubernetes Agent token, risking access to repos and registry of projects connected via agent. | access-token | |
| gitlab-oauth-app-secret | Identified a GitLab OIDC Application Secret, risking access to apps using GitLab as authentication provider. | secret-key | |
| gitlab-pat | Identified a GitLab Personal Access Token, risking unauthorized access to GitLab repositories and codebase exposure. | access-token | V |
| gitlab-pat-routable | Identified a GitLab Personal Access Token (routable), risking unauthorized access to GitLab repositories and codebase exposure. | access-token | |
| gitlab-ptt | Found a GitLab Pipeline Trigger Token, potentially compromising continuous integration workflows and project security. | trigger-token | |
| gitlab-rrt | Discovered a GitLab Runner Registration Token, posing a risk to CI/CD pipeline integrity and unauthorized access. | registration-token | |
| gitlab-runner-authentication-token | Discovered a GitLab Runner Authentication Token, posing a risk to CI/CD pipeline integrity and unauthorized access. | access-token | |
| gitlab-runner-authentication-token-routable | Discovered a GitLab Runner Authentication Token (Routable), posing a risk to CI/CD pipeline integrity and unauthorized access. | access-token | |
| gitlab-scim-token | Discovered a GitLab SCIM Token, posing a risk to unauthorized access for a organization or instance. | access-token | |
| gitlab-session-cookie | Discovered a GitLab Session Cookie, posing a risk to unauthorized access to a user account. | access-token | |
| gitter-access-token | Uncovered a Gitter Access Token, which may lead to unauthorized access to chat and communication services. | access-token | |
| gocardless-api-token | Detected a GoCardless API token, potentially risking unauthorized direct debit payment operations and financial data exposure. | api-token | |
| grafana-api-key | Identified a Grafana API key, which could compromise monitoring dashboards and sensitive data analytics. | api-key | |
| grafana-cloud-api-token | Found a Grafana cloud API token, risking unauthorized access to cloud-based monitoring services and data exposure. | api-token | |
| grafana-service-account-token | Discovered a Grafana service account token, posing a risk of compromised monitoring services and data integrity. | access-token | |
| hashicorp-tf-api-token | Uncovered a HashiCorp Terraform user/org API token, which may lead to unauthorized infrastructure management and security breaches. | api-token | |
| hashicorp-tf-password | Identified a HashiCorp Terraform password field, risking unauthorized infrastructure configuration and security breaches. | password | |
| heroku-api-key | Detected a Heroku API Key, potentially compromising cloud application deployments and operational security. | api-key | |
| heroku-api-key-v2 | Detected a Heroku API Key, potentially compromising cloud application deployments and operational security. | api-key | |
| hubspot-api-key | Found a HubSpot API Token, posing a risk to CRM data integrity and unauthorized marketing operations. | api-token,api-key | |
| huggingface-access-token | Discovered a Hugging Face Access token, which could lead to unauthorized access to AI models and sensitive data. | access-token | |
| huggingface-organization-api-token | Uncovered a Hugging Face Organization API token, potentially compromising AI organization accounts and associated data. | api-token | |
| infracost-api-token | Detected an Infracost API Token, risking unauthorized access to cloud cost estimation tools and financial data. | api-token | |
| intercom-api-key | Identified an Intercom API Token, which could compromise customer communication channels and data privacy. | api-token,api-key | |
| intra42-client-secret | Found a Intra42 client secret, which could lead to unauthorized access to the 42School API and sensitive data. | client-secret | |
| jfrog-api-key | Found a JFrog API Key, posing a risk of unauthorized access to software artifact repositories and build pipelines. | api-key | |
| jfrog-identity-token | Discovered a JFrog Identity Token, potentially compromising access to JFrog services and sensitive software artifacts. | access-token | |
| jwt | Uncovered a JSON Web Token, which may lead to unauthorized access to web applications and sensitive user data. | access-token | |
| jwt-base64 | Detected a Base64-encoded JSON Web Token, posing a risk of exposing encoded authentication and data exchange information. | access-token | |
| kraken-access-token | Identified a Kraken Access Token, potentially compromising cryptocurrency trading accounts and financial security. | access-token | |
| kubernetes-secret-yaml | Possible Kubernetes Secret detected, posing a risk of leaking credentials/tokens from your deployments | secret-key | |
| kucoin-access-token | Found a Kucoin Access Token, risking unauthorized access to cryptocurrency exchange services and transactions. | access-token | |
| kucoin-secret-key | Discovered a Kucoin Secret Key, which could lead to compromised cryptocurrency operations and financial data breaches. | secret-key | |
| launchdarkly-access-token | Uncovered a Launchdarkly Access Token, potentially compromising feature flag management and application functionality. | access-token | |
| linear-api-key | Detected a Linear API Token, posing a risk to project management tools and sensitive task data. | api-token,api-key | |
| linear-client-secret | Identified a Linear Client Secret, which may compromise secure integrations and sensitive project management data. | client-secret | |
| linkedin-client-id | Found a LinkedIn Client ID, risking unauthorized access to LinkedIn integrations and professional data exposure. | client-id | |
| linkedin-client-secret | Discovered a LinkedIn Client secret, potentially compromising LinkedIn application integrations and user data. | client-secret | |
| lob-api-key | Uncovered a Lob API Key, which could lead to unauthorized access to mailing and address verification services. | api-key | |
| lob-pub-api-key | Detected a Lob Publishable API Key, posing a risk of exposing mail and print service integrations. | api-key | |
| mailchimp-api-key | Identified a Mailchimp API key, potentially compromising email marketing campaigns and subscriber data. | api-key | |
| mailgun-pub-key | Discovered a Mailgun public validation key, which could expose email verification processes and associated data. | public-key | |
| mailgun-private-api-token | Found a Mailgun private API token, risking unauthorized email service operations and data breaches. | private-key | |
| mailgun-signing-key | Uncovered a Mailgun webhook signing key, potentially compromising email automation and data integrity. | api-key | |
| mapbox-api-token | Detected a MapBox API token, posing a risk to geospatial services and sensitive location data exposure. | api-token | |
| mattermost-access-token | Identified a Mattermost Access Token, which may compromise team communication channels and data privacy. | access-token | |
| maxmind-license-key | Discovered a potential MaxMind license key. | api-key | |
| messagebird-api-token | Found a MessageBird API token, risking unauthorized access to communication platforms and message data. | api-token | |
| messagebird-client-id | Discovered a MessageBird client ID, potentially compromising API integrations and sensitive communication data. | client-id | |
| netlify-access-token | Detected a Netlify Access Token, potentially compromising web hosting services and site management. | access-token | |
| new-relic-user-api-key | Discovered a New Relic user API Key, which could lead to compromised application insights and performance monitoring. | api-key | |
| new-relic-user-api-id | Found a New Relic user API ID, posing a risk to application monitoring services and data integrity. | access-id | |
| new-relic-browser-api-token | Identified a New Relic ingest browser API token, risking unauthorized access to application performance data and analytics. | api-token | |
| new-relic-insert-key | Discovered a New Relic insight insert key, compromising data injection into the platform. | api-key | |
| notion-api-token | Notion API token | api-token | |
| npm-access-token | Uncovered an npm access token, potentially compromising package management and code repository access. | access-token | |
| nuget-config-password | Identified a password within a Nuget config file, potentially compromising package management access. | password | |
| nytimes-access-token | Detected a Nytimes Access Token, risking unauthorized access to New York Times APIs and content services. | access-token | |
| octopus-deploy-api-key | Discovered a potential Octopus Deploy API key, risking application deployments and operational security. | api-key | |
| okta-access-token | Identified an Okta Access Token, which may compromise identity management services and user authentication data. | access-token | |
| 1Password-Secret-Key | Uncovered a possible 1Password secret key, potentially compromising access to secrets in vaults. | private-key | |
| 1Password-Service-Account-Token | Uncovered a possible 1Password service account token, potentially compromising access to secrets in vaults. | access-token | |
| openai-api-key | Found an OpenAI API Key, posing a risk of unauthorized access to AI services and data manipulation. | api-key | |
| Openshift-User-Token | Found an OpenShift user token, potentially compromising an OpenShift/Kubernetes cluster. | access-token | |
| Perplexity-Api-Key | Detected a Perplexity API key, which could lead to unauthorized access to Perplexity AI services and data exposure. | api-key | |
| plaid-client-id | Uncovered a Plaid Client ID, which could lead to unauthorized financial service integrations and data breaches. | client-id | |
| Plaid-Secret-Key | Detected a Plaid Secret key, risking unauthorized access to financial accounts and sensitive transaction data. | secret-key | |
| Plaid-Api-Token | Discovered a Plaid API Token, potentially compromising financial data aggregation and banking services. | api-token | |
| planetscale-password | Discovered a PlanetScale password, which could lead to unauthorized database operations and data breaches. | password | |
| planetscale-api-token | Identified a PlanetScale API token, potentially compromising database management and operations. | api-token | |
| planetscale-oauth-token | Found a PlanetScale OAuth token, posing a risk to database access control and sensitive data integrity. | access-token | |
| postman-api-token | Uncovered a Postman API token, potentially compromising API testing and development workflows. | api-token | |
| prefect-api-token | Detected a Prefect API token, risking unauthorized access to workflow management and automation services. | api-token | |
| private-key | Identified a Private Key, which may compromise cryptographic security and sensitive data encryption. | private-key | |
| pulumi-api-token | Found a Pulumi API token, posing a risk to infrastructure as code services and cloud resource management. | api-token | |
| pypi-upload-token | Discovered a PyPI upload token, potentially compromising Python package distribution and repository integrity. | upload-token | |
| rapidapi-access-token | Uncovered a RapidAPI Access Token, which could lead to unauthorized access to various APIs and data services. | access-token | |
| readme-api-token | Detected a Readme API token, risking unauthorized documentation management and content exposure. | api-token | |
| rubygems-api-token | Identified a Rubygem API token, potentially compromising Ruby library distribution and package management. | api-token | |
| Scalingo-Api-Token | Found a Scalingo API token, posing a risk to cloud platform services and application deployment security. | api-token | |
| sendbird-access-id | Discovered a Sendbird Access ID, which could compromise chat and messaging platform integrations. | access-id | |
| sendbird-access-token | Uncovered a Sendbird Access Token, potentially risking unauthorized access to communication services and user data. | access-token | |
| sendgrid-api-token | Detected a SendGrid API token, posing a risk of unauthorized email service operations and data exposure. | api-token | |
| sendinblue-api-token | Identified a Sendinblue API token, which may compromise email marketing services and subscriber data privacy. | api-token | |
| sentry-access-token | Found a Sentry Access Token, risking unauthorized access to error tracking services and sensitive application data. | access-token | |
| sentry-org-token | Found a Sentry.io Organization Token, risking unauthorized access to error tracking services and sensitive application data. | access-token | |
| sentry-user-token | Found a Sentry.io User Token, risking unauthorized access to error tracking services and sensitive application data. | access-token | |
| Settlemint-Application-Access-Token | Found a Settlemint Application Access Token. | access-token | |
| Settlemint-Personal-Access-Token | Found a Settlemint Personal Access Token. | access-token | |
| Settlemint-Service-Access-Token | Found a Settlemint Service Access Token. | access-token | |
| shippo-api-token | Discovered a Shippo API token, potentially compromising shipping services and customer order data. | api-token | |
| shopify-access-token | Uncovered a Shopify access token, which could lead to unauthorized e-commerce platform access and data breaches. | access-token | |
| shopify-custom-access-token | Detected a Shopify custom access token, potentially compromising custom app integrations and e-commerce data security. | access-token | |
| shopify-private-app-access-token | Identified a Shopify private app access token, risking unauthorized access to private app data and store operations. | access-token | |
| shopify-shared-secret | Found a Shopify shared secret, posing a risk to application authentication and e-commerce platform security. | public-secret | |
| sidekiq-secret | Discovered a Sidekiq Secret, which could lead to compromised background job processing and application data breaches. | secret-key | |
| sidekiq-sensitive-url | Uncovered a Sidekiq Sensitive URL, potentially exposing internal job queues and sensitive operation details. | sensitive-url | |
| slack-bot-token | Identified a Slack Bot token, which may compromise bot integrations and communication channel security. | access-token | |
| slack-app-token | Detected a Slack App-level token, risking unauthorized access to Slack applications and workspace data. | access-token | |
| slack-legacy-token | Detected a Slack Legacy token, risking unauthorized access to older Slack integrations and user data. | access-token | |
| slack-user-token | Found a Slack User token, posing a risk of unauthorized user impersonation and data access within Slack workspaces. | access-token | |
| slack-config-access-token | Found a Slack Configuration access token, posing a risk to workspace configuration and sensitive data access. | access-token | |
| slack-config-refresh-token | Discovered a Slack Configuration refresh token, potentially allowing prolonged unauthorized access to configuration settings. | refresh-token | |
| slack-legacy-bot-token | Uncovered a Slack Legacy bot token, which could lead to compromised legacy bot operations and data exposure. | access-token | |
| slack-legacy-workspace-token | Identified a Slack Legacy Workspace token, potentially compromising access to workspace data and legacy features. | access-token | |
| slack-webhook-url | Discovered a Slack Webhook, which could lead to unauthorized message posting and data leakage in Slack channels. | webhook | |
| stripe-access-token | Found a Stripe Access Token, posing a risk to payment processing services and sensitive financial data. | access-token | |
| square-access-token | Detected a Square Access Token, risking unauthorized payment processing and financial transaction exposure. | access-token | |
| squarespace-access-token | Identified a Squarespace Access Token, which may compromise website management and content control on Squarespace. | access-token | |
| sumologic-access-id | Discovered a SumoLogic Access ID, potentially compromising log management services and data analytics integrity. | access-id | |
| sumologic-access-token | Uncovered a SumoLogic Access Token, which could lead to unauthorized access to log data and analytics insights. | access-token | |
| snyk-api-token | Uncovered a Snyk API token, potentially compromising software vulnerability scanning and code security. | api-key | |
| microsoft-teams-webhook | Uncovered a Microsoft Teams Webhook, which could lead to unauthorized access to team collaboration tools and data leaks. | webhook | |
| telegram-bot-api-token | Detected a Telegram Bot API Token, risking unauthorized bot operations and message interception on Telegram. | api-token | |
| travisci-access-token | Identified a Travis CI Access Token, potentially compromising continuous integration services and codebase security. | access-token | |
| twilio-api-key | Found a Twilio API Key, posing a risk to communication services and sensitive customer interaction data. | api-key | |
| twitch-api-token | Discovered a Twitch API token, which could compromise streaming services and account integrations. | api-token | |
| twitter-api-key | Identified a Twitter API Key, which may compromise Twitter application integrations and user data security. | api-key | |
| twitter-api-secret | Found a Twitter API Secret, risking the security of Twitter app integrations and sensitive data access. | api-key | |
| twitter-access-token | Detected a Twitter Access Token, posing a risk of unauthorized account operations and social media data exposure. | access-token | |
| twitter-access-secret | Uncovered a Twitter Access Secret, potentially risking unauthorized Twitter integrations and data breaches. | public-secret | |
| twitter-bearer-token | Discovered a Twitter Bearer Token, potentially compromising API access and data retrieval from Twitter. | api-token | |
| typeform-api-token | Uncovered a Typeform API token, which could lead to unauthorized survey management and data collection. | api-token | |
| vault-batch-token | Detected a Vault Batch Token, risking unauthorized access to secret management services and sensitive data. | api-token | |
| vault-service-token | Identified a Vault Service Token, potentially compromising infrastructure security and access to sensitive credentials. | api-token | |
| yandex-api-key | Discovered a Yandex API Key, which could lead to unauthorized access to Yandex services and data manipulation. | api-key | |
| yandex-aws-access-token | Uncovered a Yandex AWS Access Token, potentially compromising cloud resource access and data security on Yandex Cloud. | access-token | |
| yandex-access-token | Found a Yandex Access Token, posing a risk to Yandex service integrations and user data privacy. | access-token | |
| zendesk-secret-key | Detected a Zendesk Secret Key, risking unauthorized access to customer support services and sensitive ticketing data. | secret-key | |
| authenticated-url | Identify username:password inside URLS | sensitive-url | |

</details>

{% hint style="info" %}
If you need to customize or extend secret scanning beyond the default rules, use the [Secret Detection Query Editor](/document/preview/517070#UUID-56eab598-46ed-8992-4749-a16ab74c0863).
{% endhint %}

### Checkmarx Dev Assist Agentic-AI Remediation

When the user initiates a remediation action for a risk, a session is opened with the IDE's AI assistant (GitHub Copilot for VS Code or the local AI in Cursor). Checkmarx gathers all relevant data about the risk and submits it to the AI assistant. For supported risk types, the AI assistant sends a request to our MCP which applies the relevant tools and returns a response with suggested remediation steps. The AI assistant implements the changes and offers the user the option to accept the changes or continue a chat session to refine the remediation.

{% hint style="info" icon="pencil" %}
If for some reason the Checkmarx MCP connection is unavailable, the remediation agent automatically falls back to the IDE's LLM to provide remediation suggestions. In this case, a notification is displayed indicating that the recommendations are not based on Checkmarx's specialized security models.
{% endhint %}

In addition, this tool enables use of AI to better understand the precise nature of a risk in the context of your code.

#### Remediating Vulnerable or Malicious Images and Packages

Remediation for OSS and Container risks is done by identifying the best non-vulnerable package that provides the same functionality as the vulnerable package. When our proprietary databases indicate that a remediated version of the current package is available, the remediated version that is closest to the current version is used. When no remediated version is available, our MCP server uses a dedicated AI tool to identify alternative packages that provide equivalent functionality.

{% hint style="info" icon="pencil" %}
Our MCP tool for identifying non-vulnerable versions is supported both for OSS and Containers. However, the MCP tool for finding **alternative** packages is not supported for containers.
{% endhint %}

When Checkmarx Dev Assist recommends updating a package version, our **Safe Refactor** feature searches your entire project for additional usage of that package and determines where and how the code needs to be refactored to accommodate the package update.

##### Remediation Logic

The following tables describe the logic of the remediation response for various cases.

{% hint style="info" icon="pencil" %}
When suggesting a non-vulnerable version or a more secure version, the MCP always recommends the smallest effective upgrade, rather than jumping to a higher version.
{% endhint %}

<details>

<summary>Vulnerable Packages</summary>

| Case | Response |
| --- | --- |
| Package has non-vulnerable version | Secure version of the same package. Suggest that the user apply changes and help with fixing code if there were breaking changes. |
| Package has no completely non-vulnerable version, but has a more secure one and Checkmarx has alternative package suggestions | Suggest the most secure version of the same package; List alternative packages |
| Package has no non-vulnerable version, and no more secure version, and Checkmarx has alternative package suggestions | List alternative packages |
| Package has no completely non-vulnerable version, but has a more secure one, and Checkmarx does not have alternative package suggestions | Suggest the most secure version of the same package; Offer user if they want to run a web search, with a warning that it's their own responsibility to check the security and relevance of the results. |
| Package has no non-vulnerable version, and no more secure version, and Checkmarx does not have alternative package suggestions | Offer user if they want to run a web search, with a warning that it's their own responsibility to check the security and relevance of the results. |

</details>

<details>

<summary>Malicious Packages</summary>

| Case | Response |
| --- | --- |
| Package has non-vulnerable and non-malicious version | Secure version of the same package. Suggest that the user apply changes and help with fixing code if there were breaking changes. |
| Package has non-malicious but vulnerable version | Suggest the most secure version of the same package; List alternative packages |
| Package has no non-malicious version, and Checkmarx has alternative package suggestions | List alternative packages |
| Package has no non-malicious version, and Checkmarx does not have alternative package suggestions | Offer user if they want to run a web search, with a warning that it's their own responsibility to check the security and relevance of the results. |

</details>

#### Remediating Exposed Secrets

Remediation is done by removing the hard coded secret from the code and replacing it with an Environment Variable that can be used to store the secret in a secure manner.

#### Remediating ASCA and IaC Vulnerabilities

For vulnerabilities in your code that were identified by the ASCA or IaC Realtime scanners, remediation is done by sending a customized prompt including all relevant data about the vulnerability instance to your IDEs AI assistant (Copilot or Cursor). The AI assistant then provides a remediated snippet that can be used in your code.
