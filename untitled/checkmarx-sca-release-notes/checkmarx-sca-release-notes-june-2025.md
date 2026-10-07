# Checkmarx SCA Release Notes June 2025

{% include ".gitbook/includes/note-031596ef (1).md" %}

{% include ".gitbook/includes/warning-d19d3540 (1).md" %}

## SCA Updates

### Managing Data Retention for SBOM Analysis

We now enable users to ensure that SBOM files sent to the SCA cloud for [File Analysis](https://app.gitbook.com/s/XSPACE_REST_API/checkmarx-sca--rest--api---file-analysis) are purged as soon as possible. When using the File Analysis API, which runs an SCA scan on an SBOM that you submit, you can now set `DisableRetention` as `true` so that as soon as the Analysis report has been retrieved successfully once, all related data is deleted from the SCA cloud. When this parameter is `false` (default) then the current policy of retaining the data for 5 days and allowing multiple retrievals of the report remains in place.

This enables users to improve security by keeping data retention in the cloud to the absolute minimum.
