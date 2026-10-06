# Running Scans Using Checkmarx SCA Resolver

## Prerequisites

* Download and install the latest version of Checkmarx SCA Resolver for your OS, see [Checkmarx SCA Resolver Download](checkmarx-sca-resolver-download-and-installation.md).
* Checkmarx SCA Resolver requires dependency resolution utilities to be installed, and the project to be in a buildable state. For a list of requirements, see [Package Managers Support in SCA Resolver.](installing-supported-package-managers-for-resolver.md)
* You need to have the following info about your Checkmarx SCA account: **account name**, **username** and **password**.

{% hint style="info" icon="pencil" %}
If you authenticate via a SAML provider, then providing user credentials is not necessary. See [SAML Authentication for Checkmarx SCA Resolver](saml-authentication-for-checkmarx-sca-resolver.md).
{% endhint %}

## Running Scans Using the Checkmarx SCA Resolver

You can use the Resolver to scan an **existing** Project or to create a **new** Project. If you are scanning an existing Project, then the Project settings that you configured in the SCA web portal (e.g., teams assignment, notifications, Python version) are automatically applied to the scan. If you are creating a new Project in Resolver, then you can use the optional configuration arguments to configure these settings, see [Checkmarx SCA Resolver Configuration Arguments](checkmarx-sca-resolver-configuration-arguments.md).

