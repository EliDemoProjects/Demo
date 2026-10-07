---
title: Workflow
---

{% hint style="info" icon="pencil" %}
You need to have the Project ID of the project that you would like to scan in order to run the Scan Upload API. See [Checkmarx SCA (REST) API - Projects](../../untitled/.gitbook/includes/checkmarx-sca--rest--api---projects.md).
{% endhint %}

To scan a zip file

1. Use `POST /api/uploads` to generate an upload link.
2. Use `PUT /{uploadLink}`, specifying the path to your ZIP file, to upload your file.
3. Use `POST /api/scans`, specifying the Project ID and upload link, to scan the ZIP file.
4. Use `GET /api/scans/{scanId}` to check the status of the scan.
5. View the results using the [Export Service](../../untitled/.gitbook/includes/checkmarx-sca--rest--api---export-service.md). Alternatively, you can view the results in the Checkmarx SCA web browser (UI), see [Viewing Results](../../untitled/.gitbook/includes/viewing-results.md).

To scan from GitHub repo

1. Use `POST /api/scans` (along with the Project ID and GitHub URL) to scan the Project.
2. Use `GET /api/scans/{scanId}` to check the status of the scan.
3. View the results using the [Export Service](../../untitled/.gitbook/includes/checkmarx-sca--rest--api---export-service.md). Alternatively, you can view the results in the Checkmarx SCA web browser (UI), see [Viewing Results](../../untitled/.gitbook/includes/viewing-results.md).
