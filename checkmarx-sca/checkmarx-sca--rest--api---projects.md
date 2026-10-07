# Checkmarx SCA (REST) API - Projects

A Project in Checkmarx SCA is a logical entity that represents a source repository, such as a component, microservice, etc. which you intend to scan for vulnerable dependencies. Each time that you run a scan on the source repository you do so under the same Project, enabling you to track vulnerabilities in Checkmarx SCA throughout your SDLC. When you create a Project, you configure the Project settings, including specifying Teams for access control.

You can perform all CRUD actions on Projects via API.

{% hint style="info" icon="pencil" %}
Once you have created a Project you can run a scan of that Project using the [Scan Upload](checkmarx-sca--rest--api---scan-upload.md) APIs.
{% endhint %}

The following base URLs are used for all calls, depending on your environment:

- US Environment - [https://api-sca.checkmarx.net](https://api-sca.checkmarx.net/)
- EU Environment - [https://eu.api-sca.checkmarx.net](https://eu.api-sca.checkmarx.net/identity/connect/token)

The following is a list of the Checkmarx SCA APIs that relate to Projects:

| **API** | **Method** | **Endpoint** | **Description** |
| --- | --- | --- | --- |
| GET Projects | GET | /risk-management/projects | View info about all the Projects in your account. |
| [POST Projects](checkmarx-sca--rest--api---post-project.md) | POST | /risk-management/projects | Create a new Project. The user specifies the Project name and configures the Project settings. The response returns a unique Project ID which is used to refer to the Project. |
| GET (Specific) Project | GET | /risk-management/projects/{id} | View info about a specific Project. |
| [PUT Project](checkmarx-sca--rest--api---put-project.md) | PUT | /risk-management/projects/{id} | Update the Project name and/or the Teams assigned to the Project. |
| DELETE Project | DELETE | /risk-management/projects/{id} | Delete a Project. |
