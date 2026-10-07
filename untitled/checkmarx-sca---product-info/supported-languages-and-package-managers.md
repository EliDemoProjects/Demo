# Supported Languages and Package Managers

<details>
<summary>How SCA Works</summary>

Checkmarx SCA uses the following methods to identify the 3rd party packages in your project:

1. File Analysis – Checkmarx SCA identifies all files in your project that may be part of a 3<sup>rd</sup> party package, and analyzes them in order to determine which packages are being used. This is done by comparing the hashes and metadata of the relevant files (e.g., .jar files for Java, .js files for JS) in the scanned project with the hashes and metadata of packages that are catalogued in our database. As part of this process, compressed files of supported types (.jar, .war, .ear, .zip) are extracted so that the files can be analyzed. This is applied recursively up to four levels of depth.

   File Analysis is done for the supported languages/frameworks listed below, using the corresponding file types specified in the table.

2. Dependency Resolution - Checkmarx SCA resolves dependencies using one of two methods:

   - Package Manager Resolution (default)

     - Checkmarx SCA uses package managers to resolve dependencies against customer-defined or public repositories and reconstruct the dependency tree based on manifest files (e.g., `package.json`). These files define the intended dependencies, typically using version ranges.
     - Because this method depends on the state of external repositories at scan time, the resulting dependency tree may differ from what was originally installed. In some cases, this can lead to incomplete or inconsistent dependency reconstruction, especially if package versions have been removed, updated, or resolved differently across environments.

   - Lock File Resolution

     - When a lock file is present (e.g., `package-lock.json`, `yarn.lock`), Checkmarx SCA uses it to determine the exact versions of all resolved dependencies, including transitive dependencies. This provides a deterministic and reproducible view of the dependency tree as it was installed.
     - This method significantly improves accuracy and reduces the risk of missing dependencies or security findings caused by differences in resolution behavior or changes in package availability.

   {% hint style="info" icon="pencil" %}
   To ensure accurate and reproducible results, it is strongly recommended to include lock files in SCA scans. Lock files reflect the exact dependency tree used in the application and improve both vulnerability detection and auditability of scan results.
   {% endhint %}

For more information about how Checkmarx SCA scans run using various methods, refer to [Understanding How Checkmarx SCA Scans Run Using Various Methods](understanding-how-checkmarx-sca-scans-run-using-various-methods.md).

</details>

{% hint style="info" icon="pencil" %}
If you are using Checkmarx SCA Resolver, then you need to install the relevant package managers locally. For installation info, see [Installing Supported Package Managers for Resolver](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-download-and-installation/installing-supported-package-managers-for-resolver).
{% endhint %}

## Supported Languages and Package Managers

[Java](#UUID-9c93d6b8-4b0b-b4de-ee58-9e99b1ec02ba_section-idm4494748069177633396069421573_body)

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-113e175db6fc1cdfe0c2663d7c33ae55.png" alt=""></figure></td><td colspan="4"><p></p><p><strong><strong>JVM Languages:</strong></strong> Java, Kotlin, Android, Groovy, Scala</p><p><strong><strong>Additional Frameworks:</strong></strong> Struts, Spring</p><p><strong><strong>Repository:</strong></strong> Maven Central, Sonatype, Apache</p><p><strong><strong>File Types:</strong></strong> .jar</p><p><strong><strong>Supported Languages for Exploitable Path:</strong></strong> Java</p></td></tr>
<tr><td><p><strong><strong>Package Managers</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td colspan="2"><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong></p></td></tr>
<tr><td><p>Maven</p></td><td><p></p></td><td colspan="2"><p></p></td><td><p><code>pom.xml</code></p></td></tr>
<tr><td><p>Gradle</p></td><td><p></p></td><td colspan="2"><p></p></td><td colspan="2"><p><code>build.gradle</code> , <code>build.gradle.kts</code></p></td></tr>
<tr><td><p>Ivy</p></td><td><p></p></td><td colspan="2"><p></p></td><td><p><code>ivy.xml</code>,</p><p><code>build.xml</code></p></td></tr>
<tr><td><p>SBT</p></td><td><p></p></td><td colspan="2"><p></p></td><td><p><code>build.sbt</code></p></td></tr>
</tbody>
</table>

<details>
<summary>JavaScript/TypeScript</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-0aa99a0522a4571621fa63a1599845db.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> JavaScript, TypeScript, NodeJS, React, Angular, Apex</p><p><strong>Tip</strong></p><p>Apex is only supported when running the scan using Checkmarx SCA Resolver with the <code>--extract-archives resource</code> argument, see <a href="https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-configuration-arguments">Checkmarx SCA Resolver Configuration Arguments</a>.</p><p><strong><strong>Repository:</strong></strong> NPM</p><p><strong><strong>File Types:</strong></strong> .js</p><p><strong><strong>Supported Languages for Exploitable Path:</strong></strong> JavaScript</p></td></tr>
<tr><td><p><strong><strong>Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong> (Packages marked with <img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</p></td></tr>
<tr><td><p>NPM</p></td><td><p></p></td><td><p></p></td><td><p><code>package.json</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> , <code>package-lock.json</code><sup>1]</sup></p></td></tr>
<tr><td><p>Yarn (and Yarn 2)</p></td><td><p></p></td><td><p></p></td><td><p><code>package.json</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> , <code>yarn.lock</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"><sup>1]</sup></p></td></tr>
<tr><td><p>Bower</p></td><td><p></p></td><td><p></p></td><td><p><code>bower.json</code></p></td></tr>
<tr><td><p>Pnpm</p></td><td><p></p></td><td><p></p></td><td><p><code>pnpm-lock.yaml</code></p></td></tr>
</tbody>
</table>

1\] When a `lock` file is present in the project, SCA may use it to resolve dependencies. Therefore, it is important to keep the lock file up-to-date with any changes that you make in the manifest file.

