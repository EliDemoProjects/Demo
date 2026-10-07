# Checkmarx SCA Release Notes September 2024

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

## Support for Pub Package Manage

We have added limited support for Pub package manager.

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-7b8261dae4e6c7d876b28a7c1bf2f147.jpg" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> Dart, Flutter</p><p><strong><strong>Repository:</strong></strong> N/A</p><p><strong><strong>File Types:</strong></strong> none</p><p><strong><strong>Exploitable Path:</strong></strong> Not supported</p></td></tr>
<tr><td><p><strong><strong>Supported Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong></p></td></tr>
<tr><td><p>Pub</p></td><td><p></p></td><td><p></p></td><td><p><code>pubspec.lock</code></p></td></tr>
</tbody>
</table>

## SCA Resolver Releases

Download the latest version [here](checkmarx-sca-resolver-changelog.md).

### Version 2.11.2

#### (Sep 20, 2024)

- Added support for Pub package manager (for Dart and Flutter frameworks).

  {% hint style="info" icon="pencil" %}
  Current limitations: Only identifies direct dependecies and only identifies Malicious Packages.
  {% endhint %}

- Performance optimization during folder analysis.

- Improved Risk Report and SBOM generation. SBOMs are now generated in [CycloneDX v1.5](https://cyclonedx.org/docs/1.5/#SchemaProperties) format (instead of v1.3).

- For Gradle, we now remove dependencies which Gradle marks as FAILED (such as packages that conflict with a different package version) from our scan results.

### Version 2.10.2

#### (September 3, 2024)

- For Npm, improved package.json identification when lerna.json is present

- For RubyGems, fixed circle dependencies

- For Yarn, fixed direct dependency identification for yarn.lock v2

- We added the following items to the scan summary that is shown when a scan is completed:

  - Outdated packages
  - Vulnerable packages, with breakdown by severity level
  - Legal risks, with breakdown by severity level
  - Critical and Info level severity are now displayed. (However, results for these severities are only identified in accounts for which this feature has been activated.)
