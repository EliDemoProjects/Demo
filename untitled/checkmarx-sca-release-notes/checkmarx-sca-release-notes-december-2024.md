# Checkmarx SCA Release Notes December 2024

{% include "../.gitbook/includes/note-031596ef.md" %}

{% include "../.gitbook/includes/warning-d19d3540.md" %}

## Support for CVSS 4.0

We have added support for the [CVSS 4.0](https://nvd.nist.gov/vuln-metrics/cvss/v4-calculator) scoring system, which uses additional metrics to provide better granularity and further refine the scoring methodology. We now show the CVSS 4.0 score for each vulnerability that has such a score. When no CVSS 4.0 score is available, we continue to use the most recent available score from previous scoring systems (3.1 or 2.0).

## SCA Resolver Releases

### Version 2.12.3 (Dec 12, 2024)

* Improved logging for the project creation process
* Fixed issue with manifest file upload on Windows operating systems
* Fixed issue with certificate expiration for Windows binary digital signing
* For Nuget, improved package version resolution for `Directory.Packages.props` and `Directory.Build.props` files.

Download the latest version [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).
