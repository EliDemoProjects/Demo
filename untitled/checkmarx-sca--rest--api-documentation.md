# Checkmarx SCA (REST) API Documentation

You can access the full functionality of the Checkmarx SCA platform using our external (REST) APIs. You can perform the following actions vai API: CRUD actions on Checkmarx SCA Projects, run scans, view scan results, and generate Risk Reports.

Checkmarx SCA uses Access Tokens for authentication of all API calls. Access Tokens can be acquired using the login credentials that you use to log in to the web platform. Each session begins with generating an Access Token, which is valid for one hour. That token is then used in the header with each API call.

{% hint style="info" icon="pencil" %}
Make sure that your firewall is configured to allow access to all relevant Checkmarx SCA endpoints, see [Connectivity to Checkmarx SCA Cloud](connectivity-to-checkmarx-sca-cloud.md).
{% endhint %}

## Workflow

The following represents a standard workflow for creating a new Project, running a scan on that Project and viewing results.

1. Use[`POST /identity/connect/token`](checkmarx-sca--rest--api---post-token.md) to generate an Access Token.
2. Use `POST risk-management/projects` to create a new Project and generate a Project ID.
3. If you would like to activate Exploitable Path, use `PUT /risk-management/settings/projects/{projectId}` to configure the Exploitable Path settings.
4. If your source code is in a zip file, use `POST /api/uploads` to generate an upload link and then use `PUT /{uploadLink}` and the path to your zip file to upload your file.
5. Use `POST /api/scans` , specifying the URL of the uploaded file or Git repository, to scan the Project.
6. You can check the status of the scan using `GET /api/scans/{scanId}` .
7. View the results using the [Export Service](checkmarx-sca--rest--api---export-service.md) APIs.

{% hint style="info" icon="pencil" %}
Alternatively, you can view the results in the Checkmarx SCA web browser (UI), see [Viewing Results](viewing-results.md).
{% endhint %}
