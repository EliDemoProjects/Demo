# Checkmarx SCA Release Notes June 2024

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

## Remediation Icon

When a remediated version of a package exists, we now show a remediation icon next to the package in the **Packages** tab of the scan results. Clicking on this icon takes you to that item in the **Remediation Tasks** tab.

{% hint style="info" icon="pencil" %}
This feature is only available for direct dependencies.
{% endhint %}

## Improved Remediation Tasks

We have cut out the “noise” in this section by showing recommendations for replacing transitive packages only if the current package has vulnerabilities. For outdated packages without vulnerabilities, we no longer show remediation suggestions.

## Global Inventory & Risks - Data Enrichment

We have enriched the Global Inventory and Risks page to include all relevant data from the SCA scan results page. We have added the following items in the **Packages** and **Risks** tabs respecitvely:

### Packages Tab

- Show only **Effective** licenses
- Added **Scan Date**

### Risks Tab

- Added severity **Score**
- Added risk **State**
- Added **Exploitability** indicators
- Added **Category** (CWE)
- Made **Package Name** and **Package Version** into separate items
- Added **Detection Date**

In addition we have improved filter and search capabilities.
