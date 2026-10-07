# Checkmarx SCA (REST) API - Export Service

{% hint style="warning" %}
This API replaces the [/risk-report API](checkmarx-sca--rest--api---get-scan-reports-and-sboms.md) that had been used previously for generating scan reports and SBOMs. The /risk-report API will be deprecated soon.
{% endhint %}

{% hint style="info" icon="pencil" %}
This API is supported both for Checkmarx One and SCA standalone accounts.
{% endhint %}

## Overview

This API enables you to export reports of the data identified by a Checkmarx SCA scan. This includes detailed info about the open source packages in your project and the risks associated with them. This API can be used to generate the following types of reports:

- **Scan Report** - shows an overview of the security of your project as well as specific vulnerabilities, legal risks, and outdated versions identified by the scan. Scan Reports can be generated in JSON, XML, PDF or CSV format.

- **Software Bill of Materials (SBOM)** - SBOMs can be generated in either [CycloneDX v1.7](https://cyclonedx.org/docs/1.7/#SchemaProperties) or [SPDX v2.3](https://spdx.github.io/spdx-spec/v2.3/) format. SPDX SBOMs are output in JSON format. For CycloneDX, there is an option to output the data as JSON or XML.

- **Remediated Manifest File** - A replacement manifest file that contains the recommended versions for each of your packages. You can download the remediated manifest file and use it to update your project. This feature is currently supported only for npm manifest files and this remediation method is relevant only for direct dependencies.

  {% hint style="warning" %}
  If you update the dependency versions, your code may require some refactoring because of some possible functionality changes.
  {% endhint %}

{% hint style="info" %}
Each API call generates a report in a single format. If you would like to generate reports in multiple formats, then you need to send a separate API call for each report.
{% endhint %}

{% tabs %}
{% tab title="What's in a Scan Report?" %}
The report shows an overview of the security of your project as well as specific vulnerabilities, legal risks, and outdated versions identified by the scan. Reports can be generated in pdf, xml, json, or csv format.

Reports show data divided into the following sections:

- **Packages** - shows info about the open source packages used by your project that contain risks, including: security vulnerabilities, license violations, and outdated versions. The info is separated into a direct packages table and a transitive packages table.
- **Vulnerabilities** - shows info about all of the security vulnerabilities that were identified in the open source packages used by your project, including: severity level, CVE references, remediation recommendations etc. Results are shown also for Supply Chain risks (i.e., suspected malicious packages).
- **Licenses** - shows the licenses that you have for the packages in your project and the legal risks associated with those packages.
- **Policy Violations** - shows any security Policies which the Project violates.

When you generate a report, by default all sections are included in the report. You can specify any sections that you would like to **exclude** from the report.
{% endtab %}
{% tab title="What's in an SBOM Report?" %}
Software Bill of Materials (SBOM), in simple words, is a list of all ingredients (i.e., components) of a software product. Just like you would check the ingredients of a food product before eating it, so too you should know what’s in your software before using it.

Checkmarx SCA leverages our existing infrastructure for identifying vulnerabilities as well as license and supply chain risks to supplement the standard SBOM info. This creates an SBOM that provides real insight into the risks associated with your 3rd party components.

This API enables creation of SBOMs in two popular formats:

- CycloneDX - CycloneDX is a lightweight SBOM standard for application security contexts and supply chain component analysis, used primarily for OWASP compliance.
- SPDX - SPDX is formed with the intent of creating a common data exchange format for information related to software packages for sharing and collection among developers.
{% endtab %}
{% endtabs %}

### Export Service URLs

#### Checkmarx One

The following base URLs are used for these APIs, depending on your environment:

- US Environment - https://ast.checkmarx.net/api/sca/export
- US2 Environment - https://us.ast.checkmarx.net/api/sca/export
- EU Environment - https://eu.ast.checkmarx.net/api/sca/export
- EU2 Environment - https://eu-2.ast.checkmarx.net/api/sca/export
- DEU Environment - https://deu.ast.checkmarx.net/api/sca/export
- Australia & New Zealand – https://anz.ast.checkmarx.net/api/sca/export
- India - https://ind.ast.checkmarx.net/api/sca/export
- Singapore - https://sng.ast.checkmarx.net/api/sca/export
- UAE - https://mea.ast.checkmarx.net/api/sca/export

#### Checkmarx SCA Standalone

- US Environment - https://api-sca.checkmarx.net/export
- EU Environment - https://eu.api-sca.checkmarx.net/export

### Workflow

1. Create a project and run a scan. Take note of the `scanId`.
2. Use `POST /requests`, specifying the `scanId`, and `fileFormat` to generate a report. Take note of the `exportId`.
3. Use `GET /requests`, specifying the `exportId` as a query parameter, to check the status of the report and to get the `fileUrl` for downloading the file.
4. Once the report is complete, use the `fileUrl` to download the report.

### Authentication

Authentication for all SCA endpoints is done using an access token. To learn how to generate an access token, see [Checkmarx SCA (REST) API - POST Token](checkmarx-sca--rest--api---post-token.md).

### Export Endpoints Summary

| API | Method | Endpoint | Description |
| --- | --- | --- | --- |
| Create a report | POST | /requests | Generate a report for a specific scan by specifying the `scanId` and the `fileFormat`. Currently supported formats are:<br><ul><li><p>CycloneDxJson</p></li><li><p>CycloneDxXml</p></li><li><p>SpdxJson</p></li><li><p>RemediatedPackagesJson</p></li><li><p>ScanReportJson</p></li><li><p>ScanReportXml</p></li><li><p>ScanReportCsv</p></li><li><p>ScanReportPdf</p></li></ul> |
| Get report | GET | /requests | Check the status of a specific report, and once the report is completed, retrieve the Url to download the report. |
| Get report formats | GET | /file-formats | Get a list of supported formats. |

## POST Create a report

This endpoint is used to generate a report for a specific scan by specifying the `scanId` and the desired report format.

{% hint style="info" icon="pencil" %}
The success response includes an **exportId** which is used to check the status and get the download URL.
{% endhint %}

### Request Parameters

#### Body Parameters

The POST method must be submitted with the following body parameters.

| **Parameter** | **Mandatory** | **Type** | Default | Enum/Comments | **Description** |
| --- | --- | --- | --- | --- | --- |
| ScanId | yes | string | N/A | N/A | The unique identifier of the scan for which you would like to generate a report. |
| FileFormat | yes | string | N/A | <ul><li><p>CycloneDxJson</p></li><li><p>CycloneDxXml</p></li><li><p>SpdxJson</p></li><li><p>RemediatedPackagesJson</p></li><li><p>ScanReportJson</p></li><li><p>ScanReportXml</p></li><li><p>ScanReportCsv</p></li><li><p>ScanReportPdf</p></li></ul> | The format of the report. |
| ExportParameters/<br>hideDevAndTestDependencies | no | boolean | false |  | If you would like to exclude all development and test dependencies from the SBOM, set this flag as `true.`. Default: false |
| ExportParameters/<br>showOnlyEffectiveLicenses | no | boolean | false |  | If you would like to exclude all licenses that aren't marked as "Effective" from the SBOM, set this flag as `true`. Default: false |
| ExportParameters/excludePackages | no | boolean | false | Relevant only for scan reports |  |
| ExportParameters/excludeLicenses | no | boolean | false | Relevant only for scan reports |  |
| ExportParameters/excludeVulnerabilities | no | boolean | false | Relevant only for scan reports |  |
| ExportParameters/excludePolicies | no | boolean | false | Relevant only for scan reports |  |
| ExportParameters/filePaths\[\] | Required for report type RemediatedPackagesJson | string |  | Relevant only for RemediatedPackagesJson reports. | Comma separated list of paths to manifest files that will be remediated. Paths are relative to the repo folder. |
| ExportParameters/compressedOutput | no | boolean | false | If set as true, the output will always be returned in a zip archive.<br>If false (default), then if there is a single filepath the output will be returned as a json.<br>**Notice** If there are multiple filepaths, then the output is always returned as a zip archive, even if this parameter is set as false. |  |

##### SBOM Body Parameters Sample

```
{
    "ScanId": "2b43b0f5-5080-4224-af24-8325d33d4676",
    "FileFormat": "cycloneDxJson",
    "ExportParameters": {
        "hideDevAndTestDependencies": true,
        "showOnlyEffectiveLicenses": false
    }
}
```

##### Scan Report Body Parameters Sample

```
{
  "ScanId": "e8576978-88f1-4c64-af8a-2b37f94d9e4b",
  "FileFormat": "ScanReportPdf",
  "ExportParameters": {
    "hideDevAndTestDependencies": false,
    "showOnlyEffectiveLicenses": false,
    "excludePackages": false,
    "excludeLicenses": true,
    "excludeVulnerabilities": false,
    "excludePolicies": true
  }
}
```

##### Remediated Packages Body Parameters Sample

```
{
  "ScanId": "e8576978-88f1-4c64-af8a-2b37f94d9e4b",
  "FileFormat": "remediatedPackagesJson",
  "ExportParameters": {
    "filePaths": [juice-shop-master/frontend/package.json, juice-shop-master/package.json]
  }
}
```

#### cURL Sample

```
curl --location 'https://api-sca.checkmarx.net/export/requests' \
--header 'Cx-Authentication-Type: service' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer  someToken' \
--data '{
  "ScanId":
  "2b43b0f5-5080-4224-af24-8325d33d4676",
  "FileFormat": "cycloneDxJson",
      "ExportParameters": {               
           "hideDevAndTestDependencies": true,
            "showOnlyEffectiveLicenses": false
    }
}'
```

### Success Response

Code: 202

The response body consists of the `exportId` of the report.

#### Response Sample

```
{
    "exportId": "2d46cf11-a77c-4333-922a-b3bc33581234"
}
```

## GET report

This endpoint is used to check the status of a specific report. Once the report is completed, this endpoint also returns the Url to be used for downloading the report.

### Request Query Parameters

The GET method must be submitted with the following query parameter.

| **Parameter** | **Mandatory** | **Type** | Enum | **Description** |
| --- | --- | --- | --- | --- |
| exportId | yes | string | N/A | The unique identifier of the report for which you would like to get the status and download link. |

#### cURL Sample

```
curl --location --request GET 'https://api-sca.checkmarx.net/export/requests?exportId=e537bcb0-e539-4a6b-9881-43cb2ea21234' \
--header 'Authorization: Bearer {TOKEN}'
```

### Success Response

Code: 200

The response body consists of the following parameters.

| **Parameter** | **Type** | Enum | **Description** |
| --- | --- | --- | --- |
| exportId | string | N/A | The unique identifier of the scan for which you would like to generate a report. |
| exportStatus | string | <ul><li><p>Pending</p></li><li><p>Exporting</p></li><li><p>Completed</p></li><li><p>Failed</p></li></ul> | The current status of the report generation. |
| fileUrl | string |  | The URL for downloading the report.<br>This parameter is only returned for reports that are in "Completed" status. |

#### Response Sample

```
{
    "exportId": "2d46cf11-a77c-4333-922a-b3bc33586060",
    "exportStatus": "Completed",
    "fileUrl": "https://mysbom.json"
}
```
