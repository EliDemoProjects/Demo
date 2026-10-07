# Viewing the Global Inventory and Risks Page

The Global Inventory & Risks page displays a comprehensive list of the packages identified in your account as well as the risks associated with those packages. This info includes vulnerabilities, outdated versions, policy violations, etc. By showing info for all Projects, this screen enables you to prioritize remediation of risks and vulnerable packages by seeing which ones are affecting multiple Projects across your organization. It also helps you to coordinate efforts between different development teams.

{% hint style="info" icon="pencil" %}
The info shown on the Global Inventory & Risks page includes packages and risks identified in Projects to which the current user is not assigned. However, users can only open the Scan Results page for items that were identified in Projects to which that user is assigned.
{% endhint %}

<div align="left"><figure><img src=".gitbook/assets/img-8a1016f238edb75450af1fa6b8d58010.png" alt=""></figure></div>

The Global Inventory & Risks page is opened by clicking on the Global Inventory & Risks icon in the left navigation pane on the Dashboard (**Home page)**.

The screen includes three tabs:

- Packages (default) – shows info about all of the packages used in all the Projects in your organization.
- Risks – shows info about all of the vulnerabilities, operational, and legal risks across all the Projects in your organization.
- Licenses - shows info about all of the licenses that are associated with the open source packages used by your projects.

You can customize the report content by specifying which sections to include and applying the sorting and filters of the current display.

## Global Inventory and Risks Page - Packages Tab

The Global Inventory & Risks tab shows detailed info about the packages identified by the scans of all of your Projects. This info includes policy violations, vulnerabilities, outdated versions, etc. The total number of packages is shown in parentheses in the tab title.

{% hint style="info" icon="pencil" %}
If a package is used by multiple Projects, a separate record (row) is shown for each instance.
{% endhint %}

You can search for **Package Name**, **Violates Policies**, **License**, and **Project** using the search box. You can also set filters and sort by several key column headers.

You can export the data on this page as a CSV file. There is an option to export all data or only data shown based on the current filters.