</details>

<details>
<summary>.NET</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-cc258c57dd6a07bba226176fa1579825.jpg" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> C#, F#, .NET, .NET Core, WCF, WPF, ASP.NET</p><p><strong><strong>Repository:</strong></strong> NuGet</p><p><strong><strong>File Types:</strong></strong> .dll</p><p><strong><strong>Supported Languages for Exploitable Path:</strong></strong> C#</p></td></tr>
<tr><td><p><strong><strong>Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong></p></td></tr>
<tr><td><p>NuGet</p></td><td><p></p></td><td><p></p></td><td><p><code>*.csproj</code> , <code>packages.config</code>, <code>project.assets.json</code>, <code>packages.lock.json</code></p></td></tr>
</tbody>
</table>

</details>

<details>
<summary>Python</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-224a5acf482ebf711d9adf7337adf4eb.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> Python, Django, Flask</p><p><strong><strong>Repository:</strong></strong> PyPi</p><p><strong><strong>File Types:</strong></strong> .egg, .whl</p><p><strong><strong>Supported Languages for Exploitable Path:</strong></strong> Python</p></td></tr>
<tr><td><p><strong><strong>Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong> (Packages marked with <img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</p></td></tr>
<tr><td><p>PIP</p></td><td><p></p></td><td><p></p></td><td><p><code>requirements.txt</code>, <code>requirements-*.txt</code>, <code>requirement.txt</code>, <code>requirement-*.txt</code></p></td></tr>
<tr><td><p>Poetry</p></td><td><p></p></td><td><p></p></td><td><p><code>pyproject.toml</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>poetry.lock</code></p></td></tr>
<tr><td><p>Setuptools<sup> 1]</sup></p></td><td><p></p></td><td><p></p></td><td><p><code>Setup.cfg</code>, <code>Setup.py</code></p></td></tr>
<tr><td><p>UV</p></td><td><p></p></td><td><p></p></td><td><p><code>uv.lock</code>, <code>requirements.txt</code>, <code>pyproject.toml</code></p></td></tr>
</tbody>
</table>

1\] Setuptools is supported only when running scans using SCA Resolver.

</details>

