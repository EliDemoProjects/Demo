# SCA Risk Severity Levels

## Severity Level for Risks

Checkmarx SCA assigns a severity level to each risk. The severity level represents the degree of threat posed by this risk. Possible values for severity level are:

- **HIGH**
- **MEDIUM**
- **LOW**

{% hint style="warning" %}
There are other factors that contribute to the urgency of remediating a vulnerability that are not reflected in the severity score, such as the degree of exploitability. You should consider all relevant factors when triaging results, see [Remediating SCA Risks](remediating-sca-risks.md).
{% endhint %}

### Severity Level by Risk Category

For **Vulnerabilities**, the severity level is determined primarily based on the CVSS score of the vulnerability in the National Vulnerability Database (NVD).. If a vulnerability has a CVSS v4.0  score, that score is used; if it only has an score in NVD (v3.1 or lower), that score is used. Checkmarx SCA maps out the CVSS scores to Severity Levels as follows:

- **HIGH** - 7.0-10.0
- **MEDIUM** - 4.0-6.9
- **LOW** - 0.0-3.9

{% hint style="info" icon="pencil" %}
Although NVD has a separate category, CRITICAL, for vulnerabilities with severity 9.0 - 10.0, Checkmarx SCA currently includes these in the HIGH category.
{% endhint %}

For **Suspected Malware**, the severity level is derived from the risk score (which is designated by Checkmarx based on the assessment of our AppSec research team) using the same scale as for Vulnerabilities.

For **Legal Risks**, the severity level is derived from the Copyright Risk Score, with **HIGH** for level 6-10, **MEDIUM** for 4-5, and **LOW** for 1-3.

## Package Risk Level

Checkmarx SCA assigns an overall **Risk Level** to each package. The risk level of a package is equal to the severity level of the highest severity risk existing in the package.
