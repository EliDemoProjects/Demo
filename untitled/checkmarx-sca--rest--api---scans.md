# Checkmarx SCA (REST) API - Scans

Once you have scanned a Project in Checkmarx SCA, you can use the **Scans** APIs to view general information about the scans, including their status, scan time/date, origin, and settings.

The following base URLs are used for all calls, depending on your environment:

- US Environment - https://api-sca.checkmarx.net
- EU Environment - https://eu.api-sca.checkmarx.net

The following is a list of the Checkmarx SCA APIs that relate to Scans:

| API | Method | Endpoint | Description |
| --- | --- | --- | --- |
| GET Scans | GET | /risk-management/scans | View info about all the scans of a specific Project.<br>You must include a `projectId` as a query parameter in your request.<br>By default, up to 10 results are returned. You can adjust this limit and apply pagination using the `size` and `page` parameters.<br>For example: GET: /risk-management/scans?projectId=\<your_project_id\>&size=100&page=1 |
| GET (Specific) Scan | GET | /risk-management/scans/{scanId} | View info about a specific scan, such as scan date, the ID of the associated Project, status, progress, etc. |
| GET Scan Status | GET | /api/scans/{scanId} | View the current status of a specific scan. |
| GET Scan Settings | GET | /risk-management/scans/{scanId}/settings | View whether or not the Exploitable Path feature was enabled for a specific scan. For GitHub Projects, this also returns the branch of the repository that was scanned. |
