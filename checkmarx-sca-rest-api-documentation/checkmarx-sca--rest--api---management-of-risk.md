# Checkmarx SCA (REST) API - Management of Risk

{% hint style="warning" %}
These APIs are intended to replace the APIs that had previously been used for risk management: [Checkmarx SCA (REST) API - PUT Risk Reports UnIgnore Vulnerability](checkmarx-sca--rest--apis---apis-that-will-be-deprecated/checkmarx-sca--rest--api---put-risk-reports-unignore-vulnerability.md) and [Checkmarx SCA (REST) API - PUT Risk Reports UnIgnore Vulnerability](checkmarx-sca--rest--apis---apis-that-will-be-deprecated/checkmarx-sca--rest--api---put-risk-reports-unignore-vulnerability.md). The old risk-management APIs will be deprecated on September 30.
{% endhint %}

{% hint style="info" icon="pencil" %}
This API is supported both for Checkmarx One and SCA standalone accounts.
{% endhint %}

## Overview

Checkmarx SCA assigns a profile (predicate) to each risk instance (i.e., vulnerability or Supply Chain risk), consisting of **state**, **severity** and **comments**.

This enables users to prioritize remediation activity and manage risks throughout the SDLC. You can change the state of the risk and add comments in order to keep track of your assessment of the risk. These changes can be applied to that risk instance within a specific project or for multiple projects.

A "Risk Instance" is defined as a specific risk that is associated with a particular package. So that, if a particular risk affects several packages that are used in your project, each instance will have its own profile.

A unique risk is identified based on: packageName, packageVersion, packageManager and vulerabilityId (or supplyChainRiskId).

### Changing the State

Each instance of a risk identified by SCA has a state assigned to it. Possible states are: **To Verify**, **Not Exploitable**, **Confirmed**, **Urgent** and **Proposed Not Exploitable**.

All new risks are initially marked as **To Verify**, meaning that the threat from this risk has not yet been verified and needs to be assessed by your appsec team. During the onboarding process (and subsequent result reviews), if you determine that a risk isn't vulnerable to exploitation, e.g., the package isn't used or the source code doesn't call the vulnerable method, then you can mark it as **Proposed Not Exploitable** or **Not Exploitable**. If you determine that it does pose a threat, then you can mark it as **Confirmed** or **Urgent**.

{% hint style="info" icon="pencil" %}
**Not Exploitable** is now used in place of the state **Ignore** that had been used previously in Checkmarx SCA.
{% endhint %}

### Management of Risk URLs

#### Checkmarx One

The following base URLs are used for these APIs, depending on your environment:

* US Environment - https://ast.checkmarx.net/api/sca/management-of-risk
* US2 Environment - https://us.ast.checkmarx.net/api/sca/management-of-risk
* EU Environment - https://eu.ast.checkmarx.net/api/sca/management-of-risk
* EU2 Environment - https://eu-2.ast.checkmarx.net/api/sca/management-of-risk
* DEU Environment - https://deu.ast.checkmarx.net/api/sca/management-of-risk
* Australia & New Zealand – https://anz.ast.checkmarx.net/api/sca/management-of-risk
* India - https://ind.ast.checkmarx.net/api/sca/management-of-risk
* Singapore - https://sng.ast.checkmarx.net/api/sca/management-of-risk
* UAE - https://mea.ast.checkmarx.net/api/sca/management-of-risk

#### Checkmarx SCA Standalone

* US Environment - https://api-sca.checkmarx.net/management-of-risk
* EU Environment - https://eu.api-sca.checkmarx.net/management-of-risk

### Authentication

