# Checkmarx SCA (REST) API - PUT Settings

## Description

Activate/deactivate the Exploitable Path feature for a specific Project.

## Method

### PUT

## Workflow

1. Use `POST /risk-management/projects` to create a new Project.
2. If you would like to activate Exploitable Path, use `PUT /risk-management/settings/projects/{projectId}` to configure the Exploitable Path settings.
3. You can scan the Project using the [Scan Upload](checkmarx-sca--rest--api---scan-upload.md) APIs.

{% hint style="info" icon="pencil" %}
To use Exploitable Path for scans that are run via the API,**no prior configuration is required**. A cloud instance of SAST is automatically used to analyze your proprietary code. Alternatively, you can run EP using your local SAST instance via [Checkmarx SCA Resolver](running-exploitable-path-scans-using-resolver.md).
{% endhint %}

## URL

- US Environment - https://api-sca.checkmarx.net/risk-management/settings/projects/{projectId}
- EU Environment - https://eu.api-sca.checkmarx.net/risk-management/settings/projects/{projectId}

## Curl Sample

```
curl -X PUT " https://api-sca.checkmarx.net/risk-management/settings/projects/1a73fc26-b7aa-1234-b2dd-d3aebfc1da21" -H "accept: application/json" -d "{ "enableExploitablePath": true}”
```

## Media Type (header)

Authorization: Bearer \<access_token\>

Accept: application/json

## Parameters

Path Parameter - Required

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| projectId | string | The unique identifier of the Project for which you would like to activate/deactivate EP. |

Body Parameters - Required

| **Parameter** | **Type** | **Enum** | **Description** |
| --- | --- | --- | --- |
| enableExploitablePath | boolean | <ul><li><p>true</p></li><li><p>false</p></li></ul> | Activate/deactivate Exploitable Path for this Project. |

## Success Response

Code: 204 No Content

There is no body for the success response.

## Error Response

|  |
| --- |
| {% tabs %}<br>{% tab title="Status code: 400" %}<br>Message: `Bad data.`<br>{% endtab %}<br>{% tab title="Status code: 500" %}<br>Message: `InternalServerError`<br>{% endtab %}<br>{% endtabs %} |
