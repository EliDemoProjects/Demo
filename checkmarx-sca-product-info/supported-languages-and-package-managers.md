# Supported Languages and Package Managers

<details>

<summary>How SCA Works</summary>

Checkmarx SCA uses the following methods to identify the 3rd party packages in your project:

1.  File Analysis – Checkmarx SCA identifies all files in your project that may be part of a 3<sup>rd</sup> party package, and analyzes them in order to determine which packages are being used. This is done by comparing the hashes and metadata of the relevant files (e.g., .jar files for Java, .js files for JS) in the scanned project with the hashes and metadata of packages that are catalogued in our database. As part of this process, compressed files of supported types (.jar, .war, .ear, .zip) are extracted so that the files can be analyzed. This is applied recursively up to four levels of depth.

    File Analysis is done for the supported languages/frameworks listed below, using the corresponding file types specified in the table.
2.  Dependency Resolution - Checkmarx SCA resolves dependencies using one of two methods:

    * Package Manager Resolution (default)
      * Checkmarx SCA uses package managers to resolve dependencies against customer-defined or public repositories and reconstruct the dependency tree based on manifest files (e.g., `package.json`). These files define the intended dependencies, typically using version ranges.
      * Because this method depends on the state of external repositories at scan time, the resulting dependency tree may differ from what was originally installed. In some cases, this can lead to incomplete or inconsistent dependency reconstruction, especially if package versions have been removed, updated, or resolved differently across environments.
    * Lock File Resolution
      * When a lock file is present (e.g., `package-lock.json`, `yarn.lock`), Checkmarx SCA uses it to determine the exact versions of all resolved dependencies, including transitive dependencies. This provides a deterministic and reproducible view of the dependency tree as it was installed.
      * This method significantly improves accuracy and reduces the risk of missing dependencies or security findings caused by differences in resolution behavior or changes in package availability.

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>To ensure accurate and reproducible results, it is strongly recommended to include lock files in SCA scans. Lock files reflect the exact dependency tree used in the application and improve both vulnerability detection and auditability of scan results.</p></div>

For more information about how Checkmarx SCA scans run using various methods, refer to [Understanding How Checkmarx SCA Scans Run Using Various Methods](understanding-how-checkmarx-sca-scans-run-using-various-methods.md).

</details>

{% hint style="info" icon="pencil" %}
If you are using Checkmarx SCA Resolver, then you need to install the relevant package managers locally. For installation info, see [Installing Supported Package Managers for Resolver](../checkmarx-sca-resolver/checkmarx-sca-resolver-download-and-installation/installing-supported-package-managers-for-resolver.md).
{% endhint %}

## Supported Languages and Package Managers

[Java](supported-languages-and-package-managers.md#UUID-9c93d6b8-4b0b-b4de-ee58-9e99b1ec02ba_section-idm4494748069177633396069421573_body)

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-113e175db6fc1cdfe0c2663d7c33ae55.png" alt="" data-size="original"></td><td colspan="4"><p><strong>JVM Languages:</strong> Java, Kotlin, Android, Groovy, Scala</p><p><strong>Additional Frameworks:</strong> Struts, Spring</p><p><strong>Repository:</strong> Maven Central, Sonatype, Apache</p><p><strong>File Types:</strong> .jar</p><p><strong>Supported Languages for Exploitable Path:</strong> Java</p></td><td></td></tr><tr><td><strong>Package Managers</strong></td><td><strong>Vulnerability Support</strong></td><td colspan="2"><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong></td><td></td></tr><tr><td>Maven</td><td></td><td colspan="2"></td><td><code>pom.xml</code></td><td></td></tr><tr><td>Gradle</td><td></td><td colspan="2"></td><td colspan="2"><code>build.gradle</code> , <code>build.gradle.kts</code></td></tr><tr><td>Ivy</td><td></td><td colspan="2"></td><td><p><code>ivy.xml</code>,</p><p><code>build.xml</code></p></td><td></td></tr><tr><td>SBT</td><td></td><td colspan="2"></td><td><code>build.sbt</code></td><td></td></tr></tbody></table>

<details>

<summary>JavaScript/TypeScript</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-0aa99a0522a4571621fa63a1599845db.png" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> JavaScript, TypeScript, NodeJS, React, Angular, Apex</p><p><strong>Tip</strong></p><p>Apex is only supported when running the scan using Checkmarx SCA Resolver with the <code>--extract-archives resource</code> argument, see <a href="../checkmarx-sca-resolver/checkmarx-sca-resolver-configuration-arguments.md">Checkmarx SCA Resolver Configuration Arguments</a>.</p><p><strong>Repository:</strong> NPM</p><p><strong>File Types:</strong> .js</p><p><strong>Supported Languages for Exploitable Path:</strong> JavaScript</p></td></tr><tr><td><strong>Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong> (Packages marked with <img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</td></tr><tr><td>NPM</td><td></td><td></td><td><code>package.json</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> , <code>package-lock.json</code><sup>1]</sup></td></tr><tr><td>Yarn (and Yarn 2)</td><td></td><td></td><td><code>package.json</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> , <code>yarn.lock</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"><sup>1]</sup></td></tr><tr><td>Bower</td><td></td><td></td><td><code>bower.json</code></td></tr><tr><td>Pnpm</td><td></td><td></td><td><code>pnpm-lock.yaml</code></td></tr></tbody></table>

