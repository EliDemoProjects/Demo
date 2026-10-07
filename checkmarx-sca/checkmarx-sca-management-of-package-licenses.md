# Checkmarx SCA Management of Package Licenses

## Overview

{% hint style="info" icon="pencil" %}
This API is supported both for Checkmarx One and SCA standalone accounts.
{% endhint %}

### Adding Licenses

If you are aware of a license that is relevant for a particular package that was not identified by Checkmarx, you can add the license manually to the package. Licenses are added to specific packages. A unique package is identified based on: packageName, packageVersion and packageManager.

### Management of Package Licenses URLs

#### Checkmarx One

The following base URLs are used for these APIs, depending on your environment:

- US Environment - https://ast.checkmarx.net/api/sca/analysis/management-of-risk
- US2 Environment - https://us.ast.checkmarx.net/api/sca/analysis/management-of-risk
- EU Environment - https://eu.ast.checkmarx.net/api/sca/analysis/management-of-risk
- EU2 Environment - https://eu-2.ast.checkmarx.net/api/sca/analysis/management-of-risk
- DEU Environment - https://deu.ast.checkmarx.net/api/sca/analysis/management-of-risk
- Australia & New Zealand – https://anz.ast.checkmarx.net/api/sca/analysis/management-of-risk
- India - https://ind.ast.checkmarx.net/api/sca/analysis/management-of-risk
- Singapore - https://sng.ast.checkmarx.net/api/sca/analysis/management-of-risk
- UAE - https://mea.ast.checkmarx.net/api/sca/analysis/management-of-risk

#### Checkmarx SCA Standalone

- US Environment - https://api-sca.checkmarx.net/analysis/management-of-risk
- EU Environment - https://eu.api-sca.checkmarx.net/analysis/management-of-risk

### Management of Package Licenses URLs

#### Checkmarx One

The following base URLs are used for these APIs, depending on your environment:

- US Environment - [https://ast.checkmarx.net/api/sca/management-of-risk](https://ast.checkmarx.net/api/sca/management-of-risk)
- US2 Environment - [https://us.ast.checkmarx.net/api/sca/management-of-risk](https://us.ast.checkmarx.net/api/sca/management-of-risk)
- EU Environment - [https://eu.ast.checkmarx.net/api/sca/management-of-risk](https://eu.ast.checkmarx.net/api/sca/management-of-risk)
- DEU Environment - [https://deu.ast.checkmarx.net/api/sca/management-of-risk](https://deu.ast.checkmarx.net/api/sca/management-of-risk)
- Australia & New Zealand – [https://anz.ast.checkmarx.net/api/sca/management-of-risk](https://anz.ast.checkmarx.net/api/sca/management-of-risk/package-licenses)
- India - [https://ind.ast.checkmarx.net/api/sca/management-of-risk](https://ind.ast.checkmarx.net/api/sca/management-of-risk/package-licenses)
- Singapore - [https://sng.ast.checkmarx.net/api/sca/management-of-risk](https://sng.ast.checkmarx.net/api/sca/management-of-risk)
- UAE Environment - [https://mea.ast.checkmarx.net/api/sca/management-of-risk](https://mea.ast.checkmarx.net/api/sca/management-of-risk)

#### Checkmarx SCA Standalone

- US Environment - [https://api-sca.checkmarx.net/management-of-risk](https://api-sca.checkmarx.net/management-of-risk)
- EU Environment - [https://eu.api-sca.checkmarx.net/management-of-risk](https://eu.api-sca.checkmarx.net/management-of-risk)

### Authentication

Authentication is done using a JWT (JSON Web Token) access token. For Checkmarx One, see [here](https://checkmarx.com/resource/documents/en/34965-68774-checkmarx-one-authentication-api.html). For Checkmarx SCA standalone, see [here](https://checkmarx.com/resource/documents/en/34965-19222-checkmarx-sca--rest--api---post-token.html)

## Endpoint Summary

The following is a list of Checkmarx One APIs that relate to management of package licenses:

| **API** | **Method** | **Endpoint** | **Description** |
| --- | --- | --- | --- |
| Add License | POST | /package-licenses | Add a license to a package. |
| Disable License | POST | /package-licenses/disable | Disable (delete) a license that was added manually. |

## Package License Endpoint Details

{% tabs %}
{% tab title="POST /package-licenses" %}
If you are aware of a license that is relevant for a particular package that was not identified by Checkmarx, you can add the license manually to the package. Licenses are added to specific packages. A unique package is identified based on: packageName, packageVersion and packageManager.

#### Media Type (header)

Authorization: `Bearer <access_token>`

Accept: `application/json`

#### cURL Example

```
curl --location 'https://api-sca.checkmarx.net/management-of-risk/package-licenses' \
--header 'Cx-Authentication-Type: user' \
--header 'Authorization: Bearer TOKEN' \
--header 'Content-Type: application/json' \
--data '
{
    "LicenseId": 27,
    "PackageName": "NuGet.CommandLine",
    "PackageVersion": "4.4.1",
    "PackageManager": "Nuget",
    "ProjectIds": ["0d69c407-13d2-4013-b184-4b3be2bde063"],
    "Actions": [
        {
            "ActionType": "AddLicense",
            "Value": "27"
        }
    ]
}
'
```

#### Parameters

Body Parameters

| **Parameter** | **Mandatory** | **Type** | **Enums** | **Description** |
| --- | --- | --- | --- | --- |
| LicenseId | yes | int |  | The ID that represents the license that you are adding to the package. See the table below for the list of supported licenses and the ID of each license. |
| packageName | yes | string |  | The name of the package. |
| packageVersion | yes | string |  | The version of the package. |
| packageManager | yes | string |  | The package manager used for this package. |
| projectId | no | string |  | The project IDs of each of the projects for which this license is being added to this package.<br>If no project ID is specified, then by default the license is added in **all** projects in your account. |
| actions\[\] | yes | json object |  | The action that is being taken to add one or more licenses. |
| actionType | yes | string | Supported action types are:<br><ul><li><p>AddLicense</p></li></ul> | The type of action to be done.<br><ul><li><p>The action <code>AddLicense</code> adds the license. By default, each license that is added is marked as <strong>Effective</strong>. You can change the state to <strong>Not Effective</strong> using the management of risk APIs.</p></li></ul> |
| value | yes | int |  | The ID that represents the license that you are adding to the package.<br>Note: This should be the identical ID that was given for the LicenseId parameter. |

#### Success Response

Code: 201 successful operation

There is no body for the success response.
{% endtab %}
{% tab title="POST /package-licenses/disable" %}
Use this endpoint to disable (delete) a license that was added manually.

#### Media Type (header)

Authorization: `Bearer <access_token>`

Accept: `application/json`

#### cURL Example

```
curl --location 'https://api-sca.checkmarx.net/management-of-risk/package-licenses/disable' \
--header 'Cx-Authentication-Type: user' \
--header 'Authorization: Bearer TOKEN' \
--header 'Content-Type: application/json' \
--data '
{
    "LicenseId": 27,
    "PackageName": "NuGet.CommandLine",
    "PackageVersion": "4.4.1",
    "PackageManager": "Nuget", "PackageId": "Python-pip-22.2",
    "ProjectIds": ["0d69c407-13d2-4013-b184-4b3be2bde063"],
    "ActionType": "AddLicense"
}
'
```

#### Parameters

Body Parameters

| **Parameter** | **Mandatory** | **Type** | **Enums** | **Description** |
| --- | --- | --- | --- | --- |
| LicenseId | yes | int |  | The ID that represents the license that you are disabling (deleting) for this package. See the table below for the list of supported licenses and the ID of each license. |
| packageName | yes | string |  | The name of the package. |
| packageVersion | yes | string |  | The version of the package. |
| packageManager | yes | string |  | The package manager used for this package. |
| projectId | no | string |  | The project IDs of each of the projects for which this license is being disabled (deleted).<br>If no project ID is specified, then by default the license is deleted from **all** projects in your account. |
| actionType | yes | string | Currently, the only supported action type is:<br><ul><li><p>AddLicense</p></li></ul> | Specify the action that you are disabling. |

#### Success Response

Code: 204

There is no body for the success response.
{% endtab %}
{% endtabs %}
