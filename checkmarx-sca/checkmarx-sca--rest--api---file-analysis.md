# Checkmarx SCA (REST) API - File Analysis

These APIs enable you to upload a supported type of report file for SCA analysis, and retrieve results. The results include detailed info about the packages specified in the file as well as all associated vulnerabilities, supply chain risks and license info. This service currently supports SBOMs in CycloneDx (v1.0-1.6) and SPDX (v2.3) formats.

{% hint style="warning" %}
This API does not run a full SCA scan of your project. To run a full SCA scan, use the [Scan Upload](checkmarx-sca--rest--api---scan-upload.md) endpoints.
{% endhint %}

{% hint style="info" icon="pencil" %}
This API is supported both for Checkmarx One and SCA standalone accounts.
{% endhint %}

## Data Retention

The default behavior is to store the SBOM and related data in the cloud for 5 days and to enable multiple retrievals of the Analysis report. If you set `DisableRetention` as `true`, then as soon as the Analysis report has been retrieved successfully once, all related data is deleted from the SCA cloud.

## File Analysis URLs

### Checkmarx One

The following base URLs are used for these APIs, depending on your environment:

- US Environment - https://ast.checkmarx.net/api/sca/analysis/requests
- US2 Environment - https://us.ast.checkmarx.net/api/sca/analysis/requests
- EU Environment - https://eu.ast.checkmarx.net/api/sca/analysis/requests
- EU2 Environment - https://eu-2.ast.checkmarx.net/api/sca/analysis/requests
- DEU Environment - https://deu.ast.checkmarx.net/api/sca/analysis/requests
- Australia & New Zealand – https://anz.ast.checkmarx.net/api/sca/analysis/requests
- India - https://ind.ast.checkmarx.net/api/sca/analysis/requests
- Singapore - https://sng.ast.checkmarx.net/api/sca/analysis/requests
- UAE - https://mea.ast.checkmarx.net/api/sca/analysis/requests

### Checkmarx SCA Standalone

- US Environment - https://api-sca.checkmarx.net/analysis/requests
- EU Environment - https://eu.api-sca.checkmarx.net/analysis/requests

## Workflow

1. Use `POST /analysis/requests` to run file analysis, taking note of the `requestId` that is returned.
2. Use `GET /analysis/requests/{requestId}` specifying the desired `requestId` to retrieve results from the file analysis.

## SCA File Analysis Endpoints Summary

| API | Method | Endpoint | Description |
| --- | --- | --- | --- |
| Run file analysis | POST | /analysis/requests | Run file analysis on a supported file type. |
| Retrieve analysis results | GET | /analysis/requests/{requestId} | Get detailed results from SCA file analysis. The results include detailed info about the packages specified in the file as well as all associated vulnerabilities, supply chain risks and license info. |

## POST Run file analysis

### Description

Submit a file for SCA analysis. The success response returns the `requestId` which can be used to retrieve the results from the analysis.

### Media Type (header)

Authorization: Bearer \<access_token\>

Accept: application/json

### Curl Sample

```
curl --request POST \
  --url 'https://api-sca.checkmarx.net/analysis/requests/?AnalysisType=sbom' \
  --header 'Accept: text/plain, application/json, text/json' \
  --header 'Content-Type: multipart/form-data' \
  --form fileToAnalyse=@38-42.CycloneDx.json
```

### Parameters

Query Parameters

| Parameter | Type | Required | Enum | Description |
| --- | --- | --- | --- | --- |
| AnalysisType | string | Yes | sbom | Specify the type of file that you are submitting for analysis. Currently, the only supported type is Sbom. |
| DisableRetention | boolean | No |  | If `true`, as soon as the Analysis report has been retrieved successfully once, all related data is deleted from the SCA cloud. If `false` (default) then data is retained for 5 days and multiple report retrievals are allowed. |

Body Parameter - Required

Format: multipart/form-data

| Parameter | Type | Description |
| --- | --- | --- |
| fileToAnalyze | string | The path to the file that is being submitted for analysis.<br>**Tip** You can submit a raw json or xml file, or a zip archive. |

### Success Response

<details>
<summary>Status code: 202</summary>

