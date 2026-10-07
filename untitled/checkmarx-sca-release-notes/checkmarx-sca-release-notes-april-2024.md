# Checkmarx SCA Release Notes April 2024

{% include ".gitbook/includes/note-031596ef (1).md" %}

{% hint style="warning" %}
The **IgnoreVulnerability** and **UnignoreVulnerability** APIs, which had been used for triaging SCA vulnerabilities, will be deprecated on July 7. They have been replaced by the new [Management of Risk](https://app.gitbook.com/s/XSPACE_REST_API/checkmarx-sca--rest--api---management-of-risk) API, which supports applying the new set of states and adding comments. We recommend migrating to the new API well in advance of the July 7 deadline.
{% endhint %}

{% include ".gitbook/includes/caution-f72202af (1).md" %}

## Showing EPSS Score

We now show the [EPSS](https://www.first.org/epss/) (Exploit Prediction Scoring System) scores provided by [First](https://www.first.org/) for vulnerabilities. This score is a data-driven estimate of the likelihood that this vulnerability is being exploited. It is a dynamic score that changes over time based on identified exploitation activity and various other factors. The score is presented as a percentage (indicating the likelihood of the vulnerability being exploited within the next 30 days), and also as a percentile (indicating the ranking of this risk relative to other vulnerabilities).

EPSS scores are shown on the scan results screens for SCA vulnerabilities.

In addition, EPSS score is shown in the AppSec Knowledge Center vulnerability data.

## Detection Date

In the Scan Results > Risks tab, we now show the "Detection" date. This is the date that the vulnerability was first identified in the project that you are viewing. For vulnerabilities that were first identified in the scan that you are viewing, the NEW label is shown next to the date. You can alternate between showing the "Publication" date and the "Detection" date by clicking on the column header.

## Legal Risk

We fundamentally changed the way that we handle legal risks. Instead of listing all Licenses in the Vulnerabilities > Legal Risk section, we now show a separate tab with a list of all licenses identified in the project. In the Vulnerabilities > Legal Risk section, we now show only the following types of legal risks:

* Risky effective license - A license with medium or high severity License Score is marked as Effective for this package.
* Package with no effective license - There is an open source package in your project for which no license has been marked as Effective.
* Package with no license - Checkmarx didn't identify any licenses associated with this package.

## Support for Perl

Added support for Perl using cpan package manager.

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Perl</strong></td><td></td><td colspan="2"><p><strong>Languages/Frameworks:</strong> Perl</p><p><strong>Repository:</strong> <a href="https://www.cpan.org/">Cpan</a></p><p><strong>File Types:</strong> none</p></td></tr><tr><td><strong>Supported Package Managers</strong></td><td><strong>Exploitable Path</strong></td><td><strong>Supply Chain Security (SCS)</strong></td><td><strong>Manifest Files</strong> (Packages marked with are required)</td></tr><tr><td>Cpan</td><td></td><td></td><td><code>cpanfile</code>, <code>spcanfile.snapshot</code></td></tr></tbody></table>

## SCA Resolver Version 2.7.2 (Apr 18, 2024)

* Added support for extracting .gz archives that contain .tar folder using the `--extract-archives` flag.

Download the new version [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).
