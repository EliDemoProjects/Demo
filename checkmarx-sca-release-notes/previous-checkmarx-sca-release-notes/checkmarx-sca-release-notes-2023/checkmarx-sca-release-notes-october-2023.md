# Checkmarx SCA Release Notes October 2023

{% include "../../../.gitbook/includes/note-031596ef.md" %}

{% include "../../../.gitbook/includes/warning-d19d3540.md" %}

## Sysdig Integration

We have implemented a new integration with Sysdig for identifying runtime usage of container packages. This provides important insights for prioritizing remediation activities.

Once the integration has been configured for your account, you will see a new column Runtime Usage in the Containers Packages tab indicating which packages are used in runtime. In addition, in the Containers Vulnerabilities tab, runtime usage will be shown as a Risk Factor for specific vulnerabilities.

{% hint style="info" icon="pencil" %}
This integration is only available for accounts that have a Sysdig license. To set up the integration, please contact your account manager and provide them with your Sysdig Risk Spotlight token.
{% endhint %}

## Exploitable Path Queries

We improved the performance of Exploitable Path scans for Java projects. The updated queries yield more complete results while cutting the scan time by as much as half.

## SCA Resolver Version 2.4.8

We released a new version of SCA Resolver with the following improvements:

* For Yarn, scripts that are defined on package.json are now ignored.
* For Swift, lock file version 2 is now supported.

Download the new version [here](../../../checkmarx-sca-resolver/checkmarx-sca-resolver-changelog.md).
