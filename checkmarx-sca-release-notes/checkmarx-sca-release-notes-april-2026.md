# Checkmarx SCA Release Notes April 2026

{% include "../.gitbook/includes/note-031596ef.md" %}

## SCA Updates

### Additional OSS License Support

We added support for identifying the following licenses that apply to OSS packages: AFL-3.0, CPAL-1.0, OSL-3.0, APSL-2.0, Watcom-1.0 and LPPL-1.3c.

### Python and NuGet Support for Automated Remediation Workflows

SCA remediation now supports Python and NuGet packages. You can download a remediated manifest file (e.g., requirements.txt for Python and \*.csproj for NuGet) with secure package versions directly from the UI or via the export service API.

This expansion brings Python and .NET developers into parity with existing workflows, giving teams manual remediation paths to address open-source vulnerabilities across a broader range of ecosystems. Learn more about [Remediation using a Manifest File](../checkmarx-sca-user-guide/remediation-using-a-manifest-file.md).
