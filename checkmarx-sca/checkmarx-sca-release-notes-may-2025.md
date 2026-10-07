# Checkmarx SCA Release Notes May 2025

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

## SCA Updates

### Added Licenses to SCA Global Inventory

We have added a new tab, Licenses, to the SCA Global Inventory. This tab shows all relevant licenses for packages consumed in all of the tenant's projects. The data from this table can be exported as a .csv file.

This will greatly improve visibility of licenses on a tenant-wide level.

### Improvements in the Scan Results - Risks Tab

We have added the following improvements to the Scan Results - Risks tab:

- Added the Secure Version column, indicating whether or not a remediated version of the package is available. You can sort and filter for this column.

- The [EPSS](https://www.first.org/epss/) score is now shown in a separate column (not under Exploitability). You can now sort and filter for EPSS.

  {% hint style="info" %}
  These changes are similar to the changes made in the Global Inventory in March.
  {% endhint %}

## SCA Resolver

Download the latest version [here](checkmarx-sca-resolver-changelog.md).

### Version 2.12.23 (May 6, 2025)

- For Nuget, added support for .NET 9.
