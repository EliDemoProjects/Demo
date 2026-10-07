# Checkmarx SCA Release Notes March 2026

{% include ".gitbook/includes/note-031596ef.md" %}

## SCA Updates

### Added Support for Python 3.14

Checkmarx SCA now supports dependency resolution for Python 3.14 for scans run in the cloud as well as via SCA Resolver. This enables accurate SCA scanning of Python 3.14 projects, helping to maintain continuous visibility into security and license risk for customers who are adopting the newer Python version.

### Added Support for .NET 10 (LTS)

Checkmarx SCA now supports dependency resolution for .NET 10 (Long-Term Support), enabling teams to scan NuGet dependencies in .NET 10 projects. As an LTS release, .NET 10 is the preferred target for enterprise and production workloads, making reliable SCA coverage essential for maintaining a secure open-source supply chain over its multi-year support lifecycle.

### Added Support for Java 25 (LTS)

Checkmarx One now supports dependency resolution for Java 25 (Long-Term Support), enabling teams to scan Maven and Gradle dependencies in Java 25 projects. As an LTS release, Java 25 is the preferred target for enterprise and production workloads, making reliable SCA coverage essential for maintaining a secure open-source supply chain over its multi-year support lifecycle.

## SCA Resolver

Download the latest version [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).

### Version 2.13.3 (Feb 25, 2026)

- Added support for [Delta Scan](/document/preview/322318#UUID-2865b187-60e6-84f0-67c8-c5313ef205fc_section-idm234701538181768) resolution on Checkmarx One CLI scans, dramatically cutting the time of SCA scans when rescanning an existing project. When running SCA scans via the Checkmarx One CLI (v 2.3.44+) using Resolver (this version and above), the Delta Scan feature will now run by default. This setting can be overriden by using the `--sca-resolver-params` flag with the argument `--disable-delta-scan`.
