# Checkmarx SCA Release Notes September 2022

We are excited to announce important improvements in our Checkmarx SCA web application…

## Key improvements

### Support for C# for Exploitable Path

The Checkmarx SCA Exploitable Path feature checks for an exploitable path from your proprietary code to the vulnerable methods in your open source packages. We have added support for C# for this feature (in addition to Java, Python and JavaScript). See [Exploitable Path](exploitable-path.md)

The queries for configuring Exploitable Path for C# are available [here](https://checkmarx.atlassian.net/wiki/spaces/CR/pages/6497632313/Checkmarx+SCA+Resources).

### NPM Audit Signatures

We now verify the integrity of npm packages by running the `npm audit signatures` command. This compares the signature of the package that you are using with the signature registered with npm for that package.

{% hint style="warning" %}
To use this feature, it is required that you include the `node_modules` folder in the project that you are scanning.
{% endhint %}

## Improvements and Bug Fixes

| **Status** | **Item** | **Description** |
| --- | --- | --- |
| FIXED | Problem with settings.gradle file | Fixed issue that when a settings.gradle file contains an IncludeBuild property, it had been causing the scan to fail. |
| FIXED | Remediation tasks | We now remove the downstream remediation tasks when they don't have any vulnerabilities. |
| FIXED | Package Usage | Fixed inaccuracies in how potentially used packages are shown in the UI. |

## Checkmarx SCA Resolver Updates

We have released several new versions of Resolver with a wide range of improvements and bug fixes. Download the latest version of SCA Resolver [here](checkmarx-sca-resolver-download-and-installation.md).

### Improvements in Version 1.11.3

- For Gradle, improved results by preventing Gradle from resolving multiple projects simultaneously.

- For Python:

  - Added support for Poetry package manager
  - Added support for PIP to resolve dependencies from the following files: `pyproject.toml`, `setup.cfg` and `setup.py`.

- For Composer, we now attempt to resolve dependencies without running the install command.

## Checkmarx SCA Plugin for Jfrog

We released version 1.0.17 of the plugin ([download link](https://sca-downloads.s3.amazonaws.com/ScaJFrogPlugin/1.0.17/sca-jfrog-plugin.zip))

In the new version, we added support for Bower, CocoaPods, Composer, Go, Ivy and Sbt (in addition to NPM, Maven, Gradle, NuGet and Pypi).
