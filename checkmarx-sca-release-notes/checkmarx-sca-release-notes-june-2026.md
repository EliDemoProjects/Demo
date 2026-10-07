# Checkmarx SCA Release Notes June 2026

{% include "../.gitbook/includes/note-031596ef.md" %}

## SCA Updates

### Improved npm Dependency Resolution

Improved accuracy of npm dependency resolution for modern projects (npm v7 or later) by leveraging the new native peer dependency resolution when available. This results in more complete dependency trees and broader vulnerability coverage.

## SCA Resolver

Download the latest version [here](../checkmarx-sca-resolver/checkmarx-sca-resolver-changelog.md).

### Version 2.14.3 (June 16, 2026)

* For Ruby, improved dependency detection
* Improved version sanitization
* Improved Delta Scan detection
* Added an option to generate SBOM output
* Removed the use of `legacy-peer-deps` for NPM
* Improved resilience when downloading reports.
* For Pip, added support for scanning projects located in folders that contain spaces.
