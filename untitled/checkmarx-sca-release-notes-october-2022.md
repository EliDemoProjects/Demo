# Checkmarx SCA Release Notes October 2022

We are excited to announce important improvements in our Checkmarx SCA web application…

## Improvements and Bug Fixes

| Status | Item | Description |
| --- | --- | --- |
| UPDATED | Gradle string declarations | Gradle now supports single quotes, quotes, triple quotes and forward slash string declaration in submodule inclusions. |
| FIXED | Version compare | Fixed issues with the versions comparer in Evidence Resolver and Remediation Intelligence . |

## Checkmarx SCA Resolver Updates

We have released several new versions of Resolver with a wide range of improvements and bug fixes. Download the latest version of SCA Resolver [here](checkmarx-sca-resolver-download-and-installation.md).

### Improvements in Version 1.13.4

- For Container Scan:

  - Uses image resolver version 1.0.7.
  - Added support for resolution of image files without using Dockerfile.

- For Carthage, added authentication for private repositories based on `.netrc` file.

- For Gradle, improved sub-module resolution.

- For Python, users are now able to specify the version of pipdeptree to be used.

### Improvements in Version 1.12.2

- For Python, Resolver now has a consistent behavior for installing `pipdeptree`. For Python 2, it installs version 2.2.1; for Python 3 it installs 2.3.1.

- For Gradle:

  - Added support for project method in `settings.gradle`.
  - Resolver now ignores the IncludeBuild method in `gradle.settings` file.
  - Improved the way we get the Gradle wrapper version from the distribution URL.

- Container Scan - Resolver now scans containers via a dedicated Container CLI. When you extract the downloaded archive, it now contains an additional executable `ImageResolverCli.exe`.

  {% hint style="info" %}
  The new architecture does not affect the functionality in any way. When you extract the downloaded archive, it now contains an image resolver executable (in addition to the Resolver executable).
  {% endhint %}
