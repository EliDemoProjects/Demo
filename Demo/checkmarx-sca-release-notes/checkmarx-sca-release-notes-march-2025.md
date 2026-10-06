# Checkmarx SCA Release Notes March 2025

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

## SCA Updates

### Global Inventory Improvements

We added the following functionality to the **Vulnerabilities and Malware** tab of the **Global Inventory & Risks**.

- Added the “Secure Version” column, indicating whether or not a remediated version of the package is available. You can sort and filter for this column.
- The [EPSS](https://www.first.org/epss/) score is now shown in a separate column (not under Exploitability). You can now sort and filter for EPSS.

## SCA Resolver

Download the latest version [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).

### Version 2.12.14 (Mar 25, 2025)

- Improved the export process for risk reports.
- For SwiftPM, added support for version 3 of lock file `package.resolved`.

### Version 2.12.11 (Mar 18, 2025)

- For Nuget, fixed resolution for projects that include private packages.
