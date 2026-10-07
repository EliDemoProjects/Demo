# Checkmarx SCA (REST) API - PUT Project

## Method

### PUT

## URL

- US Environment - https://api-sca.checkmarx.net/risk-management/projects/{id}
- EU Environment - https://eu.api-sca.checkmarx.net/risk-management/projects/{id}

## Curl Sample

```
curl -X PUT " https://api-sca.checkmarx.net/risk-management/projects/1a73fabc-b7aa-4ecd-b2dd-12345fc1da21" -H "accept: application/json" -d "{ "name": "Demo04", "assignedTeams": [“Team02”,"Team03"]}”
```

## Media Type (header)

Authorization: Bearer \<access_token\>

Accept: application/json

## Parameters

Path Parameter - Required:

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| id | string | The unique identifier of the Project that you would like to update. |

Body Parameters

### \* indicates a required parameter

| **Parameter** | **Type** | **Enum** | **Description** |
| --- | --- | --- | --- |
| name\* | string | - | The new name for the Project. |
| assignedTeams | string | - | An array specifying the Team/s to which you are assigning the Project. e.g., \[“/CxServer/Team03, /CxServer/Team05”\]<br>**Tip** If this parameter is null, then **all** Teams are assigned to the Project.<br>**Tip** This overwrites the Teams that are currently assigned. |

## Success Response

Code: 204 No Content

There is no body for the success response.

## Error Response

|  |
| --- |
| {% tabs %}<br>{% tab title="Status code: 400" %}<br>Message: `Bad data. Assigned teams inaccessible`<br>{% endtab %}<br>{% tab title="Status code: 409" %}<br>Message: `Project with such name exists`<br>{% endtab %}<br>{% tab title="Status code: 500" %}<br>Message: `InternalServerError`<br>{% endtab %}<br>{% endtabs %} |
