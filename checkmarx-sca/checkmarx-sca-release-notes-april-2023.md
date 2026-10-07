# Checkmarx SCA Release Notes April 2023

{% include ".gitbook/includes/note-031596ef.md" %}

{% hint style="warning" %}
We are in the process of rolling out a new comprehensive Management of Risks service which will replace the current service. The current APIs `IgnoreVulnerability` and `UnignoreVulnerability` will soon be deprecated. Please plan accordingly. For more info, feel free to contact your Technical Account Manager.
{% endhint %}

## Global Inventory and Risks

We have revamped the system used for gathering data for the Global Inventory and Risks screen. We now use a dedicated service to process the data. This will greatly improve the performance of this feature, improving pagination, searchability and responsiveness.

The new service retains data for only one and a half years, so that packages and risks that haven't been detected by any recent scans aren't shown on this screen.

{% hint style="info" icon="pencil" %}
The data shown in Scan Results for specific projects is retained for a longer period of time.
{% endhint %}

## Support for Unity Package Manager

We added support for Unity package manager.

<details>
<summary>Details About Unity Support</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-8b3dcc8e671fe99e2fe76c9a40c74069.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> Unity</p><p><strong><strong>Repository:</strong></strong> <a href="https://github.com/orgs/Unity-Technologies/repositories">Unity Technologies</a>, <a href="https://github.com/orgs/needle-mirror/repositories">Needle-mirror</a>, <a href="https://openupm.com/packages/">Open UPM</a></p><p><strong><strong>File Types:</strong></strong> none</p></td></tr>
<tr><td><p><strong><strong>Supported Package Managers</strong></strong></p></td><td><p><strong><strong>Exploitable Path</strong></strong></p></td><td><p><strong><strong>Supply Chain Security (SCS)</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong> (Packages marked with <img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</p></td></tr>
<tr><td><p>none</p></td><td><p></p></td><td><p></p></td><td><p>manifest.json<img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, packages.json<img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"></p></td></tr>
</tbody>
</table>

</details>

### File Extraction

We now extract .jar compressed files, and scan the extracted files (in addition to existing support for .war, .ear and .zip). We have also increased the recursive extraction to 4 levels of depth.

## SCA Resolver Releases

We released the following new versions of SCA Resolver:

{% hint style="info" icon="pencil" %}
The complete changelog, and links to download SCA Resolver are available [here](checkmarx-sca-resolver-changelog.md).
{% endhint %}

### Version 2.1.5

- Added support for Unity package manager. For more information, see [Unity Package Manager Dependency Resolver](installing-supported-package-managers-for-resolver.md#UUID-6a56714b-6836-a1e0-3c21-d1fbb411cf4d_section-idm33363974042884).
- For Bower, fixed issue that dependency resolution was failing when latest version ("\*") was specified.
- For Ivy, fixed issue that unused versions were being resolved despite the fact that a newer version had been specified in the manifest file.
- ImageResolver updated to version 2.0.43.

### Version 2.1.2

- Added support for authentication via Master Access Control, see [Master Access Control Authentication for Checkmarx SCA Resolver](master-access-control-authentication-for-checkmarx-sca-resolver.md).
- For Sbt, stack overflow is fixed when building the dependency tree.
- For Gradle, when a submodule is duplicated in a project we now resolve the package only once.
- ImageResolver was updated to version 2.0.41.