<details>
<summary>PHP</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-a8bf03c955b6b95eb2418f9e405eba2e.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> PHP, Drupal</p><p><strong><strong>Repository:</strong></strong> Packagist</p><p><strong><strong>File Types:</strong></strong> none</p><p><strong><strong>Exploitable Path:</strong></strong> Not supported</p></td></tr>
<tr><td><p><strong><strong>Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong> (Packages marked with <img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</p></td></tr>
<tr><td><p>Composer</p></td><td><p></p></td><td><p></p></td><td><p><code>composer.json</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> , <code>composer.lock</code></p></td></tr>
</tbody>
</table>

</details>

<details>
<summary>iOS</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-d6cd5ddc4653ff1eb4362f8567516f0c.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> Swift, Objective c</p><p><strong><strong>Repository:</strong></strong> GitHub</p><p><strong><strong>File Types:</strong></strong> none</p><p><strong><strong>Exploitable Path:</strong></strong> Not supported</p></td></tr>
<tr><td><p><strong><strong>Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong> (Packages marked with <img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</p></td></tr>
<tr><td><p>SwiftPm</p></td><td><p></p></td><td><p></p></td><td><p><code>Package.swift</code>, <code>Package.resolved</code></p></td></tr>
<tr><td><p>CocoaPods</p></td><td><p></p></td><td><p></p></td><td><p><code>Podfile</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>Podfile.lock</code></p></td></tr>
<tr><td><p>Carthage</p></td><td><p></p></td><td><p></p></td><td><p><code>Cartfile</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>Cartfile.private</code>, <code>Cartfile.resolved</code></p><p><strong>Tip</strong></p><p>At least one <code>.private</code> or <code>.resolved</code> file must be included.</p></td></tr>
</tbody>
</table>

</details>

<details>
<summary>Go</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-ca7790723e5bac8285198d139444c923.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> Go</p><p><strong><strong>Repository:</strong></strong> Golang</p><p><strong><strong>File Types:</strong></strong> none</p><p><strong><strong>Exploitable Path:</strong></strong> Not supported</p></td></tr>
<tr><td><p><strong><strong>Supported Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong> (Packages marked with <img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</p></td></tr>
<tr><td><p>GoModules</p></td><td><p></p></td><td><p></p></td><td><p><code>go.mod</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>go.sum</code></p></td></tr>
</tbody>
</table>

</details>

<details>
<summary>Ruby</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-6d2e8a2b8e361dd5f394edd3b435a601.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> Ruby</p><p><strong><strong>Repository:</strong></strong> RubyGems</p><p><strong><strong>File Types:</strong></strong> none</p><p><strong><strong>Exploitable Path:</strong></strong> Not supported</p></td></tr>
<tr><td><p><strong><strong>Supported Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong> (Packages marked with <img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</p></td></tr>
<tr><td><p>RubyGems</p></td><td><p></p></td><td><p></p></td><td><p><code>Gemfile</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>Gemfile.lock</code></p></td></tr>
<tr><td><p>Bundler</p></td><td><p></p></td><td><p></p></td><td><p></p></td></tr>
</tbody>
</table>

</details>

<details>
<summary>C++</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-d042e5406831f530db216a732c7235db.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> C, C++</p><p><strong><strong>Repository:</strong></strong> Conan</p><p><strong><strong>File Types:</strong></strong> .cpp, .c, .h, .hpp, .a, .o, .so</p><p><strong><strong>Exploitable Path:</strong></strong> Not supported</p><p><strong>Tip</strong></p><p>C++ is supported only for File Analysis (fingerprints), not for package resolution.</p></td></tr>
<tr><td><p><strong><strong>Supported Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong></p></td></tr>
<tr><td><p>none</p></td><td><p></p></td><td><p></p></td><td><p>none</p></td></tr>
</tbody>
</table>

</details>

<details>
<summary>Unity</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-8b3dcc8e671fe99e2fe76c9a40c74069.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> Unity</p><p><strong><strong>Repository:</strong></strong><a href="https://github.com/orgs/Unity-Technologies/repositories">Unity Technologies</a>, <a href="https://github.com/orgs/needle-mirror/repositories">Needle-mirror</a>, <a href="https://openupm.com/packages/">Open UPM</a></p><p><strong><strong>File Types:</strong></strong> none</p><p><strong><strong>Exploitable Path:</strong></strong> Not supported</p></td></tr>
<tr><td><p><strong><strong>Supported Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong> (Packages marked with <img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"> are required)</p></td></tr>
<tr><td><p>none</p></td><td><p></p></td><td><p></p></td><td><p><code>manifest.json</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line">, <code>packages.json</code><img src=".gitbook/assets/img-dffd1b8669870a53cfed6fe20ff40109.png" alt="" data-size="line"></p></td></tr>
</tbody>
</table>

</details>

<details>
<summary>Perl</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-c7e62a516b610ec9e5172b76cd1e53b3.png" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> Perl</p><p><strong><strong>Repository:</strong></strong> <a href="https://www.cpan.org/"> Cpan</a></p><p><strong><strong>File Types:</strong></strong> .pl, .pm</p><p><strong><strong>Exploitable Path:</strong></strong> Not supported</p></td></tr>
<tr><td><p><strong><strong>Supported Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong></p></td></tr>
<tr><td><p>Cpan</p></td><td><p></p></td><td><p></p></td><td><p><code>cpanfile</code>, <code>spcanfile.snapshot</code></p></td></tr>
</tbody>
</table>

</details>

<details>
<summary>Dart</summary>

<table>
<tbody>
<tr><td><figure><img src=".gitbook/assets/img-7b8261dae4e6c7d876b28a7c1bf2f147.jpg" alt=""></figure></td><td colspan="3"><p><strong><strong>Languages/Frameworks:</strong></strong> Dart, Flutter</p><p><strong><strong>Repository:</strong></strong> N/A</p><p><strong><strong>File Types:</strong></strong> none</p><p><strong><strong>Exploitable Path:</strong></strong> Not supported</p></td></tr>
<tr><td><p><strong><strong>Supported Package Manager</strong></strong></p></td><td><p><strong><strong>Vulnerability Support</strong></strong></p></td><td><p><strong><strong>Malicious Package Support</strong></strong></p></td><td><p><strong><strong>Manifest Files</strong></strong></p></td></tr>
<tr><td><p>Pub</p></td><td><p> <sup>1]</sup></p></td><td><p></p></td><td><p><code>pubspec.lock</code></p></td></tr>
</tbody>
</table>

1\] Support of Pub is only for identifying malicious packages. Non-malicious packages are not shown at all in the Packages or Risks tabs.

</details>

## Container Scans

Checkmarx SCA is capable of scanning Dockerfiles and container images as long as they are hosted in supported registries and they are used in supported ecosystems.

For more info about container scans, see [Container Scans](container-scans.md).

{% include ".gitbook/includes/section-b5fbf2f1.md" %}

{% include ".gitbook/includes/section-98b0a784.md" %}