Click on a specific row to open the Package Details page for that package in the Risk Report for the Project. For more information, see [Package Details Page](project-page-tabs.md#UUID-dcde0b63-2db7-9d78-09a4-dcc92d4a8d3d).

{% hint style="info" icon="pencil" %}
You can only open the Package Details page for packages that were identified in Projects which are assigned to your Team.
{% endhint %}

<div align="left"><figure><img src=".gitbook/assets/img-8a1016f238edb75450af1fa6b8d58010.png" alt=""></figure></div>

{% hint style="info" icon="pencil" %}
You may need to scroll horizontally to view all columns.
{% endhint %}

The following table describes the info shown in the Packages tab of the Global Inventory & Risks page.

<table>
<thead>
<tr><th><p><strong><strong>Item</strong></strong></p></th><th><p><strong><strong>Description</strong></strong></p></th><th><p><strong><strong>Possible Values</strong></strong></p></th></tr>
</thead>
<tbody>
<tr><td><p><strong><strong>Package Name</strong></strong></p></td><td><p>The name of a package used in one or more of the Projects in the organization.</p><p>Next to the package name, an icon is shown indicating how the package is used by the Project.</p><p><strong>Tip</strong></p><p>If the package name is used in more than one Project, it will appear on the list multiple times, one time for each Project that uses it.</p></td><td><p>e.g., javax.annotation:javax.annotation-api</p><p><img src=".gitbook/assets/img-5748e8257415871e4d76f4dde7599422.png" alt="" data-size="line"> - <em><em>Direct</em></em> – the package is called directly by your source code </p><p><img src=".gitbook/assets/img-c4d1c0d8a459bc6ce69bb832ff2b0acb.png" alt="" data-size="line"> - <em><em>Transitive</em></em> – the package is accessed indirectly, through other dependencies</p></td></tr>
<tr><td><p><strong><strong>Manager and Scope</strong></strong></p></td><td><p>Shows labels that Checkmarx applied to the package. There is a label indicating the package manager used for package resolution. In addition, the label “Test” is applied to all packages that have the word “test” in their file path.</p><p>Additional labels are applied to special types of dependencies.</p></td><td><ul><li><p><strong><strong>Package Manager</strong></strong> - shows the package manager that was used for resolution, e.g., Maven, Pip, Nuget, Npm etc.</p></li><li><p><strong><strong>Dev</strong></strong> - is applied to dev dependencies.</p></li><li><p><strong><strong>Test</strong></strong> - is applied to all packages that have the word "test" in their file path.</p></li><li><p><strong><strong>NPM Verified</strong></strong> - is applied to packages for which the signatures were verified using <code>npm audit signatures</code>.</p></li><li><p><strong><strong>Plugin</strong></strong> - is applied to packages that relate to a plugin.</p></li></ul></td></tr>
<tr><td><p><strong><strong>Version</strong></strong></p></td><td><p>The version of the package. Hover over the display to show the date of your version, and (if available) the version number and date of the latest version as well as the number of new versions since your most recent update.</p><p>If the version is outdated, an icon is shown next to the version number. If no icon is shown, the package is up to date.</p></td><td><p>e.g., 2.0.0</p><p> The package is outdated.</p></td></tr>
<tr><td><p><strong><strong>Violates Policies</strong></strong></p></td><td><p>Indicates whether or not the package violates policies.</p></td><td><p>Yes, No</p></td></tr>
<tr><td><p><strong><strong>Usage</strong></strong></p><p>(for Projects with Exploitable Path activated)</p></td><td><p>Indicates whether or not this package is used (called) by your project’s source code.</p></td><td><ul><li><p><strong><strong>Used</strong></strong> - This package is used by your project’s source code.</p></li><li><p><strong><strong>Potentially</strong></strong> - This package is a dependency of a direct package that is used by your project’s source code.</p></li><li><p><strong><strong>Unused</strong></strong> - No usage of this package was found.</p></li><li><p><strong><strong>Unknown</strong></strong> - Checkmarx SCA could not determine whether the package is used.</p></li><li><p><strong><strong>No SAST data</strong></strong></p></li><li><p><strong><strong>Package source code not available</strong></strong></p></li><li><p><strong><strong>Unsupported language</strong></strong></p></li></ul></td></tr>
<tr><td><p><strong><strong>Effective Licenses</strong></strong></p></td><td><p>Shows all effective licenses that you have that are associated with this package. For multiple effective licenses, hover over the display to show all licenses.</p></td><td><p>e.g., GPL 2.0, Apache 2.1</p></td></tr>
<tr><td><p><strong><strong>Last Scan</strong></strong></p></td><td><p>Last scan date of the <strong><strong>primary branch</strong></strong> of the Project containing the package.</p><p><strong>Tip</strong></p><p>If the Project has no primary branch, the date will reflect the last scan of the Project.</p><p>Click on the <img src=".gitbook/assets/img-1fd08e2fc5c6c47677d09a578b3656f7.png" alt="" data-size="line"> icon to copy the scan ID.</p></td><td><p>e.g., May 17, 2024</p></td></tr>
<tr><td><p><strong><strong>Project</strong></strong></p></td><td><p>The name of the Checkmarx One Project where the package was identified.</p><p><strong>Tip</strong></p><p>If a package is used by multiple Projects, a separate record (row) is shown for each instance.</p></td><td><p>e.g., Demo01</p></td></tr>
<tr><td><p><strong><strong>Tags</strong></strong></p></td><td><p>Shows both the scan tags and project tags associated with the most recent scan in which the package was identified.</p></td><td><p>e.g., Branch:v0.1.2</p></td></tr>
<tr><td><p><strong><strong>Risks</strong></strong></p></td><td><p>A color coded bar graph indicating the number of vulnerabilities of each severity level.</p><p>Malicious Packages and Suspected Malware are indicated by the malicious icon . </p><p>You can set a filter to show only packages that contain the specified types and with the specified severity levels.</p></td><td><p>e.g.,</p><figure><img src=".gitbook/assets/img-22a4f955afd5295ebe8e71c9d1e55396.png" alt=""></figure></td></tr>
<tr><td><p><strong><strong>Secure Version</strong></strong></p></td><td><p>Indicates whether or not a remediated version (i.e, a version with no vulnerabilities) of this package exists.</p></td><td><ul><li><p>Available</p></li><li><p>Not Available</p></li></ul></td></tr>
<tr><td colspan="3"><p><strong><strong>Context Menu (top right of table)</strong></strong></p></td></tr>
<tr><td><p><strong><strong>Export CSV</strong></strong></p><p><img src=".gitbook/assets/img-a22eaca2c01e00a458384b959aeb1da2.png" alt="" data-size="line"></p></td><td><p>Click on this option to download all of the information in this table (other than <em><em>Violates Policies</em></em> ) as a CSV file.</p><p><strong>Tip</strong></p><p>You can customize the report content by specifying which sections to include and applying the sorting and filters of the current display.</p></td><td></td></tr>
</tbody>
</table>

## Global Inventory and Risks Page - Vulnerabilities and Malware Tab

The Vulnerabilities and Malware tab shows detailed info about all of the risks identified by the scans of all of your Projects. This info includes risk type, ID, publication date, etc. The total number of risks is shown in parentheses in the tab title.

{% hint style="info" icon="pencil" %}
If a risk applies to multiple Projects, a separate record (row) is shown for each instance.
{% endhint %}

You can search for **ID**, **Package**, and **Project** using the search box. You can also sort by column headers and set filters for each column (except for **Risk Type**).

You can export the data on this page as a CSV file. The file content is based on the current sorting and filtering of the table display.

Click on a specific row to open the Vulnerability Details page for that vulnerability in the Scan Results page for the Project. For more information, see [Risk Details Page](project-page-tabs.md#UUID-07a21b5d-72d7-69da-9320-fc8d5e505317).

{% hint style="info" icon="pencil" %}
You can only open the Vulnerability Details page for packages that were identified in Projects which are assigned to your Team.
{% endhint %}

<div align="left"><figure><img src=".gitbook/assets/img-db543b633c2f9dc64818a17264c0651d.png" alt=""></figure></div>

The following table describes the info shown in the Risks tab of the Reports page.

<table>
<thead>
<tr><th><p><strong><strong>Item</strong></strong></p></th><th><p><strong><strong>Description</strong></strong></p></th><th><p><strong><strong>Possible Values</strong></strong></p></th></tr>
</thead>
<tbody>
<tr><td><p><strong><strong>Risk Level</strong></strong></p></td><td><p>The severity level of the vulnerability, based on its CVSS score in the NVD.</p></td><td><ul><li><p><strong><strong>HIGH</strong></strong> - 7.0-10.0</p></li><li><p><strong><strong>MEDIUM</strong></strong> - 4.0-6.9</p></li><li><p><strong><strong>LOW</strong></strong> - 0.0-3.9</p></li></ul><p>For more info see <a href="https://app.gitbook.com/s/XSPACE_PRODUCT_INFO/severity-levels">Severity Levels</a>.</p></td></tr>
<tr><td><p><strong><strong>Risk Type</strong></strong></p></td><td><p>The type of risk.</p></td><td><p><em><em>Vulnerability</em></em>, <em><em>Operational</em></em>, or <em><em>Legal</em></em></p></td></tr>
<tr><td><p><strong><strong>State</strong></strong></p></td><td><p>Indicates the state of the vulnerability.</p></td><td><p></p><ul><li><p><strong><strong>To Verify</strong></strong> - This is the initial state of all vulnerabilities and suspected malware risks, indicating that it is a new finding that hasn’t yet been assessed by your AppSec team.</p></li><li><p><strong><strong>Not Exploitable</strong></strong> - Indicates that your team has determined that this risk doesn’t pose a threat to your application (and isn’t expected to cause a risk at any time in the future).</p></li><li><p><strong><strong>Proposed Not Exploitable</strong></strong> - Indicates that your team has suggested tentatively that this risk doesn’t pose a threat to your application.</p></li><li><p><strong><strong>Confirmed</strong></strong> - Indicates that your team has confirmed that this risk <strong><strong>does</strong></strong> pose a threat and requires mitigation.</p></li><li><p><strong><strong>Urgent</strong></strong> - Indicates that your team has determined that this risk poses an imminent threat and requires urgent mitigation.</p></li></ul></td></tr>
<tr><td><p><strong><strong>Exploitability</strong></strong></p></td><td><p>Shows which exploitability indicators apply to this vulnerability.</p></td><td><ul><li><p><strong><strong>Exploitable Path</strong></strong> - indicates that a path was detected from your source code to the vulnerable method in the package, enabling attackers to exploit the vulnerability. </p><p><strong>Tip</strong></p><p>Results are only returned if Exploitable Path was activated for this project and the project uses a language that is supported for Exploitable Path.</p></li><li><p><strong><strong>Known</strong></strong> - This vulnerability is cataloged by CISA as a <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">Known Exploited Vulnerability</a> (KEV), indicating that it poses a severe and imminent threat.</p></li><li><p><strong><strong>PoC</strong></strong> - A Proof of Concept (POC) for exploiting this vulnerability is available in the wild, making it easy for threat actors to implement an exploitation of this vulnerability. We draw this info from Offensive Security's <a href="https://www.exploit-db.com/">Eploit Database</a>.</p></li></ul></td></tr>
<tr><td><p><strong><strong>EPSS Score</strong></strong></p></td><td><p>The EPSS (Exploit Prediction Scoring System) is a risk score provided by <a href="https://first.org">First</a>, indicating the likelihood of a vulnerability being exploited. The score is presented as a percentage, representing the likelihood of this vulnerability to be exploited within the next 30 days. Hovering over the score will display a percentile indicating the ranking of this risk relative to other vulnerabilities.</p></td><td><p>e.g., 2.1%</p></td></tr>
<tr><td><p><strong><strong>ID</strong></strong></p></td><td><p>The ID of the CVE listing. The ID consists of the CVE prefix followed by the year that the CVE was discovered and the serial counter for that year's CVE listings.</p><p><strong>Tip</strong></p><p>Vulnerabilities discovered by the Checkmarx Vulnerability Research Team which are net yet catalogued as CVEs, are indicated by the “Cx” prefix.</p></td><td><p>e.g., CVE-2019-12384</p></td></tr>
<tr><td><p><strong><strong>Category</strong></strong></p></td><td><p>The category of the vulnerability. For CWEs, the CWE is given as well as a brief description of the vulnerability.</p></td><td><p>e.g., CWE-89|SQL Injection, Malicious, Chainjacking etc.</p></td></tr>
<tr><td><p><strong><strong>Package Name</strong></strong></p></td><td><p>The name of the package in which the vulnerability was identified.</p></td><td><p>e.g., com.fasterxml.jackson.core:jackson-databind</p></td></tr>
<tr><td><p><strong><strong>Package Version</strong></strong></p></td><td><p>The version of the package in which the vulnerability was identified.</p></td><td><p>e.g., 2.9.8</p></td></tr>
<tr><td><p><strong><strong>Last Scan</strong></strong></p></td><td><p>Last scan date of the <strong><strong>primary branch</strong></strong> of the Project containing the package.</p><p><strong>Tip</strong></p><p>If the Project has no primary branch, the date will reflect the last scan of the Project.</p><p>Click on the <img src=".gitbook/assets/img-1fd08e2fc5c6c47677d09a578b3656f7.png" alt="" data-size="line"> icon to copy the scan ID.</p></td><td><p>e.g., Jun 9, 2024</p></td></tr>
<tr><td><p><strong><strong>Project</strong></strong></p></td><td><p>The name of the Project in the organization that has the risk.</p><p><strong>Tip</strong></p><p>If a risk applies to multiple Projects, a separate record (row) is shown for each instance.</p></td><td><p>e.g., Demo01</p></td></tr>
<tr><td><p><strong><strong>Detection/Publication</strong></strong></p></td><td><p>Click on the desired header to alternate between the detection and publication dates.</p><ul><li><p><strong><strong>Detection</strong></strong> - the date that the risk was first detected in this project. For vulnerabilities that were first identified in this scan, the NEW label is shown next to the date.</p></li><li><p><strong><strong>Publication</strong></strong> - the date that this vulnerability was first officially published on a supported public Security Advisory.</p></li></ul></td><td><p>e.g., Jun 24, 2019</p></td></tr>
<tr><td><p><strong><strong>Secure Version</strong></strong></p></td><td><p>Indicates whether or not a remediated version of the package where this vulnerability was identified exists. </p><p><strong>Tip</strong></p><p>In the context of the Risks tab, a version is considered secure as long as this particular vulnerability is remediated, even if the package has other vulnerabilities.</p></td><td><ul><li><p>Available</p></li><li><p>Not Available</p></li></ul></td></tr>
<tr><td colspan="3"><p><strong><strong>Context Menu (top right of table)</strong></strong></p></td></tr>
<tr><td><p><strong><strong>Export CSV</strong></strong></p></td><td><p>Click on this option to download all of the information in this table (in addition to <em><em>Risk Score</em></em>) as a CSV file.</p><p><strong>Tip</strong></p><p>You can customize the report content by specifying which sections to include and applying the sorting and filters of the current display.</p></td><td><p>-</p></td></tr>
</tbody>
</table>

## SCA Global Inventory and Risks Page - Licenses Tab

The Licenses tab shows info about all of the licenses that are associated with the open source packages used by your project.

You can search for **License Name**, **Package Name**, and **Package Version** using the search box. You can also set filters and sort by column headers (except for **Project**).

You can export the data on this page as a CSV file. There is an option to export all data or only data shown based on the current filters.

Click on a specific row to open the Licenses page for that license in the Scan Results page for the Project. For more information, see [License Details Page](/document/preview/365461#UUID-8e77d945-c90d-a0ea-9716-ac65ef53f9dc).

<div align="left"><figure><img src=".gitbook/assets/img-9920439cea025f0a997c22ae91eced07.png" alt=""></figure></div>

The following table describes the info shown in the Licenses tab of the Global Inventory & Risks page.

<table>
<thead>
<tr><th><p><strong><strong>Item</strong></strong></p></th><th><p><strong><strong>Description</strong></strong></p></th><th><p><strong><strong>Possible Values</strong></strong></p></th></tr>
</thead>
<tbody>
<tr><td><p><strong><strong>Risk Level</strong></strong></p></td><td><p>Shows the severity level and score indicating the overall risk level associated with this license. </p><p><strong>Tip</strong></p><p>If this isn't the effective license for this package, then a high license score doesn't necessarily pose a legal risk.</p></td><td><ul><li><p>High - 6-10</p></li><li><p>Medium - 4-5</p></li><li><p>Low - 1-3</p></li><li><p>Info - 0</p></li></ul></td></tr>
<tr><td><p><strong><strong>State</strong></strong></p></td><td><p>Indicates whether or not this license is the "effective" license for your organization's use of this package. Also, if the package to which the license applies has been muted or snoozed, this is indicated in the State column.</p></td><td><ul><li><p>To Verify</p></li><li><p>Effective</p></li><li><p>Not Effective</p></li><li><p>Muted Package</p></li><li><p>Snoozed Package</p></li></ul></td></tr>
<tr><td><p><strong><strong>License Name</strong></strong></p></td><td><p>The name of the license.</p></td><td><p>e.g., GPL 3.0, MIT etc.</p></td></tr>
<tr><td><p><strong><strong>Copyleft</strong></strong></p></td><td><p>The category of the license.</p></td><td><ul><li><p>No Copyleft</p></li><li><p>Full - Copyleft applies</p></li><li><p>Partial - Copyleft applies on modifications only</p></li><li><p>Empty</p></li></ul></td></tr>
<tr><td><p><strong><strong>Package Name</strong></strong></p></td><td><p>The name of the package in which the vulnerability was identified.</p></td><td><p>e.g., com.fasterxml.jackson.core:jackson-databind</p></td></tr>
<tr><td><p><strong><strong>Package Version</strong></strong></p></td><td><p>The version of the package in which the vulnerability was identified.</p></td><td><p>e.g., 2.9.8</p></td></tr>
<tr><td><p><strong><strong>Source Path</strong></strong></p></td><td><p>The source from which the license was identified.</p></td><td><p>e.g., Manifest File, Npm Repository Site, Official Website, Statically Observed etc.</p><p><strong>Tip</strong></p><p>The category "Statically Observed" indicates that the license was identified in the source code (e.g., README files) using regex and other identification methods.</p></td></tr>
<tr><td><p><strong><strong>Project</strong></strong></p></td><td><p>The name of the Project in the organization that has the risk.</p><p><strong>Tip</strong></p><p>If a risk applies to multiple Projects, a separate record (row) is shown for each instance.</p></td><td><p>e.g., Demo01</p></td></tr>
<tr><td colspan="3"><p><strong><strong>Context Menu (top right of table)</strong></strong></p></td></tr>
<tr><td><p><strong><strong>Export CSV</strong></strong></p></td><td><p>Click on this option to download all of the information in this table (in addition to <em><em>Risk Score</em></em>) as a CSV file.</p><p><strong>Tip</strong></p><p>You can customize the report content by specifying which sections to include and applying the sorting and filters of the current display.</p></td><td><p>-</p></td></tr>
</tbody>
</table>