Authentication is done using a JWT (JSON Web Token) access token. For Checkmarx One, see [here](https://checkmarx.com/resource/documents/en/34965-68774-checkmarx-one-authentication-api.html). For Checkmarx SCA standalone, see [here](https://checkmarx.com/resource/documents/en/34965-19222-checkmarx-sca--rest--api---post-token.html).

{% hint style="warning" %}
We do not currently enforce the need for specific management of risk permissions in order to use the Management of Risk APIs.
{% endhint %}

### Workflow

1. Create a project, run a scan and review and triage the results.
2. Use `POST /package-vulnerabilities` and/or `POST /package-supply-chain-risks` to change the states and add comments for specific vulnerabilities and supply chain risks.
3.  Run scan recalculation. For SCA standalone, use [Checkmarx SCA (REST) API - Scan Recalculation](checkmarx-sca--rest--api---scan-recalculation.md).For Checkmarx One, use the API documented [here](https://checkmarx.stoplight.io/docs/checkmarx-one-api-reference-guide/49c4b318522c7-run-scan-recalculation).

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>Management of Risk changes don't take affect until either a scan recalculation is done or a new scan is run on the project.</p></div>

## Endpoint Summary

The following is a list of Checkmarx One APIs that relate to Management of Risk:

| API                              | Method | Endpoint                    | Description                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------- | ------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Change vulnerability profile     | POST   | /package-vulnerabilities    | <p>Change the state and add a comment to a specific instance of a vulnerability.<br>You can specify one or more projects for which the change will take effect.<br><strong>Tip</strong> This endpoint replaces the current APIs <code>IgnoreVulnerability</code> and <code>UnignoreVulnerability</code>, which will be deprecated soon.</p> |
| Change Supply Chain risk profile | POST   | /package-supply-chain-risks | <p>Change the state and add a comment to a specific instance of an SCS risk.<br>You can specify one or more projects for which the change will take effect.</p>                                                                                                                                                                             |

## Package Vulnerabilities Endpoint Details

<details>

<summary>POST /package-vulnerabilities</summary>

Change the profile info (state and comments) of a specific vulnerability instance. You can specify one or more projects for which the change will take effect.

#### Media Type (header)

Authorization: `Bearer <access_token>`

Accept: `application/json`

#### cURL Example

```
curl --request POST \
  --url https://eu.ast.checkmarx.net/api/sca/management-of-risk/package-vulnerabilities \
  --header 'Content-Type: application/json' \
  --data '{
  "Actions": [
    {
      "Value": "NotExploitable",
      "Comment": "Effective validation in place",
      "ActionType": "ChangeState"
    }
  ],
  "ProjectIds": [
    "515f6bec-d548-450b-b4c4-2b929d9596ff"
  ],
  "PackageName": "NewtonSoftJson",
  "PackageManager": "Nuget",
  "PackageVersion": "1.0.0",
  "VulnerabilityId": "CVE-2021-24112"
}'
```

#### Parameters

Body Parameters

| Parameter       | Mandatory | Type        | Enums                                                                                                                                        | Description                                                                                                                                                                                    |
| --------------- | --------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| packageName     | yes       | string      |                                                                                                                                              | The name of the package.                                                                                                                                                                       |
| packageVersion  | yes       | string      |                                                                                                                                              | The version of the package.                                                                                                                                                                    |
| packageManager  | yes       | string      |                                                                                                                                              | The package manager used for this package.                                                                                                                                                     |
| VulnerabilityId | yes       | string      |                                                                                                                                              | The id of the vulnerability.                                                                                                                                                                   |
| projectIds\[]   | no        | string      |                                                                                                                                              | <p>The project id of one or more projects for which the new profile will be applied.<br>If no project ID is specified, then by default the change applies to all projects in your account.</p> |
| actions\[]      | yes       | json object |                                                                                                                                              | The action that is being taken to change the risk instance profile.                                                                                                                            |
| actionType      | yes       | string      | <p>Currently, the only supported action type is:<br>ChangeState</p>                                                                          | The type of action to be done.                                                                                                                                                                 |
| value           | yes       | string      | <p>For ChangeState:<br></p><ul><li>ToVerify</li><li>NotExploitable</li><li>ProposedNotExploitable</li><li>Confirmed</li><li>Urgent</li></ul> | The value assigned for this action, based on the action type. For ChangeState, specify the state to be assigned to this vulnerability instance.                                                |
| comment         | no        | string      |                                                                                                                                              | Add a comment explaining the action taken.                                                                                                                                                     |

#### Responses

| Status Code | Meaning                                                                       |
| ----------- | ----------------------------------------------------------------------------- |
| 200         | Successful Operation.                                                         |
| 404         | Project or package not found.                                                 |
| 403         | User does not have the required permissions to change the status of the risk. |

</details>

## Package Supply Chain Risks Endpoint Details

<details>

<summary>POST /package-supply-chain-risks</summary>

Change the profile info (state and comments) of a specific supply chain risk instance. You can specify one or more projects for which the change will take effect.

#### Media Type (header)

Authorization: `Bearer <access_token>`

Accept: `application/json`

#### Parameters

Body Parameters

| Parameter         | Mandatory | Type        | Enums                                                                                                                                        | Description                                                                                                                                                                                    |
| ----------------- | --------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| packageName       | yes       | string      |                                                                                                                                              | The name of the package.                                                                                                                                                                       |
| packageVersion    | yes       | string      |                                                                                                                                              | The version of the package.                                                                                                                                                                    |
| packageManager    | yes       | string      |                                                                                                                                              | The package manager used for this package.                                                                                                                                                     |
| SupplyChainRiskId | yes       | string      |                                                                                                                                              | The id of the supply chain risk.                                                                                                                                                               |
| projectIds\[]     | no        | string      |                                                                                                                                              | <p>The project id of one or more projects for which the new profile will be applied.<br>If no project ID is specified, then by default the change applies to all projects in your account.</p> |
| actions\[]        | yes       | json object |                                                                                                                                              | The action that is being taken to change the risk instance profile.                                                                                                                            |
| actionType        | yes       | string      | <p>Currently, the only supported action type is:<br>ChangeState</p>                                                                          | The type of action to be done.                                                                                                                                                                 |
| value             | yes       | string      | <p>For ChangeState:<br></p><ul><li>ToVerify</li><li>NotExploitable</li><li>ProposedNotExploitable</li><li>Confirmed</li><li>Urgent</li></ul> | The value assigned for this action, based on the action type. For ChangeState, specify the state to be assigned to this vulnerability instance.                                                |
| comment           | no        | string      |                                                                                                                                              | Add a comment explaining the action taken.                                                                                                                                                     |

#### cURL Example

```
curl --request POST \
  --url https://eu.ast.checkmarx.net/api/sca/management-of-risk/package-supply-chain-risks \
  --header 'Content-Type: application/json' \
  --data '{
  "Actions": [
    {
      "Value": "NotExploitable",
      "Comment": "Effective validation in place",
      "ActionType": "ChangeState"
    }
  ],
  "ProjectIds": [
    "515f6bec-d548-450b-b4c4-2b929d9596ff"
  ],
  "PackageName": "coa",
  "PackageManager": "npm",
  "PackageVersion": "3.1.3",
  "SupplyChainRiskId": "Cx3a0295c5-2d04"
}'
```

#### Responses

| Status Code | Meaning                                                                       |
| ----------- | ----------------------------------------------------------------------------- |
| 200         | Successful Operation.                                                         |
| 404         | Project or package not found.                                                 |
| 403         | User does not have the required permissions to change the status of the risk. |

</details>
