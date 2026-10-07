# Checkmarx SCA (REST) API - POST Project

## Title

POST Project

## Description

Create a new Project. You need to specify the Project name and assign the Project to Teams. The response returns a unique Project ID which is used to refer to the Project when running scans or performing CRUD actions.

## Method

### POST

## Workflow

1. Use `POST /risk-management/projects` to create a new Project.
2. If you would like to activate Exploitable Path, use `PUT /risk-management/settings/projects/{projectId}` to configure the Exploitable Path settings.
3. You can scan the Project using the [Scan Upload](../checkmarx-sca--rest--api---scan-upload/) APIs.

## URL

* US Environment - https://api-sca.checkmarx.net/risk-management/projects
* EU Environment - https://eu.api-sca.checkmarx.net/risk-management/projects

## Curl Sample

```
curl -X POST " https://api-sca.checkmarx.net/risk-management/projects" -H "accept: application/json" -d "{ "name": "Demo04", "assignedTeams": [“Team02”,"Team03"]}”
```

## Media Type (header)

Authorization: Bearer \<access\_token>

Accept: application/json

## Parameters

Body Parameters - Required

| Parameter        | Type   | Enum | Description                                                                                                                                                                                  |
| ---------------- | ------ | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name             | string | -    | The name of the Project.                                                                                                                                                                     |
| assignedTeams\[] | string | -    | <p>An array sprecifying the Team/s that the Project is assigned to. e.g. [“/CxServer/Team03, /CxServer/Team05”]<br>If an empty array is submitted then all Teams can access the Project.</p> |

## Success Response

Code: 201 Created

Attributes:

| Attribute                                 | Type                         | Enums                                | Description                                                                                                                                                       |
| ----------------------------------------- | ---------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                                        | string                       | -                                    | The unique identifier of the Project.                                                                                                                             |
| name                                      | string                       | -                                    | The name of the Project.                                                                                                                                          |
| isManaged                                 | boolean                      | <ul><li>True</li><li>False</li></ul> | <p>True if the Project is managed by GitHub. False if it is a “General” Project.<br><strong>Tip</strong> All Projects created via API are “General” Projects.</p> |
| <p>createdOn<br>(nullable)</p>            | <p>string<br>(date-time)</p> | -                                    | The date and time that the Project was created.                                                                                                                   |
| tenantId                                  | string                       | -                                    | The unique identifier of the tenant account.                                                                                                                      |
| <p>Branch<br>(nullable)</p>               | string                       | -                                    | The branch of the Project in GitHub, for GitHub Projects only.                                                                                                    |
| <p>assignedTeams[ ]<br>(nullable)</p>     | string                       | -                                    | Teams that were assigned to the Project.                                                                                                                          |
| <p>lastSuccessfulScanId<br>(nullable)</p> | string                       | -                                    | The unique identifier of the last successful scan of the Project.                                                                                                 |

### Sample Success Response

```
{
    "id": "636622e2-db25-496b-baeb-a264bfa88309",
    "name": "Demo04",
    "isManaged": false,
    "createdOn": "2021-04-11T14:00:25.5855168Z",
    "tenantId": "89c72e33-2d07-484d-914a-6d546fe31f07",
    "branch": "master",
    "assignedTeams": [
        "/CxServer/DemoTeam03"
    ],
    "lastSuccessfulScanId": null
}
```

## Error Response

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <div data-gb-custom-block data-tag="tabs"><div data-gb-custom-block data-tag="tab"><p><br></p></div><div data-gb-custom-block data-tag="tab" data-title="Status code: 400"><p><br>Message: <code>Bad data. Assigned teams inaccessible</code><br></p></div><div data-gb-custom-block data-tag="tab"><p><br></p></div><div data-gb-custom-block data-tag="tab" data-title="Status code: 409"><p><br>Message: <code>Project with such name exists</code><br></p></div><div data-gb-custom-block data-tag="tab"><p><br></p></div><div data-gb-custom-block data-tag="tab" data-title="Status code: 500"><p><br>Message: <code>InternalServerError</code><br></p></div><div data-gb-custom-block data-tag="tab"><p><br></p></div></div> |