1] When a `lock` file is present in the project, SCA may use it to resolve dependencies. Therefore, it is important to keep the lock file up-to-date with any changes that you make in the manifest file.

</details>

<details>

<summary>.NET</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-cc258c57dd6a07bba226176fa1579825.jpg" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> C#, F#, .NET, .NET Core, WCF, WPF, ASP.NET</p><p><strong>Repository:</strong> NuGet</p><p><strong>File Types:</strong> .dll</p><p><strong>Supported Languages for Exploitable Path:</strong> C#</p></td></tr><tr><td><strong>Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong></td></tr><tr><td>NuGet</td><td></td><td></td><td><code>*.csproj</code> , <code>packages.config</code>, <code>project.assets.json</code>, <code>packages.lock.json</code></td></tr></tbody></table>

</details>

<details>

<summary>Python</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-224a5acf482ebf711d9adf7337adf4eb.png" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> Python, Django, Flask</p><p><strong>Repository:</strong> PyPi</p><p><strong>File Types:</strong> .egg, .whl</p><p><strong>Supported Languages for Exploitable Path:</strong> Python</p></td></tr><tr><td><strong>Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong> (Packages marked with <img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</td></tr><tr><td>PIP</td><td></td><td></td><td><code>requirements.txt</code>, <code>requirements-*.txt</code>, <code>requirement.txt</code>, <code>requirement-*.txt</code></td></tr><tr><td>Poetry</td><td></td><td></td><td><code>pyproject.toml</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>poetry.lock</code></td></tr><tr><td>Setuptools <sup>1]</sup></td><td></td><td></td><td><code>Setup.cfg</code>, <code>Setup.py</code></td></tr><tr><td>UV</td><td></td><td></td><td><code>uv.lock</code>, <code>requirements.txt</code>, <code>pyproject.toml</code></td></tr></tbody></table>

1] Setuptools is supported only when running scans using SCA Resolver.

</details>

<details>

<summary>PHP</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-a8bf03c955b6b95eb2418f9e405eba2e.png" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> PHP, Drupal</p><p><strong>Repository:</strong> Packagist</p><p><strong>File Types:</strong> none</p><p><strong>Exploitable Path:</strong> Not supported</p></td></tr><tr><td><strong>Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong> (Packages marked with <img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</td></tr><tr><td>Composer</td><td></td><td></td><td><code>composer.json</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> , <code>composer.lock</code></td></tr></tbody></table>

</details>

<details>

<summary>iOS</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-d6cd5ddc4653ff1eb4362f8567516f0c.png" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> Swift, Objective c</p><p><strong>Repository:</strong> GitHub</p><p><strong>File Types:</strong> none</p><p><strong>Exploitable Path:</strong> Not supported</p></td></tr><tr><td><strong>Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong> (Packages marked with <img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</td></tr><tr><td>SwiftPm</td><td></td><td></td><td><code>Package.swift</code>, <code>Package.resolved</code></td></tr><tr><td>CocoaPods</td><td></td><td></td><td><code>Podfile</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>Podfile.lock</code></td></tr><tr><td>Carthage</td><td></td><td></td><td><p><code>Cartfile</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>Cartfile.private</code>, <code>Cartfile.resolved</code></p><p><strong>Tip</strong></p><p>At least one <code>.private</code> or <code>.resolved</code> file must be included.</p></td></tr></tbody></table>

