# Checkmarx SCA (REST) API - GET Scan Reports and SBOMs

{% hint style="warning" %}
This API will be deprecated soon. You should start using the new [Export Service](../checkmarx-sca--rest--api---export-service.md) for generating SCA scan reports and SBOMs.
{% endhint %}

## Overview

This API enables you to export reports of the data identified by a Checkmarx SCA scan. This includes detailed info about the open source packages in your project and the risks associated with them. This API can be used to generate two different types of reports:

* Scan Report - shows an overview of the security of your project as well as specific vulnerabilities, legal risks, and outdated versions identified by the scan. Scan Reports can be generated in JSON, XML, PDF or CSV format.
* Software Bill of Materials (SBOM) - shows detailed info about each of the open source packages used by your program and the associated risks, using [CycloneDX v1.3](https://cyclonedx.org/docs/1.3/#SchemaProperties) format. SBOM Reports can be generated in JSON or XML format.

{% hint style="info" %}
Each API call generates a single type of report, in a single format. If you would like to generate multiple types of reports and/or multiple output formats, then you need to send a separate API call for each report.
{% endhint %}

{% tabs %}
{% tab title="What's in a Scan Report?" %}
The report shows an overview of the security of your project as well as specific vulnerabilities, legal risks, and outdated versions identified by the scan. Reports can be generated in pdf, xml, json, or csv format.

Reports show data divided into the following sections:

* Packages - shows info about the open source packages used by your project that contain risks, including: security vulnerabilities, license violations, and outdated versions. The info is separated into a direct packages table and a transitive packages table.
* Vulnerabilities - shows info about all of the security vulnerabilities that were identified in the open source packages used by your project, including: severity level, CVE references, remediation recommendations etc.
* Licenses - shows the licenses that you have for the packages in your project and the legal risks associated with those packages.
* Policy Violations - shows any security Policies which the Project violates.

When you generate a report, you can specify whether you want to include all sections or only specific sections.
{% endtab %}

{% tab title="What's in an SBOM Report?" %}
Software Bill of Materials (SBOM), in simple words, is a list of all ingredients (i.e., components) of a software product. Just like you would check the ingredients of a food product before eating it, so too you should know what’s in your software before using it.

Checkmarx SCA leverages our existing infrastructure for identifying vulnerabilities as well as license and supply chain risks to supplement the standard SBOM info. This creates an SBOM that provides real insight into the risks associated with your 3rd party components.

Our reports use the existing format (SPDX and SWID will be added in the future), with additional “property” fields showing supplemental risk data.
{% endtab %}
{% endtabs %}

### Workflow

After creating a Project and running a scan, use this API to generate a report of the data identified by a specific scan.

### Method

#### GET

### URL

* US Environment - https://api-sca.checkmarx.net/risk-management/risk-reports/{scan\_id}/export
* EU Environment - https://eu.api-sca.checkmarx.net/risk-management/risk-reports/{scan\_id}/export

### Media Type (header)

Authorization: Bearer \<access\_token>

Accept: application/\*

### Request Parameters

#### Path Parameters (Required)

| Parameter | Type   | Description                                                                      |
| --------- | ------ | -------------------------------------------------------------------------------- |
| scan\_id  | string | The unique identifier of the scan for which you would like to generate a report. |

#### Query Parameter

| Parameter   | Type   | Description                                                                                                                                                                            | Enum                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Default |
| ----------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| format      | string | The format of the report that is generated. Your selection determines whether the report generated is a Scan Report or an SBOM Report. It al determines the file format of the report. | <ul><li>Json - Scan Report in JSON format</li><li>Xml - Scan Report in XML format</li><li>Pdf - Scan Report in PDF format</li><li><p>Csv - Scan Report in CSV format</p><p><strong>Tip</strong></p><p>- for this format, the response is given as a zip file, which can be extracted to obtain the CSV files</p></li><li>CycloneDxJson - SBOM report <a href="https://cyclonedx.org/docs/1.3/#SchemaProperties">CycloneDX v1.3</a> format, returned as a JSON</li><li>CycloneDxXml - SBOM report <a href="https://cyclonedx.org/docs/1.3/#SchemaProperties">CycloneDX v1.3</a> format, returned as an XML</li></ul><p><br><strong>Tip</strong> There is an alternative method for generating SBOM reports using the <a href="../checkmarx-sca--rest--api---export-service.md">Export Service</a>. The Export Service generates SBOMs that are more compliant with SBOM formatting specifications. Export Service also supports generating SBOMs in SPDX format.</p> | Json    |
| dataType\[] | string | <p>Specifies the sections that will be included in the report. You can specify<br><strong>Tip</strong> This parameter is relevant only for Scan Reports, not for SBOM Reports.</p>     | <ul><li>All</li><li>Packages</li><li>Vulnerabilities</li><li>Licenses</li><li>Policies</li><li>SupplyChainRisks</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | All     |

### Curl Samples

#### Scan Report Sample

```
curl -X GET "https://api-sca.checkmarx.net/risk-management/risk-reports/ebbb42f2-3421-48db-8d71-dd3f89516c91/export?format=Json&dataType[]=Vulnerabilities&dataType[]=Packages" -H accept: application/*
```

#### SBOM Report Sample

```
curl -X GET "https://api-sca.checkmarx.net/risk-management/risk-reports/ebbb42f2-3421-48db-8d71-dd3f89516c91/export?format=CycloneDxJson" -H accept: application/*
```

### Success Response

Code: 200

For all reports other than CSV, the report is returned in the specified format.

For CSV reports, the response is returned in zip file format, which can be extracted to obtain the CSV files.

For a detailed description of the content of the Reports, see [Viewing SCA Scan Reports](../../checkmarx-sca-user-guide/generating-sca-reports/sca-scan-reports.md#UUID-c05db39c-6802-e561-f066-feb30acb0c8c) and [Viewing CycloneDx SBOM Reports](../../checkmarx-sca-user-guide/generating-sca-reports/sbom-reports.md#UUID-43f1388f-116c-29f1-25e1-3fbfbe1c42e3).

### Error Response

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <div data-gb-custom-block data-tag="tabs"><div data-gb-custom-block data-tag="tab"><p><br></p></div><div data-gb-custom-block data-tag="tab" data-title="Status code: 400"><p><br>Message: <code>Bad data.</code><br></p></div><div data-gb-custom-block data-tag="tab"><p><br></p></div><div data-gb-custom-block data-tag="tab" data-title="Status code: 500"><p><br>Message: <code>InternalServerError</code><br></p></div><div data-gb-custom-block data-tag="tab"><p><br></p></div></div> |
