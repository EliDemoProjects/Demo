# Checkmarx SCA Integrations and Plugins

Checkmarx SCA offers a robust set of integrations that help you to get the most out of SCA’s capabilities.

Checkmarx SCA, can be integrated into development tools, so that open source packages can be automatically scanned during the development process. For example, the Checkmarx Plugin for Jenkins enables SCA scanning to be configured as part of the build step, so that if vulnerabilities are discovered the build process can be terminated.

The Checkmarx Plugins provide software composition analysis based only on the manifest files and fingerprints. This analysis involves compressing and sending only the manifest files, configuration files, file names, and fingerprint data to the Checkmarx SCA cloud. The source code is not sent to the cloud.

In addition to the tools that we offer for integration with your Checkmarx SCA account, we also offer several free plugins the enable any user to integrate SCA analysis into their development workflows.

{% hint style="warning" %}
This page relates only to integrations for SCA standalone accounts and free SCA tools. For Checkmarx One accounts that use the SCA scanner, integration info is available [here](../../document/preview/68614/#UUID-c898951d-fa80-c7c3-f4a1-f349c334f8ce).
{% endhint %}

{% include ".gitbook/includes/warning-e25f6b2c (1).md" %}

## SCA Standalone Accounts

| Platform(Documentation links)                                                                 | Comments                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CLI Plugin](../../document/preview/8149/#UUID-929c3f4a-dabe-6247-b44e-7a87d9a52f46)          |                                                                                                                                                                                                                                                                 |
| [CxFlow](https://github.com/checkmarx-ltd/cx-flow/wiki/CxSCA-Integration)                     |                                                                                                                                                                                                                                                                 |
| [Jenkins Plugin](../../document/preview/8155/#UUID-022ffa42-2bca-259b-2c29-70dc3f72c033)      | Supports integration with Checkmarx SCA Resolver, see [Configuring the Jenkins Plugin for Scanning](../../document/preview/8157/#UUID-4f3bc676-dae6-9685-acd1-f131d4f3b4f3_id_InstallingandConfiguringtheJenkinsPlugin-ConfiguringtheJenkinsPluginforScanning). |
| [Azure DevOps Plugin](../../document/preview/8186/#UUID-baffdf29-b960-2e2b-dc38-ef5c759df250) | Supports integration with Checkmarx SCA Resolver, see “Adding a Checkmarx SCA Scan Project” in [Running a Scan from Azure DevOps](../../document/preview/8190/#UUID-26d4e2d4-da3f-f72c-4042-c459c95300bc).                                                      |
| [TeamCity Plugin](../../document/preview/8180/#UUID-57aa3a09-2280-4db8-e5e2-066461d61a91)     |                                                                                                                                                                                                                                                                 |
| [Bamboo Plugin](../../document/preview/8172/#UUID-f2bbf798-1a91-8685-ebca-ae767f5cb881)       |                                                                                                                                                                                                                                                                 |

## Free Tools

| Platform(Documentation links)                                                                                 | Comments                                                                                                               |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [Docker Desktop Extension](checkmarx-docker-desktop-extension.md)                                             | <p>Free tool, no Checkmarx SCA account required.<br>For Checkmarx SCA users, data does not sync with your account.</p> |
| JFrog Plugin                                                                                                  | <p>Free tool, no Checkmarx SCA account required.<br>For Checkmarx SCA users, data does not sync with your account.</p> |
| Nexus Plugin                                                                                                  | <p>Free tool, no Checkmarx SCA account required.<br>For Checkmarx SCA users, data does not sync with your account.</p> |
| [VS Code Plugin - Realtime Scanner](../../document/preview/152268/#UUID-4f8d5acd-3566-3bc2-7144-6ff451ede6df) | <p>Free tool, no Checkmarx SCA account required.<br>For Checkmarx SCA users, data does not sync with your account.</p> |
