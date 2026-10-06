# Understanding How Checkmarx SCA Scans Run Using Various Methods

## Main Checkmarx SCA Processes

The following are the main processes that take place when you run a Checkmarx SCA scan. Some processes are always run in the cloud, while others can be run either on-prem or in the Checkmarx SCA Cloud, depending on which method you use to initiate the scan.

1. File Analysis – Checkmarx SCA identifies all files in your project that may be part of a 3<sup>rd</sup> party package, and analyzes them in order to determine which packages are being used. This is done by comparing the hashes and metadata of the relevant files (e.g., .jar files for Java, .js files for JS) in the scanned project with the hashes and metadata of packages that are cataloged in our database.

   {% hint style="info" icon="pencil" %}
   For non-scripting files (e.g., .dll, .jar .zip .egg) there is a one to one relationship between files and packages. For scripting files (e.g., .js, .php, .c .cpp) we identify the package that best matches the group of related files in your project.
   {% endhint %}

   As part of this process, compressed files of supported types (.jar, .war, .ear, .zip) are extracted so that the files can be analyzed. This is applied recursively up to four levels of depth.

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

   {% hint style="info" icon="pencil" %}
   Why Lock Files Matter for Accurate Detection

   Manifest files (e.g., `package.json`) declare intended dependencies but do not record the exact versions that were resolved and installed. If a malicious or vulnerable package version was installed at build time but was later removed from the package registry, a scan based solely on the manifest may not detect it.

   Lock files (e.g., `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`) capture the exact resolved versions of all dependencies at the time of installation. Scanning with a lock file ensures that the actual installed state of your dependencies is assessed — including transitive dependencies — making it the recommended approach for accurate risk detection.

   If a lock file is not available (e.g., the scan is performed before the project is built), the scan will fall back to manifest-based resolution, which may result in incomplete visibility.
   {% endhint %}

3. Evidence Analysis - Checkmarx SCA takes the output of the previous steps and uses it to identify the specific risks that affect the packages in your project. This is done by checking the packages that were identified against our extensive database of vulnerabilities as well as checking for legal and suspected malware risks.

## Methods for Running Scans

- Web Portal - When scans are initiated by the Checkmarx SCA web portal, the source code and manifest files are sent to the cloud and all of the processing is done in the cloud. In this case, Checkmarx SCA’s preconfigured package managers are used for resolving the manifest files. This is the simplest method, as it doesn’t require any prior configuration or setup. However, it limits the customer’s ability to customize how the resolving is done and doesn’t enable access to private repositories. It also requires sending the actual source code to the Checkmarx SCA Cloud.

- Checkmarx SCA Resolver - When scans are initiated using Checkmarx SCA Resolver, the File Analysis and Dependency Resolution are both done on-prem and only the output of the analysis, the “evidence files”, are sent to the cloud for the final process of Evidence Analysis. This method enables maximum flexibility for customizing how the package managers run and it enables access to your private repositories. However, it requires that you have all of the relevant package managers configured on your local environment (see [Installing Supported Package Managers for Resolver](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-download-and-installation/installing-supported-package-managers-for-resolver)).

  {% hint style="info" icon="pencil" %}
  The default behavior for Checkmarx SCA Resolver is that the manifest files are sent to the cloud together with the evidence files. This enables Checkmarx SCA to recommend remediation actions relating to the manifest files. There is an option to use the `--no-upload-manifest` flag to block uploading of manifest files. This doesn’t interfere with the effectiveness of the scan, but it may limit Checkmarx SCA’s ability to suggest precise mitigation actions.
  {% endhint %}

- Plugins - When scans are initiated using Checkmarx plugins (CLI, Jenkins, etc.), the default behavior is that the File Analysis is done on-prem and then the “evidence files” as well as the manifest files are sent to the Checkmarx SCA Cloud where the Dependency Resolution and Evidence Analysis are performed.

  {% hint style="info" icon="pencil" %}
  There is an option to configure the plugins to use the Checkmarx SCA Resolver. This requires installing the Checkmarx SCA Resolver locally. In this case, both File Analysis and Dependency Resolution are done on-prem.

  There is also an option to configure the plugins to run all processes in the cloud. This is done by using the `-includesource` upload flag to send the source code to the cloud.
  {% endhint %}

- Checkmarx One - When an SCA scan is run via Checkmarx One, the default behavior is that all of the processing is done in the cloud (similar to a Checkmarx SCA web portal scan). This is true whether the scan is initiated by the Checkmarx One Web Platform, the Checkmarx One CLI Tool or Checkmarx One plugins. The Checkmarx One CLI Tool and plugins have an option to run scans using the Checkmarx SCA Resolver, in which case the File Analysis and Dependency Resolution are done on-prem.

  {% hint style="info" icon="pencil" %}
  For the most accurate and complete scan results, ensure that lock files are included in the scanned repository or working directory. When a lock file is present, Checkmarx SCA uses it to resolve the exact versions of all dependencies, providing a deterministic view of the dependency tree. Without a lock file, dependency resolution is based on manifest files and may result in incomplete or non-reproducible results depending on repository state and resolution behavior at scan time.
  {% endhint %}

## What is Sent to the SCA Cloud?

For scans that don’t require sending the actual source code, as described above (i.e., using Resolver), the following data is sent to the cloud:

- The project name
- List of all file names and relative paths (except the ones that were excluded from the scan)
- Various checksums of the files (SHA-1, SHA-1 on content without spaces, etc.)
- Manifest files (except for scans run via Resolver with the `--no-upload-manifest` flag)

{% hint style="info" icon="pencil" %}
The complete list of files that are sent to the cloud can be seen in [Files Used for Manifest Resolution](files-used-for-manifest-resolution.md).
{% endhint %}

- Names and exact versions of dependencies extracted from lock files (when available) or manifest files.
- Scan errors and warnings such as “Failed resolving dependencies”. Each warning message may contain a file path as an argument.
- SAST Exploitable Path Query result (for Exploitable Path scans)
