# Checkmarx SCA Release Notes December 2025

{% include ".gitbook/includes/note-031596ef.md" %}

## SCA Updates

### New Automated Process to Add CVEs Quickly

In order to speed up the process of adding newly identified CVEs to our database, we have introduced a new automated process that identifies and publishes CVEs in a timely manner. However, this does not replace the need for our AppSec Research team to thoroughly analyze each CVE. Therefore, when the initial automated results are available, we publish the CVE with a note indicating that it is "pending manual review”. Once our AppSec team has completed their manual analysis they publish an updated version of the CVE details in which they correct any imprecise information and add important remarks about their analysis.

### Highlighting AppSec Team Remarks

Our AppSec Research team often adds remarks based on their expert analysis. These remarks give important information about exploitability and remediation options. We now highlight these comments by showing them in a separate info box both in the scan results **Risk Details** page and in our **AppSec Knowledge Center**.

### Added Suspected Malware Risks to AppSec Knowledge Center

You can now view Suspected Malware risk information in the AppSec Knowledge Center. It is presented similarly to vulnerabilities. This enables users to learn about specific risks without needing to scan a project with the risky package.

### Support for package.lock.json

For .NET projects, we added support for scanning `packages.lock.json` files.

### Additional Package Data in SCA Reports

We added new fields that provide additional information about the packages used in your project. This will help organizations meet regulatory requirements and improve the transparency and security of their software supply chain.

The **Packages** section of Checkmarx SCA reports now includes **Component Description**, **Component Supplier** and **Executable Properties** fields. And, SBOM reports (CycloneDX and SPDX) now include the **Component Description** field.
