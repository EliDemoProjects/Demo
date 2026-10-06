# Checkmarx SCA Release Notes November 2023

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

## Improvements

| **Status** | **Item** | **Description** |
| --- | --- | --- |
| UPDATE | Persistent filters | The filters applied to the Global Inventory page are now persistent, so that when you drill-down to see details for a package or a risk and then click the back button in the browser, the filters on the Global Inventory page will remain in place. |
| FIXED | Project name | Fixed issue that changing project name in repo for a Checkmarx One project had caused errors for the SCA scanner. |

## Persistent Filters

The filters applied to the Global Inventory page are now persistent, so that when you drill-down to see details for a package or a risk and then click the back button in the browser, the filters on the Global Inventory page will remain in place.

## SCA Resolver Releases

We released the following new versions of SCA Resolver:

{% hint style="info" icon="pencil" %}
The complete changelog, and links to download SCA Resolver are available [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).
{% endhint %}

### Version 2.5.13

- Fixed issue that the MacOS artifact hadn't been published in prior versions (2.4.8, 2.5.2 and 2.5.11).

### Version 2.5.11

- We now only create a reports folder when the user actually generates a report.
- Fixed the fingerprint calculation for JavaScript files.
- For container scans, updated ImageResolver to version 3.0.31, which includes the following updates:

  - We now scan yaml files, enabling detection of images inside docker-compose files and helm charts. This dramatically increases our coverage for detecting container images.

    {% hint style="info" %}
    If you prefer to exclude these files from a scan, you can do so using the command `--excludes "*.yaml"`.
    {% endhint %}
  - Improved detection of Java and IOS package inside images.
  - Enabled running container scans via Checkmarx One CLI.

    This is done by using SCA Resolver in the CLI command, and setting the Resolver params as follows:

    - `--scan-containers`
    - `--containers-result-path <base_folder_path>/.cxsca-container-results.json`

      {% hint style="info" %}
      \<base_folder_path\> must be identical to the value given for `-s`.

      The precise file name `.cxsca-container-results.json` must be used.
      {% endhint %}

    Learn more about running container scans [here](https://app.gitbook.com/s/XSPACE_RESOLVER/running-scans-using-checkmarx-sca-resolver#UUID-af718204-6dfc-2b27-439e-419b9157d364_section-idm33346502401272)

### Version 2.5.2

- We now sanitize the parameters passed to the package managers. We also added a flag, `--disable-parameter-sanitization` (and a config parameter), in case you would like to disable this feature.
- Added a flag, `--logs-path`, for passing the logs directory name in the CLI command (in addition to existing support for setting it in the config file).
- For container scans, we added a flag, `--containers-cache-path` (and a config parameter), for setting the path to the directory where the container images cache is written.
- For CocoaPods, fixed the error that caused the scan to fail when the lock file parse failed for a dependency.

## Nexus Plugin

We released version 1.1.6 of the Checkmarx SCA Nexus plugin.

In this version, we fixed a bug in custom tasks for repository groups.

{% hint style="warning" %}
It is important to update to the new version, since the old version uses an outdated SCA database.
{% endhint %}
