# Checkmarx SCA (REST) API - Settings

The **Settings** APIs enable you to view and set the Exploitable Path settings for a specific Project.

The **Exploitable Path** feature leverages the ability to scan the actual Project code itself in parallel with scanning the manifest file, in order to validate whether the vulnerable open source packages are called from your proprietary code and whether the vulnerable methods are actually used by your code. For more information, see [Exploitable Path](exploitable-path.md).

The following base URLs are used for all calls, depending on your environment:

- US Environment - https://api-sca.checkmarx.net
- EU Environment - https://eu.api-sca.checkmarx.net

The following is a list of the Checkmarx SCA APIs that relate to Settings:

| **API** | **Method** | **Endpoint** | **Description** |
| --- | --- | --- | --- |
| GET (Specific Project) Settings | GET | /risk-management/settings/projects/{projectId} | View the Exploitable Path setting for a specific Project. |
| [PUT (Specific Project) Settings](checkmarx-sca--rest--api---put-settings.md) | PUT | /risk-management/settings/projects/{projectId} | Set the Exploitable Path setting for a specific Project. |
