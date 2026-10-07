# Checkmarx SCA (REST) API - Scan Upload

You can use the **Scan Upload** APIs to run a scan of a Project by uploading a zip file or by referring to its GitHub URL.

{% hint style="info" icon="pencil" %}
Before you can start running scans via API, you need to create your Project. If you haven’t yet set up a Project for the source code that you would like to scan, then first create the Project as described in [Checkmarx SCA (REST) API - POST Project](checkmarx-sca--rest--api---post-project.md).

Alternatively, you can create the Project in the Checkmarx SCA web portal, see [Creating a Project - Project Types](creating-a-project---project-types.md).
{% endhint %}

{% hint style="info" icon="pencil" %}
The scanning procedure is identical whether this is the initial scan after creating the Project or whether you are rescanning a Project that has already been scanned.
{% endhint %}

The following base URLs are used for all calls, depending on your environment:

- US Environment - https://api-sca.checkmarx.net
- EU Environment - https://eu.api-sca.checkmarx.net

{% include ".gitbook/includes/section-9c82ca9c.md" %}

## Scan Upload APIs

The following is a list of the Checkmarx SCA APIs that relate to Scan Upload:

{% hint style="info" icon="pencil" %}
If a GitHub URL is being scanned (as opposed to a zip file), then the only API needed is POST Scan.
{% endhint %}

| API | Method | Endpoint | Description |
| --- | --- | --- | --- |
| [POST Generate Upload Link](checkmarx-sca--rest--api---post-scans-generate-upload-link.md) | POST | /api/uploads | Generate an upload link for scanning a ZIP file.<br>This returns an Upload Link which is used in **PUT Upload Link** and **POST Scan**. |
| [PUT Upload Link](checkmarx-sca--rest--api---put-upload-link.md) | PUT | {upload_url} | Upload the ZIP file to Checkmarx SCA.<br>The url is the url that you generated using **POST Generate Upload Link**.<br>The Body parameter is the path to the zip file on your local machine. |
| [POST Scan](checkmarx-sca--rest--api---post-scan.md) | POST | /api/scans | Scan the previously uploaded ZIP file (or the GitHub URL).<br>The user specifies the Project ID and includes the previously generated Upload Link (or the GitHub file URL).<br>The response returns a Scan ID which you can use with Risk Reports to view results. |
