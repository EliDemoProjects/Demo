# Viewing the Dashboard (Home Page)

The Dashboard shows the overall status of all of your Projects.

- The **Overview** widgets - show aggregated results for all of your organization’s Projects (dependent on access control).
- The **Projects** pane - shows results for each individual Project. Each record shows general Project info and overall results for the most recent scan of that Project. You can click on a Project to open the Project page for that Project.

<div align="left"><figure><img src=".gitbook/assets/img-0737c94c7fd0edc319b16b734eec4db7.png" alt=""></figure></div>

## Overview Widgets

<div align="left"><figure><img src=".gitbook/assets/img-d146d5ad09a818947df9e6be638771f3.png" alt=""></figure></div>

The following table describes the info shown in the overview widgets.

<table>
<thead>
<tr><th><p><strong>Item</strong></p></th><th><p><strong>Description</strong></p></th><th><p><strong>Possible Values</strong></p></th></tr>
</thead>
<tbody>
<tr><td><p><strong>Projects at Risk</strong></p></td><td><p>The total number of Projects at Risk over the total number of Projects in your organization. The number of Projects at risk is color coded to indicate the highest risk level of any of the Projects.</p></td><td><p>e.g., 4/9</p></td></tr>
<tr><td><p><strong>High Risk Projects</strong></p></td><td><p>The total number of Projects with a high risk.</p></td><td><p>e.g., 4</p></td></tr>
<tr><td><p><strong>Medium Risk Projects</strong></p></td><td><p>The total number of Projects with a medium risk.</p></td><td><p>e.g., 0</p></td></tr>
<tr><td><p><strong>Low Risk Projects</strong></p></td><td><p>The total number of Projects with a low risk.</p></td><td><p>e.g., 0</p></td></tr>
<tr><td><p><strong>Total Vulnerabilities</strong></p></td><td><p>The combined total number of vulnerabilities in all of your Projects followed by a color coded bar graph indicating the number of vulnerabilities of each severity level.</p></td><td><p>e.g.,</p><figure><img src=".gitbook/assets/img-e4a0d8881e6c582ee9ca877e6fe2e0fc.png" alt=""></figure></td></tr>
<tr><td colspan="3"><p><strong>Action Button</strong></p></td></tr>
<tr><td><p><strong>Create New Project Button</strong></p></td><td><p>Click on this button to create a new project.</p></td><td><p>-</p></td></tr>
</tbody>
</table>

## Projects Pane

The **Projects** pane shows a list of all Projects in your organization’s account. Each record shows general Project info as well as overall results for the most recent scan of that Project. You can search for specific packages using the search box. You can also sort by column headers and set filters for each column.

You can click on a row to open the **Project** page for that Project.

<div align="left"><figure><img src=".gitbook/assets/img-510706bc39408f4eae499990af51be2c.png" alt=""></figure></div>

The following table describes the info shown in the **Projects** pane and the actions available in the context menu.

<table>
<thead>
<tr><th><p><strong>Item</strong></p></th><th><p><strong>Description</strong></p></th><th><p><strong>Possible Values</strong></p></th></tr>
</thead>
<tbody>
<tr><td><p><strong>Selection Box</strong></p></td><td><p>Select multiple checkboxes to perform bulk action on all selected Projects. A delete button is shown above the Project Name column enabling you to delete all selected Projects.</p></td><td><p>-</p></td></tr>
<tr><td><p><strong>Risk Level</strong></p></td><td><p>The highest risk level of any vulnerability identified in the Project.</p></td><td><p><em><em>High</em></em>, <em><em>Medium</em></em>, <em><em>Low</em></em>, <em><em>Unknown</em></em>, or <em><em>No Risk</em></em></p></td></tr>
<tr><td><p><strong>Project Name</strong></p></td><td><p>The name of the Project.</p></td><td><p>e.g., Test_1</p></td></tr>
<tr><td><p><strong>Violates Policies</strong></p></td><td><p>Indicates if the last scan of this Project triggered any Policy violations, see <a href="policy-management.md">Policy Management</a>.</p></td><td><p><em><em>Yes</em></em> or <em><em>No</em></em></p></td></tr>
<tr><td><p><strong>Direct Dependencies (Total)</strong></p></td><td><p>The number of direct dependencies in the Project, followed by the total number of dependencies in parentheses.</p></td><td><p>e.g., 12 (34)</p></td></tr>
<tr><td><p><strong>Risks (Aggregated)</strong></p></td><td><p>A bar graph showing the number of risks in the project, according to risk level. This includes vulnerabilities, suspected malware risks and legal risks. Hover over a graph to show a breakdown by risk type.</p><ul><li><p><strong>HIGH</strong></p></li><li><p><strong>MEDIUM</strong></p></li><li><p><strong>LOW</strong></p></li><li><p><strong>UNKNOWN</strong> (light grey - relevant only for legal risks)</p></li></ul><p>For more information, see <a href="severity-levels.md">SCA Risk Severity Levels</a></p></td><td><p>e.g.,</p><figure><img src=".gitbook/assets/img-dbb1b4c966e29ba609b4bb741272460c.png" alt=""></figure></td></tr>
<tr><td><p><strong>Team</strong></p></td><td><p>The Teams that are assigned to the Project.</p></td><td><p>e.g., All users, Team01</p></td></tr>
<tr><td><p><strong>Last Scanned/Date</strong></p></td><td><p>The relative time or calendar date that the last scan was performed on your Project. Toggle between relative time and date by clicking “Last Scanned” or “Date” in the column header.</p></td><td><p>e.g., 19 days ago</p><p>e.g., Jan 28, 2021 11:22 AM</p></td></tr>
<tr><td><p><strong>Created/Date</strong></p></td><td><p>The relative time or date that the project was created. Toggle between relative time and date by clicking “Created” or “Date” in the column header.</p></td><td><p>e.g., 19 days ago</p><p>e.g., Jan 28, 2021 11:22 AM</p></td></tr>
<tr><td colspan="3"><p><strong>Context Menu</strong></p></td></tr>
<tr><td><p><strong>Scan Project</strong></p></td><td><p>Run a new scan on the Project.</p></td><td><p>-</p></td></tr>
<tr><td><p><strong>Project Settings</strong></p></td><td><p>Enables you to edit the Project settings as well as to activate/deactivate notifications.</p></td><td><p>-</p></td></tr>
<tr><td><p><strong>Delete Project</strong></p></td><td><p>Delete a Project and associated scans.</p></td><td><p>-</p></td></tr>
<tr><td><p><strong>Latest Scan Results</strong></p></td><td><p>Open the Risk Report page for the most recent scan of the Project.</p></td><td><p>-</p></td></tr>
</tbody>
</table>
