# Checkmarx SCA Release Notes March 2024

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

{% hint style="warning" %}
For the SCA JFrog plugin, version 1.1.9 and below are no longer supported. To continue using this plugin, make sure to upgrade to version 1.1.10.

For the SCA Nexus plugin, version 1.1.5 and below are no longer supported. To continue using this plugin, make sure to upgrade to version 1.1.6.
{% endhint %}

## Risk Management

We have improved the handling of Risk Management for vulnerabilities identified by Checkmarx SCA. You can now change the state of all SCA vulnerabilities and Supply Chain risks to any of the following states: To Verify (default), Not Exploitable, Proposed Not Exploitable, Confirmed or Urgent. Whenever you make a state change you are required to add a comment explaining the rationale behind the change. In addition, there is an option to add a comment without making a state change.

When a state change is made, a red dot next to the Risks tab indicates the need for a recalculation in order to update the risk counters to reflect the changes. State changes are automatically applied to the identical risk if it is identified in subsequent scans of that project.

## Support for VB.NET

We expanded our support for Nuget package manager to include VB.NET projects that use `*.vbproj` manifest files.

## SCA Resolver Version 2.6.9 (Mar 21, 2024)

- For Gradle,

  - Fixed exception during project detection
  - Fixed issue that scans were being duplicated

Download the new version [here](checkmarx-sca-resolver-changelog.md).
