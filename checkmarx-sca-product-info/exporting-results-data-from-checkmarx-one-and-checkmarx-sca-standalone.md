# New Data Retention Policy

We will be changing our customer data retention policy in order to enhance data security, improve compliance and performance, and reduce risk across our platform.

The following data retention rules will be implemented:

*   Results data (e.g., scan results, findings metadata, and analysis logs) will be retained for 3 months. For customers with Premium Support, the retention period will be extended to 12 months.

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>Source code will continue to be retained for only 24 hours.</p></div>

This article explains how you can export your scan results using the SCA web application (UI) or the available APIs.

{% hint style="info" icon="pencil" %}
This article relates to exporting data from SCA standalone platform. A new retention policy is also being impemented for Checkmarx One, see [Checkmarx One Documentation](../document/preview/459401/#UUID-324c3c00-8bb7-3691-1ab3-6cce4d206f06).
{% endhint %}

## Exporting Reports via SCA Web Application

If you need to retain data (e.g., evidence packs, historical reports) beyond the scheduled time period, you should download reports that contain the relevant data.

Learn about generating SCA scan reports [here](../checkmarx-sca-user-guide/generating-sca-reports/sca-scan-reports.md).

## Exporting Reports via SCA (REST) APIs

The following base URLs are used for all calls, depending on your environment:

* US Environment - https://api-sca.checkmarx.net
* EU Environment - https://eu.api-sca.checkmarx.net

1. Use the Projects API GET {Base\_URL}[/risk-management/projects/](https://docs.checkmarx.com/en/34965-19223-checkmarx-sca--rest--api---projects.html#UUID-e242b52f-b644-979b-c738-a2a50f132456) to obtain information about all the Projects in your account, the projectId is necessary for the next step.
2. Use the obtained projectId to obtain information about the scans on each project using the Scans API GET {Base\_URL}[/risk-management/scans](https://docs.checkmarx.com/en/34965-19226-checkmarx-sca--rest--api---scans.html#UUID-b8beb5b1-fc4e-6e45-7973-fb3d6bef1402)/ endpoint to obtain all the scanId from each project. By default, up to 10 results are returned. You can adjust this limit and apply pagination using the size and page parameters.
3.  The scanId obtained can be used with the [Export Service](https://docs.checkmarx.com/en/34965-145615-checkmarx-sca--rest--api---export-service.html#UUID-3a23fef0-9c5d-6099-e9d1-2d2665a2df2f) API to generate a Scan Report that shows an overview of the security of your project as well as specific vulnerabilities, legal risks, and outdated versions identified by the scan. Scan Reports can be generated in JSON, XML, PDF or CSV format.

    Create a report using the POST /requests endpoint and specify the scanId and the fileFormat. Once the request is created you can check its status by using the GET /requests endpoint to check the status of a specific report. More information on the Export Endpoints can be found [here](https://docs.checkmarx.com/en/34965-145615-checkmarx-sca--rest--api---export-service.html#UUID-3a23fef0-9c5d-6099-e9d1-2d2665a2df2f_section-idm33349096126026).
