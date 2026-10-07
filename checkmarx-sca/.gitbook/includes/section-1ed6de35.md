---
title: Workflow
---

1. Use `POST /api/uploads` to generate an upload link.
2. Use `PUT {upload_url}` , specifying the path to your zip file, to upload your file.
3. Use `POST /api/scans`, specifying the Project ID and upload link, to scan the zip file.
4. Use `GET /api/scans/{scanId}` to check the status of the scan.
5. View the results using the [Scan Reports API](../../untitled/.gitbook/includes/checkmarx-sca--rest--api---get-scan-reports-and-sboms.md). Alternatively, you can view the results in the Checkmarx SCA web browser (UI), see [Viewing Results](../../untitled/.gitbook/includes/viewing-results.md).
