# Checkmarx SCA Release Notes October 2024

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

## New Project Page

We have fundamentally restructured the screens that show Project information in the SCA web application.

- Clicking on the row of a Project in the **Dashboard** now takes you directly to the main **Project** page which contains all information about that Project, including the overview, the scan history and detailed scan results (it is no longer necessary to click on the **Scan Results** button). The info on this page is divided into the following tabs: Project Overview, Packages, Risks, Container, Licenses, Remediation Tasks and Policy Violations.

- The list of scans, which had been shown in the **Scan History** tab of the **Overview** page, is now shown below the overview widgets in the **Project Overview** tab.

  {% hint style="warning" %}
  The **Top Vulnerabilities** section that had been shown in that position has been deprecated.
  {% endhint %}

- The info that had been shown in the **Scan Summary** tab of the **Scan Results** page is now available from the more options menu <img src=".gitbook/assets/img-1d1787297384426534f8e8ba6ac6cb44.png" alt="" data-size="line"> at the top of **Project** page (for all tabs). The section showing details of the scan process is now accessed by selecting **Scan Details**. The section showing info about the package resolution process (e.g., successful and failed manifest files) is now accessed by selecting **Resolving Info**.

Aside from the changes in the way the info is presented, this update also involves fundamental changes to how the data is gathered "under the hood". This will improve efficiency and ensure more consistent and uniform behavior of aggregated counters.

## Delta Scan

We have dramatically cut the time of SCA scans by introducing the new Delta scan feature. When rescanning an existing project, if the manifest files haven’t been changed since the last scan, then we skip the dependency resolution process. This can cut scan times by up to 95% without detracting from the accuracy of the scan. For more information, see [SCA Delta Scan](/document/preview/253719#UUID-63e2b71c-52f3-397e-b843-06f91e911551).

### Current Limitations

- Only applies to scans run in the cloud, not to scans using SCA Resolver.
- Supported for all languages and package managers for which dependency resolution is done using manifest files except for C and C++.
- Does not apply to languages for which dependency resolution is done by file analysis (fingerprint method).
- Currently available only in multi-tenant environments, not in single-tenant.

## Show all manifest files

We now show all manifest files that were detected, even if no packages were identified in that manifest.
