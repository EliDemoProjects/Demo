# Checkmarx SCA Release Notes January 2024

{% include ".gitbook/includes/note-031596ef (1).md" %}

{% include ".gitbook/includes/warning-d19d3540 (1).md" %}

{% hint style="warning" %}
For the SCA JFrog plugin, version 1.1.9 and below will stop working on Feb. 29. To continue using this plugin, make sure to upgrade to version [1.1.10](../../document/preview/120938/#UUID-fc6b0d9b-d71b-6dd3-6da0-92ac5a79b379_id_CheckmarxSCAPluginforJFrog-DownloadLinks) before that date.

For the SCA Nexus plugin, version 1.1.5 and below will stop working on Feb. 29. To continue using this plugin, make sure to upgrade to version [1.1.6](../../document/preview/127324/#UUID-a1dd9aaf-156a-43bf-dc1c-0cbe92571db5_id_CheckmarxSCAPluginforJFrog-DownloadLinks) before that date.
{% endhint %}

## Improvements and Bug Fixes

| Status | Item                       | Description                                                                                                                                 |
| ------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| UPDATE |                            |                                                                                                                                             |
| FIXED  | Link from All Packages tab | Clicking on the Vulnerabilities widget on a Scan Results > Package Details page now opens the Risks tab, filtered for the specific package. |

## SCA Resolver Version 2.5.15

We released a new version of SCA Resolver with the following improvements:

* For Gradle, the processing of wildcards on Gradle multi-module scans has been improved.
* For Python, pip is no longer presented as a dependency for all Python projects.

Download the new version [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).
