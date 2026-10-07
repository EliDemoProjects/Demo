# Checkmarx SCA Release Notes July 2026

{% include ".gitbook/includes/note-031596ef (1).md" %}

## SCA Updates

#### Added Support for PNPM Lockfile Resolution

SCA now supports dependency resolution using `pnpm-lock.yaml`, extending lockfile-based analysis to projects managed with PNPM.

When a `pnpm-lock.yaml` file is detected in a project, it is used as the authoritative source for resolving both direct and transitive dependencies, reflecting the exact versions installed by PNPM. For projects without a pnpm-lock.yaml, existing NPM-based resolution behavior is unchanged. This ensures that PNPM-managed projects receive accurate vulnerability and license risk analysis without requiring any changes to the project configuration.

## SCA Resolver

Download the latest version [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).

### Version 2.14.11 (July 22, 2026)

* Added arm64 version of installation files for each supported OS
* Added support for extraction of .whl, .tgz and .rpm file formats
* Added `packages-only` and `binary-only` arguments to Sbom generation
* Added support for Pnpm package manager
* Fixed Sbom format to use camelCase instead of PascalCase
* Added support for custom archive extensions extraction by adding `--include-archive-files` and `--include-extensionless-archives` optional arguments.
