# Checkmarx SCA Release Notes November 2024

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

## SCA Resolver Releases

Download the latest version [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).

### Version 2.11.6

#### (November 20, 2024)

- For Gradle, fixed include modules feature to only resolve the specified modules and ignore the remaining modules.

### Version 2.11.4

#### (November 5, 2024)

- Added the "@" symbol to the list of allowed characters for parameter sanitization
- For Unity, improved detection of `manifest.json` files
- For SBT, fixed `plugins.sbt` file permissions for dependency resolution
- For Gradle, improved submodule detection
- For Nuget, improved framework package version detection