</details>

<details>

<summary>Go</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-ca7790723e5bac8285198d139444c923.png" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> Go</p><p><strong>Repository:</strong> Golang</p><p><strong>File Types:</strong> none</p><p><strong>Exploitable Path:</strong> Not supported</p></td></tr><tr><td><strong>Supported Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong> (Packages marked with <img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</td></tr><tr><td>GoModules</td><td></td><td></td><td><code>go.mod</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>go.sum</code></td></tr></tbody></table>

</details>

<details>

<summary>Ruby</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-6d2e8a2b8e361dd5f394edd3b435a601.png" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> Ruby</p><p><strong>Repository:</strong> RubyGems</p><p><strong>File Types:</strong> none</p><p><strong>Exploitable Path:</strong> Not supported</p></td></tr><tr><td><strong>Supported Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong> (Packages marked with <img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</td></tr><tr><td>RubyGems</td><td></td><td></td><td><code>Gemfile</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>Gemfile.lock</code></td></tr><tr><td>Bundler</td><td></td><td></td><td></td></tr></tbody></table>

</details>

<details>

<summary>C++</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-d042e5406831f530db216a732c7235db.png" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> C, C++</p><p><strong>Repository:</strong> Conan</p><p><strong>File Types:</strong> .cpp, .c, .h, .hpp, .a, .o, .so</p><p><strong>Exploitable Path:</strong> Not supported</p><p><strong>Tip</strong></p><p>C++ is supported only for File Analysis (fingerprints), not for package resolution.</p></td></tr><tr><td><strong>Supported Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong></td></tr><tr><td>none</td><td></td><td></td><td>none</td></tr></tbody></table>

</details>

<details>

<summary>Unity</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-8b3dcc8e671fe99e2fe76c9a40c74069.png" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> Unity</p><p><strong>Repository:</strong><a href="https://github.com/orgs/Unity-Technologies/repositories">Unity Technologies</a>, <a href="https://github.com/orgs/needle-mirror/repositories">Needle-mirror</a>, <a href="https://openupm.com/packages/">Open UPM</a></p><p><strong>File Types:</strong> none</p><p><strong>Exploitable Path:</strong> Not supported</p></td></tr><tr><td><strong>Supported Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong> (Packages marked with <img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</td></tr><tr><td>none</td><td></td><td></td><td><code>manifest.json</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>packages.json</code><img src="../.gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"></td></tr></tbody></table>

</details>

<details>

<summary>Perl</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-c7e62a516b610ec9e5172b76cd1e53b3.png" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> Perl</p><p><strong>Repository:</strong> <a href="https://www.cpan.org/">Cpan</a></p><p><strong>File Types:</strong> .pl, .pm</p><p><strong>Exploitable Path:</strong> Not supported</p></td></tr><tr><td><strong>Supported Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong></td></tr><tr><td>Cpan</td><td></td><td></td><td><code>cpanfile</code>, <code>spcanfile.snapshot</code></td></tr></tbody></table>

</details>

<details>

<summary>Dart</summary>

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="../.gitbook/assets/img-7b8261dae4e6c7d876b28a7c1bf2f147.jpg" alt="" data-size="original"></td><td colspan="3"><p><strong>Languages/Frameworks:</strong> Dart, Flutter</p><p><strong>Repository:</strong> N/A</p><p><strong>File Types:</strong> none</p><p><strong>Exploitable Path:</strong> Not supported</p></td></tr><tr><td><strong>Supported Package Manager</strong></td><td><strong>Vulnerability Support</strong></td><td><strong>Malicious Package Support</strong></td><td><strong>Manifest Files</strong></td></tr><tr><td>Pub</td><td><sup>1]</sup></td><td></td><td><code>pubspec.lock</code></td></tr></tbody></table>

1] Support of Pub is only for identifying malicious packages. Non-malicious packages are not shown at all in the Packages or Risks tabs.

</details>

## Container Scans

Checkmarx SCA is capable of scanning Dockerfiles and container images as long as they are hosted in supported registries and they are used in supported ecosystems.

For more info about container scans, see [Container Scans](container-scans.md).

{% include "../.gitbook/includes/section-b5fbf2f1.md" %}

{% include "../.gitbook/includes/section-98b0a784.md" %}