Message: `Accepted`

</details>

Attributes:

| Attribute | Type | Description |
| --- | --- | --- |
| requestId | string | The unique identifier for retrieving results from this analysis. |

### Error Response

|  |
| --- |
| <details><br><summary>Status code: 400</summary><br><br>Message: `Bad request`<br><br></details> |

## GET Retrieve analysis results

### Description

Get detailed results from SCA file analysis. The results include detailed info about the packages specified in the file as well as all associated vulnerabilities, supply chain risks and license info.

### URL

- US Engironment - https://api-sca.checkmarx.net/analysis/requests/{requestId}
- EU Environment - https://eu.api-sca.checkmarx.net/analysis/requests/{requestId}

### Media Type (header)

Authorization: Bearer \<access_token\>

Accept: application/json

### Curl Sample

```
curl --request GET \
  --url https://ast.checkmarx.net/api/sca/analysis/requests/84f6da29-0eb5-429b-9a56-681cfea2764f \
  --header 'Accept: text/plain, application/json, text/json'
```

### Parameters

Path Parameter - Required

| Parameter | Type | Description |
| --- | --- | --- |
| requestId | string | Specify the unique identifier for the SCA analysis that you would like to retrieve. |

### Success Response

<details>
<summary>Status code: 200</summary>

Message: `Success`

</details>

#### Sample Response Body