{% hint style="info" icon="pencil" %}
If you would like to use the **Policy** feature to cause builds to break whenever the specified threshold of security threats is detected, you need to first create the Project in the web portal and assign it to a Policy (see [Policy Management](https://app.gitbook.com/s/XSPACE_USER_GUIDE/policy-management)). Then, you can run the Project using Resolver.
{% endhint %}

{% hint style="info" icon="pencil" %}
If you would like to run scans using the **Exploitable Path** feature, use the procedure described in [Running Exploitable Path Scans Using Resolver](running-exploitable-path-scans-using-resolver.md).
{% endhint %}

### Checkmarx SCA Resolver Modes

Checkmarx SCA Resolver (version 1.5.4+) can be run either in Online mode or in Offline mode. When online mode is used (default), the resolved results are automatically sent to Checkmarx SCA Cloud for scanning. When offline mode is used, the resolved results are saved locally. You can then use Upload mode at a later time to send the results to Checkmarx SCA Cloud for scanning.

{% hint style="info" icon="pencil" %}
In order to run Checkmarx SCA Resolver in Online or Upload mode you need to provide authentication credentials. The procedures below describe the standard authentication method, which uses the username and password for authentication. Alternatively, if you have integrated your Checkmarx SCA account with a SAML provider, you can authenticate for Checkmarx SCA Resolver via your SAML provider, see [SAML Authentication for Checkmarx SCA Resolver](saml-authentication-for-checkmarx-sca-resolver.md).
{% endhint %}

### Running a Scan - Online Mode

To run a new scan using the Checkmarx SCA Resolver in Online mode:

1.  If you would like to view the list of available arguments, in the CLI, run `ScaResolver.exe` (Windows) or `ScaResolver` (Linux) with the `-h` flag, as shown:

    ```
    ./ScaResolver -h
    ```

    The available arguments are displayed.
2.  To start a scan, run `ScaResolver.exe` (Windows) or `ScaResolver` (Linux) with the following mandatory arguments:

    -s : path to the folder to scan

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>This must be the path to a local folder that contains the source code, not to a zip archive or a code repository.</p></div>

    -n : to scan an existing Project, enter the name of the Project. OR,

    to create a new Project, enter a new name to assign to the Project

    -a : your Checkmarx SCA account name

    -u : your username

    -p : your password

    The following example shows a run command using the mandatory arguments:

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>You can add additional arguments to specify the desired scan configuration, see <a href="checkmarx-sca-resolver-configuration-arguments.md">Checkmarx SCA Resolver Configuration Arguments</a>. For example, the <code>-e</code> argument enables you to exclude specific folder and file patterns, see examples in the “Optional Arguments” section of <a href="checkmarx-sca-resolver-configuration-arguments.md">Checkmarx SCA Resolver Configuration Arguments</a>.</p></div>

    After a successful completion, a risk report summary is displayed in the CLI.

    The following example shows a risk report summary:

    ```
    ################### Risk report summary ###################
    Direct dependencies :                   10 (28 total)

    High severity vulnerabilities:          11
    Medium severity vulnerabilities:        1
    Low severity vulnerabilities:           0
    ###########################################################
    ```

3\. If you used the `--report-type` flag in the run command, then you can open the Risk Report file to view the results. Otherwise, you can view the results in the Checkmarx SCA web portal by searching for the Project by the name designated in the -n argument.

### Running a Scan - Offline Mode

To run a new scan using the Checkmarx SCA Resolver in Offline mode:

1.  If you would like to view the list of available arguments, in the CLI, run `ScaResolver.exe` (Windows) or `ScaResolver` (Linux) with the `-h` flag, as shown:

    ```
    ./ScaResolver -h
    ```

    The available arguments are displayed.
2.  To start a scan, run `ScaResolver.exe offline` (Windows) or `ScaResolver offline` (Linux) with the following mandatory arguments:

    -s : path to the folder to scan

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>This must be the path to a local folder that contains the source code, not to a zip archive or a code repository.</p></div>

    -n : to scan an existing Project, enter the name of the Project. OR,

    to create a new Project, enter a new name to assign to the Project

    -r : path to directory/file where results will be stored for future upload

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>When running a container scan in Offline mode, it is also mandatory to use <code>--containers-result-path</code> to specify the container results output location.</p></div>

    The following example shows an Offline run command using the mandatory arguments:

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>You can add additional arguments to specify the desired scan configuration, see <a href="checkmarx-sca-resolver-configuration-arguments.md">SCA Resolver Configuration Arguments</a>. For example, the <code>-e</code> argument enables you to exclude specific folder and file patterns, see examples in the “Optional Arguments” section of <a href="checkmarx-sca-resolver-configuration-arguments.md">SCA Resolver Configuration Arguments</a>.</p></div>
3.  When you are ready to run the scan, run `ScaResolver.exe upload` (Windows) or `ScaResolver upload` (Linux) with the following mandatory arguments:

    -n : enter the name of the Project (same as used for Offline mode)

    -a : your Checkmarx SCA account name

    -u : your username

    -p : your password

    -r : path to the file where results from the Offline mode were stored

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>When running a container scan in Offline mode, it is also mandatory to use <code>--containers-result-path</code> to refer to the location where the container results were stored.</p></div>

    The following example shows an Upload run command using the mandatory arguments:

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>You can add additional arguments to specify the desired scan configuration, see <a href="checkmarx-sca-resolver-configuration-arguments.md">Checkmarx SCA Resolver Configuration Arguments</a>.</p></div>

    After a successful completion, a risk report summary is displayed in the CLI.

    The following example shows a risk report summary:

    ```
    ################### Risk report summary ###################
    Direct dependencies :                   10 (28 total)

    High severity vulnerabilities:          11
    Medium severity vulnerabilities:        1
    Low severity vulnerabilities:           0
    ###########################################################
    ```
4. If you used the `--report-type` flag in the Upload run command, then you can open the Risk Report file to view the results. Otherwise, you can view the results in the Checkmarx SCA web portal by searching for the Project by the name designated in the -n argument.

### Reports

Checkmarx SCA generates two types of reports:

* Risk Report - a comprehensive report which shows aggregated statistics for your Project as well as detailed info about the risks that were identified by the scan.
*   Software Bill of Materials (SBOM) - a report that gives a complete list of all components used by the program, including direct and transitive dependencies. The report follows the [CycloneDX v1.3](https://cyclonedx.org/docs/1.3/#SchemaProperties) format, which includes info for each component such as name, supplier name, version, hashes and other unique identifiers etc. Checkmarx SCA supplements this data with additional “property” fields that contain info about the risks associated with each package.

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>There is an alternative method for generating SBOM reports using the <a href="https://app.gitbook.com/s/XSPACE_REST_API/checkmarx-sca--rest--api---export-service">Export Service API</a>. The Export Service API generates SBOMs that are more compliant with SBOM formatting specifications. Export Service also supports generating SBOMs in SPDX format.</p></div>

You can generate a Risk Report in json, xml, csv or pdf format when running a scan using Checkmarx SCA Resolver (version 1.5.4+).

Risk Report Example:

{% tabs %}
{% tab title="Linux/MacOS" %}
```
./ScaResolver -s /Users/DemoUser/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --report-extension Pdf,Json,Csv --report-type Risk
```
{% endtab %}

{% tab title="Windows" %}
```
./ScaResolver.exe -s C:\Users\DemoUser\MyApp -n MyApp -a Checkmarx -u jack -p "demo123!" --report-extension Pdf,Json,Csv --report-type Risk
```
{% endtab %}
{% endtabs %}

You can generate an SBOM Report in json or xml format when running a scan using Checkmarx SCA Resolver (version 1.5.52+).

SBOM Report Example:

{% tabs %}
{% tab title="Linux/MacOS" %}
```
./ScaResolver -s /Users/DemoUser/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --report-extension Xml,Json --report-type CycloneDx
```
{% endtab %}

{% tab title="Windows" %}
```
./ScaResolver.exe -s C:\Users\DemoUser\MyApp -n MyApp -a Checkmarx -u jack -p "demo123!" --report-extension Xml,Json --report-type CycloneDx
```
{% endtab %}
{% endtabs %}

For more info about the arguments used for exporting reports, see the “Report Arguments” section of [Checkmarx SCA Resolver Configuration Arguments](checkmarx-sca-resolver-configuration-arguments.md).

{% hint style="info" icon="pencil" %}
In addition, you can download Risk Reports and SBOM Reports for any scans that have been run in your account via the web portal, see [Scan Reports](https://app.gitbook.com/s/XSPACE_USER_GUIDE/generating-sca-reports/sca-scan-reports). You can also view detailed scan results in the web browser, see [Viewing Results](https://checkmarx.atlassian.net/wiki/spaces/GO/pages/2030993550/Viewing+Results).
{% endhint %}

### Container Scans

{% include "../.gitbook/includes/warning-9851dc6f (1).md" %}

In addition to scanning the packages in your source code itself, Checkmarx SCA also scans the Dockerfiles in your project to identify the container images used in your project. Checkmarx SCA extracts all layers of each public base image located in the Dockerfile, and identifies the packages used by each layer.

For scans run via SCA Resolver, in addition to scanning the Dockerfile itself, you can also scan the image that is created from the Dockerfile, using the Syft open source tool. This enables greater visibility into all packages used in the image for all languages supported by SCA as well as many non-supported languages (e.g., Dart, Haskell, Swift etc.). In addition, you can use SCA Resolver to submit specific images from public or private registries for analysis by SCA using the Syft tool.

For more info about container scans, see [Container Scans](https://app.gitbook.com/s/XSPACE_PRODUCT_INFO/container-scans).

{% include "../.gitbook/includes/section-a7f59a84 (1).md" %}

{% include "../.gitbook/includes/section-fb691940 (1).md" %}

{% include "../.gitbook/includes/section-04b09d94 (1).md" %}

For more info about container scans, see [Container Scans](https://app.gitbook.com/s/XSPACE_PRODUCT_INFO/container-scans).

### Proxy Scans

You can use a proxy server to make internet requests for SCA Resolver. You can configure proxies for HTTP and HTTPS and you can pass the authentication credentials.

#### Running Scans via Proxy

1. To scan a project using a proxy server, add the `--proxies` flag to the scan command followed by comma separated host urls.
2. If you you need to pass credentials, add them using the following syntax @\<username>:\<password>.

Proxy Scan Example:

The following example shows a command to run a scan using proxy HTTP and HTTPS servers. This command also passes the the authentication credentials for the HTTP server.

{% tabs %}
{% tab title="Linux/MacOS" %}
```
./ScaResolver -s /Users/DemoUser/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --proxies “http:somehost:8081@myusername:ABC1234, https:anotherhost:8082”
```
{% endtab %}

{% tab title="Windows" %}
```
./ScaResolver.exe -s C:\Users\DemoUser\MyApp -n MyApp -a Checkmarx -u jack -p "demo123!" --proxies “http:somehost:8081@myusername:ABC1234, https:anotherhost:8082”--proxies “http:somehost:8081”
```
{% endtab %}
{% endtabs %}

## Exit Codes

The table below shows the possible exit codes that are received from Checkmarx SCA Resolver and explains their meaning.

| Code | Name                                   | Description                                                                                                                                                                                                                                   |
| ---- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0    | Success                                | The request ran successfully.                                                                                                                                                                                                                 |
| 3    | AuthenticationFailure                  | Request failed because unable to authenticate the user account.                                                                                                                                                                               |
| 4    | InternalError                          | Request failed because of an internal error in the system.                                                                                                                                                                                    |
| 5    | ParsingError                           | Request failed because of an invalid command (e.g., invalid flags or configurations).                                                                                                                                                         |
| 6    | ExceededVulnerabilitySeverityThreshold | The results indicate that vulnerabilities were identified that exceed the threshold set for the scan (using the `--severity_threshold` flag in the run command). See [Optional Arguments](checkmarx-sca-resolver-configuration-arguments.md). |
| 7    | InsufficientPermissions                | Request failed because the user credentials submitted don’t have the required permissions for this action.                                                                                                                                    |
| 8    | BreakBuild                             | The scan results indicate that the build should be broken, based on a risk Policy configured for this Project. See [Policy Management](https://app.gitbook.com/s/XSPACE_USER_GUIDE/policy-management).                                        |
| 9    | PackageManagerError                    | <p>The scan failed because resolution failed for one or more of the manifest files.<br><strong>Tip</strong> This code is only returned if the scan was run with the flag <code>--break-on-manifest-failure</code>.</p>                        |
| 10   | ConfigurationNotSupported              | The scan failed because of an unsupported configuration.                                                                                                                                                                                      |

## Logging

Logs are printed to the standard output as well as to the “logs” directory, located where you run the Resolver.

Each run creates a log file with an appropriate timestamp.

The location of the log directory is determined by the LogsDirectory parameter in the config file.

By default, log verbosity is information level and higher. Use --log\_level Debug to receive more output, or --log\_level Error to receive only errors.

For more information, see SCA Resolver Configuration Arguments.

## Troubleshooting

Some issues have occurred when attempting to run the Resolver on clean Ubuntu and Debian systems. This is mainly because the .NET CORE packed executable relies on some basic packages. If the executable fails to run, see [SCA Resolver Download.](checkmarx-sca-resolver-download-and-installation.md)

### Contacting Support

With every support request, please verify the version of the Resolver used by running `ScaResolver.exe` (Windows) or `ScaResolver` (Linux) with the `--version` flag, as shown:

```
./ScaResolver --version
```

{% hint style="info" icon="pencil" %}
This command works only from version 1.2.3. If the command is not available, please let technical support know.
{% endhint %}

Every scan has a scan ID. When a scan is completed, the following line is displayed:

```
Information    Program "Scan Id: ce0ce194-39a0-4a00-9e09-7bad8c225dd2"
```

Please provide this Scan ID with all support calls and requests.

### Troubleshooting Dependency Resolution

Checkmarx SCA Resolver requires dependency resolution utilities to be installed, and the project to be in a buildable state. Some errors may occur during dependency resolution.

For a list of requirements, see [Package Managers Support in SCA Resolver.](installing-supported-package-managers-for-resolver.md)

If the Resolver run fails, the output displays error messages, as shown in the following NPM failure:

```
2020-06-17T20:09:22+03:00 Error  NpmDependencyResolver "Failed to create package lock file" {ResolvingModuleType=Npm, Command="i --package-lock-only", ProcessErrorResponse="npm ERR! code ETARGET
npm ERR! notarget No matching version found for unknown@1.2.3
npm ERR! notarget In most cases you or one of your dependencies are requesting
npm ERR! notarget a package version that doesn't exist.
npm ERR! notarget 
npm ERR! notarget It was specified as a dependency of 'artifactory'
npm ERR! notarget 

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\\Users\\test\\AppData\\Roaming\\npm-cache\\_logs\\2020-06-17T17_09_22_150Z-debug.log", ProcessInfoLog=""} { ResolvingModuleType: Npm, Command: "i --package-lock-only", ProcessErrorResponse: "npm ERR! code ETARGET
npm ERR! notarget No matching version found for unknown@1.2.3
npm ERR! notarget In most cases you or one of your dependencies are requesting
npm ERR! notarget a package version that doesn't exist.
npm ERR! notarget
npm ERR! notarget It was specified as a dependency of 'artifactory'
npm ERR! notarget

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\test\AppData\Roaming\npm-cache\_logs\2020-06-17T17_09_22_150Z-debug.log", ProcessInfoLog: "" } 
```
