# Checkmarx SCA Release Notes July 2023

{% include ".gitbook/includes/note-031596ef (1).md" %}

{% include ".gitbook/includes/warning-d19d3540 (1).md" %}

## Improvements and Bug Fixes

| Status | Item | Description                                                                                                                                                                                          |
| ------ | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UPDATE | SBOM | We added two optional query parameters to the `POST /export` API, `hideDevAndTestDependencies` and `showOnlyEffectiveLicenses`. These can be used to filter the results returned in the SBOM report. |

## SCA Resolver Releases

We released the following new versions of SCA Resolver:

{% hint style="info" icon="pencil" %}
The complete changelog, and links to download SCA Resolver are available [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).
{% endhint %}

### Version 2.2.11

* Fixed a bug related with exploitable path that the file was being generated in an incorrect format.

### Version 2.2.9

* Improved file handling of large results files.
* For PIP, Graphviz is now used instead of the pipdeptree tool.
