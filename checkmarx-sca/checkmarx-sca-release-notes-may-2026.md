# Checkmarx SCA Release Notes May 2026

{% include ".gitbook/includes/note-031596ef.md" %}

## SCA Updates

### Package Upgrade Recommendations

We have introduced Package Upgrade Recommendations, based on our proprietary algorithms, in the **Project Page** of each project. This provides actionable guidance to help you identify and prioritize safer dependency upgrades.

A new **Suggested Fix** column in the **Packages** tab highlights what upgrade options are available for each package (None, Next, Latest), with color-coded indicators distinguishing between full (green) and partial (purple) remediation. Hover over a value to see additional details and click on the value to open a sidebar that shows both the minimal update and the latest version that offer the best remediation options. There is also a link to the AppSec Knowledge Center where you can see a full analysis of the vulnerable package. In the **Risks** tab, a new **Risk Resolution** column delivers targeted fix recommendations per vulnerability, enabling more granular remediation decisions.

Aside from the scan results viewer, these insights are also available on the **Global Inventory** screen as well as in the exported CSV files.

These recommendations reduce the time and effort required to remediate open-source vulnerabilities, helping teams make faster, more informed upgrade decisions.

## Improved Delta Scan Accuracy

The **Delta Scan** feature in SCA has been updated to better determine when a full scan is required. The set of monitored files per package manager has been expanded, and scan arguments and platform configurations are now factored into the delta evaluation - ensuring that relevant changes always trigger a full scan and produce accurate results.
