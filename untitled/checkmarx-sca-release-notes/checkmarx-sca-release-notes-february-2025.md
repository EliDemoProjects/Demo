# Checkmarx SCA Release Notes February 2025

{% include "../.gitbook/includes/note-031596ef.md" %}

{% include "../.gitbook/includes/warning-d19d3540.md" %}

## SCA Updates

### Support for CVSS 4.0

We have added support for the [CVSS 4.0](https://nvd.nist.gov/vuln-metrics/cvss/v4-calculator) scoring system, which uses additional metrics to provide better granularity and further refine the scoring methodology. We now show the CVSS 4.0 score for each vulnerability that has such a score. When no CVSS 4.0 score is available, we continue to use the most recent available score from previous scoring systems (3.1 or 2.0). Additional details about this change are available [here](https://app.gitbook.com/s/XSPACE_USER_GUIDE/viewing-results/viewing-the-project-page/project-page-tabs#UUID-07a21b5d-72d7-69da-9320-fc8d5e505317_UUID-cad2fd15-59dd-521f-444e-cec7678aaa3d).

### New SCA Policy Conditions

We have added several new policy conditions, enabling granular detection of specific risk factors:

* [EPSS](https://www.first.org/epss/) - set thresholds based on EPSS score or EPSS percentile.
* State - set a condition for vulnerabilities in one or more specified states. Options are: To Verify, Proposed not Exploitable, Confirmed and Urgent.
* Malicious Package detection (for accounts with the relevant license) - you can now create conditions based on specific types of malicious attacks (e.g., Typosquatting, Chainjacking etc.). You can also create conditions based on thresholds for the following package integrity metrics: Contributor Reputation, Reliability Score and Behavioral Integrity.