```
{
	"status": "Completed",
	"result": {
		"resultType": "SbomResult",
		"id": "urn:uuid:99da86c5-c3be-4bba-bc3e-100a749274d5",
		"sbomType": "CycloneDx",
		"sbomFormat": "Json",
		"documentDate": "2023-10-18T09:38:50Z",
		"documentVersion": "1",
		"documentNamespace": null,
		"tools": [
			"SCA"
		],
		"componentType": "Library",
		"componentName": "Scan 99da86c5-c3be-4bba-bc3e-100a749274d5",
		"componentVersion": "1.0.0",
		"componentVersionReason": null,
		"componentAuthor": null,
		"componentPublisher": null,
		"componentDescription": null,
		"sbomPackages": [
			{
				"name": "junit:junit",
				"version": "4.12",
				"isDirect": true,
				"moduleType": "gradle",
				"description": null,
				"projectHomePage": null,
				"releaseDate": "2014-12-04T16:17:00+00:00",
				"projectUrl": null,
				"packageVulnerabilities": [
					{
						"id": "CVE-2020-15250",
						"description": "In JUnit4 from version 4.7 and before 4.13.1, the test rule TemporaryFolder contains a local information disclosure vulnerability. On Unix like systems, the system's temporary directory is shared between all users on that system. Because of this, when files and directories are written into this directory they are, by default, readable by other users on that same system. This vulnerability does not allow other users to overwrite the contents of these directories or files. This is purely an information disclosure vulnerability. This vulnerability impacts you if the JUnit tests write sensitive information, like API keys or passwords, into the temporary folder, and the JUnit tests execute in an environment where the OS has other untrusted users. Because certain JDK file system APIs were only added in JDK 1.7, this this fix is dependent upon the version of the JDK you are using. For Java 1.7 and higher users: this vulnerability is fixed in 4.13.1. For Java 1.6 and lower users: no patch is available, you must use the workaround below. If you are unable to patch, or are stuck running on Java 1.6, specifying the `java.io.tmpdir` system environment variable to a directory that is exclusively owned by the executing user will fix this vulnerability. For more information, including an example of vulnerable code, see the referenced GitHub Security Advisory.",
						"cwe": "CWE-732",
						"severity": "Medium",
						"foundOnSource": true,
						"isDetectedBySca": true
					}
				],
				"packageLicenses": [
					{
						"name": "Eclipse 1.0",
						"licenseUrl": "https://www.eclipse.org/legal/epl-v10.html",
						"description": "This commercially-friendly copyleft license provides the ability to commercially license binaries; a modern royalty-free patent license grant; and the ability for linked works to use other licenses, including commercial ones.",
						"foundOnSource": false,
						"isDetectedBySca": true
					}
				],
				"children": [],
				"packageSupplyChainInformation": {
					"isMalicious": false,
					"contributorReputationScore": null,
					"packageReliabilityScore": null,
					"runTimeBehaviorScore": null,
					"supplyChainRisks": []
				},
				"analysedVersion": null,
				"analysedVersionReason": null
			},
			{
				"name": "commons-httpclient:commons-httpclient",
				"version": "3.1",
				"isDirect": false,
				"moduleType": "gradle",
				"description": null,
				"projectHomePage": null,
				"releaseDate": "2007-08-21T13:44:00+00:00",
				"projectUrl": null,
				"packageVulnerabilities": [
					{
						"id": "CVE-2012-5783",
						"description": "Apache Commons HttpClient prior to 4.0-alpha1, as used in Amazon Flexible Payments Service (FPS) merchant Java SDK and other products, does not verify that the server hostname matches a domain name in the subject's Common Name (CN) or 'subjectAltName' field of the X.509 certificate, which allows man-in-the-middle attackers to spoof SSL servers via an arbitrary valid certificate.",
						"cwe": "CWE-295",
						"severity": "Medium",
						"foundOnSource": true,
						"isDetectedBySca": true
					},
					{
						"id": "CVE-2012-6153",
						"description": "http/conn/ssl/AbstractVerifier.java in Apache Commons HttpClient before 4.2.3 does not properly verify that the server hostname matches a domain name in the subject's Common Name (CN) or subjectAltName field of the X.509 certificate, which allows man-in-the-middle attackers to spoof SSL servers via a certificate with a subject that specifies a common name in a field that is not the CN field.  NOTE: this issue exists because of an incomplete fix for CVE-2012-5783.",
						"cwe": "CWE-20",
						"severity": "Medium",
						"foundOnSource": false,
						"isDetectedBySca": true
					}
				],
				"packageLicenses": [
					{
						"name": "Apache 2.0",
						"licenseUrl": "https://www.apache.org/licenses/LICENSE-2.0",
						"description": "A permissive license whose main conditions require preservation of copyright and license notices. Contributors provide an express grant of patent rights. Licensed works, modifications, and larger works may be distributed under different terms and without source code.",
						"foundOnSource": false,
						"isDetectedBySca": true
					}
				],
				"children": [],
				"packageSupplyChainInformation": {
					"isMalicious": false,
					"contributorReputationScore": null,
					"packageReliabilityScore": null,
					"runTimeBehaviorScore": null,
					"supplyChainRisks": []
				},
				"analysedVersion": null,
				"analysedVersionReason": null
			},
			{
				"name": "mistune",
				"version": "0.8.4",
				"isDirect": false,
				"moduleType": "python",
				"description": null,
				"projectHomePage": "",
				"releaseDate": "2018-10-11T06:59:26+00:00",
				"projectUrl": "https://pypi.org/project/mistune/",
				"packageVulnerabilities": [
					{
						"id": "CVE-2022-34749",
						"description": "In mistune through 2.0.2, support of inline markup is implemented by using regular expressions that can involve a high amount of backtracking on certain edge cases. This behavior is commonly named catastrophic backtracking.",
						"cwe": "CWE-697",
						"severity": "High",
						"foundOnSource": true,
						"isDetectedBySca": true
					},
					{
						"id": "CVE-2022-34750",
						"description": "An issue was discovered in MediaWiki through 1.38.1. The lemma length of a Wikibase lexeme is currently capped at a thousand characters. Unfortunately, this length is not validated, allowing much larger lexemes to be created, which introduces various denial-of-service attack vectors within the Wikibase and WikibaseLexeme extensions. This is related to Special:NewLexeme and Special:NewProperty.",
						"cwe": "CWE-770",
						"severity": "High",
						"foundOnSource": true,
						"isDetectedBySca": false
					}
				],
				"packageLicenses": [
					{
						"name": "BSD 3",
						"licenseUrl": "https://opensource.org/licenses/BSD-3-Clause",
						"description": "A permissive license similar to the BSD 2-Clause License, but with a 3rd clause that prohibits others from using the name of the project or its contributors to promote derived products without written consent.",
						"foundOnSource": false,
						"isDetectedBySca": true
					}
				],
				"children": [],
				"packageSupplyChainInformation": {
					"isMalicious": false,
					"contributorReputationScore": null,
					"packageReliabilityScore": null,
					"runTimeBehaviorScore": null,
					"supplyChainRisks": []
				},
				"analysedVersion": null,
				"analysedVersionReason": null
			},
			{
				"name": "Microsoft.Data.SqlClient",
				"version": "1.0.19269.1",
				"isDirect": false,
				"moduleType": "nuget",
				"description": "Provides the data provider for SQL Server. These classes provide access to versions of SQL Server and encapsulate database-specific protocols, including tabular data stream (TDS)\n\nCommonly Used Types:\nMicrosoft.Data.SqlClient.SqlConnection\nMicrosoft.Data.SqlClient.SqlException\nMicrosoft.Data.SqlClient.SqlParameter\nMicrosoft.Data.SqlClient.SqlDataReader\nMicrosoft.Data.SqlClient.SqlCommand\nMicrosoft.Data.SqlClient.SqlTransaction\nMicrosoft.Data.SqlClient.SqlParameterCollection\nMicrosoft.Data.SqlClient.SqlClientFactory\n\nWhen using NuGet 3.x this package requires at least version 3.4.",
				"projectHomePage": null,
				"releaseDate": "2019-09-26T21:15:53.953+00:00",
				"projectUrl": null,
				"packageVulnerabilities": [
					{
						"id": "CVE-2022-41064",
						"description": ".NET Framework `System.Data.SqlClient` versions prior to \n4.8.5 and `Microsoft.Data.SqlClient` versions prior to 1.1.4 and 2.0.0 prior to 2.1.2 is vulnerable to Information Disclosure Vulnerability.",
						"cwe": "CWE-200",
						"severity": "Medium",
						"foundOnSource": true,
						"isDetectedBySca": true
					},
					{
						"id": "CVE-2000-99999",
						"description": null,
						"cwe": null,
						"severity": null,
						"foundOnSource": true,
						"isDetectedBySca": false
					}
				],
				"packageLicenses": [
					{
						"name": "MIT",
						"licenseUrl": "https://opensource.org/licenses/MIT",
						"description": "A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.",
						"foundOnSource": false,
						"isDetectedBySca": true
					}
				],
				"children": [],
				"packageSupplyChainInformation": {
					"isMalicious": false,
					"contributorReputationScore": null,
					"packageReliabilityScore": null,
					"runTimeBehaviorScore": null,
					"supplyChainRisks": []
				},
				"analysedVersion": null,
				"analysedVersionReason": null
			},
			{
				"name": "pointfreeco:swift-clocks",
				"version": "1.0.0",
				"isDirect": false,
				"moduleType": "swift",
				"description": null,
				"projectHomePage": null,
				"releaseDate": "2023-07-30T00:00:00+00:00",
				"projectUrl": null,
				"packageVulnerabilities": [],
				"packageLicenses": [
					{
						"name": "MIT",
						"licenseUrl": "https://opensource.org/licenses/MIT",
						"description": "A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.",
						"foundOnSource": false,
						"isDetectedBySca": true
					}
				],
				"children": [],
				"packageSupplyChainInformation": {
					"isMalicious": false,
					"contributorReputationScore": null,
					"packageReliabilityScore": null,
					"runTimeBehaviorScore": null,
					"supplyChainRisks": []
				},
				"analysedVersion": null,
				"analysedVersionReason": null
			}
		],
		"sbomLicenses": [],
		"sbomVulnerabilities": [],
		"sbomSupplyChainInformation": {
			"isMalicious": false,
			"contributorReputationScore": null,
			"packageReliabilityScore": null,
			"runTimeBehaviorScore": null,
			"supplyChainRisks": []
		}
	},
	"errorMessage": null
}
```

### Error Response

|  |
| --- |
| {% tabs %}<br>{% tab title="Status code: 403" %}<br>Message: `Forbidden`<br>{% endtab %}<br>{% tab title="Status code: 404" %}<br>Message: `Not Found`<br>{% endtab %}<br>{% endtabs %} |
