# Checkmarx SCA Release Notes August 2023

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

## Improvements and Bug Fixes

| **Status** | **Item** | **Description** |
| --- | --- | --- |
| UPDATE | Supported manifest files | We added support for resolving Swift dependencies using the `Package.resolved` file when no `Package.swift` file is present in the project. |

## SCA Resolver Releases

We released the following new versions of SCA Resolver:

{% hint style="info" icon="pencil" %}
The complete changelog, and links to download SCA Resolver are available [here](checkmarx-sca-resolver-changelog.md).
{% endhint %}

### Version 2.4.2

- For Container Scans, updated ImageResolver to version 3.0.7, which includes the following updates:

  - In order to run container scans via Resolver, you are now required to have Syft version 0.83 installed on your local machine.
  - Added support for Podman (in addtion to Docker).
  - It is no longer required to have Docker installed in order to run container scans on public images. However, if you are scanning private images, then you need to have Docker or Podman installed, and you need to be authenticated for the relevant image registry, e.g., Jfrog, ECR, GCR, Nexus etc.
  - Improved process for identifying packages and vulnerabilities, yielding more comprehensive results

### Version 2.3.3

- When multi-module projects cause manifest files to be duplicated in the results, we now merge the results from both manifests so that the scan can complete successfully.

- For Poetry, added the flag `--poetry-parameters` for adding custom parameters for Poetry.

- For Python:

  - When there is a problem resolving the dependencies from a manifest file, we now correctly show a failure for the resolution of that manifest file.
  - Added support for pyenv configuration.

- For Gradle, fixed issue that despite the `--gradle-include-modules` flag being used, non-included modules were still being scanned.

- For NPM, improved the method for resolving workspaces, so that it is no longer necessary to change the content of the package-lock file.

## JFrog Plugin

We released version 1.1.10 of the Checkmarx SCA JFrog plugin.

This is a free tool for running Checkmarx SCA scans on your JFrog artifacts.

{% hint style="warning" %}
It is important to update to the new version, since the old version uses an outdated SCA database.
{% endhint %}
