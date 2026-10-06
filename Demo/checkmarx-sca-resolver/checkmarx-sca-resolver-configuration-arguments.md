# Checkmarx SCA Resolver Configuration Arguments

Most Checkmarx SCA Resolver configuration parameters can be submitted either as command line arguments or by editing the **configuration.yml** file.

{% hint style="info" icon="pencil" %}
Certain parameters must be submitted via the config file. Therefore, it is mandatory to include the configuration.yml file (which is included in the Checkmarx SCA Resolver download) in the same folder as the ScaResolver binary.
{% endhint %}

{% hint style="info" %}
The info provided on this page relates to running Resolver as a standalone tool. If you are running Resolver via an external platform such as the Checkmarx One CLI tool or plugins, or the CxSAST/CxSCA CLI tool or plugins, then only Offline arguments can be used. In addition, the mandatory arguments differ for different platforms. See the relevant [SAST/SCA Integrations](/document/preview/7297#UUID-09af4cb8-95d4-d86a-48f3-5e0e5176366b) documentation for details.
{% endhint %}

## Configuration.yml file Specifications

{% hint style="warning" %}
As of version 2.0, `Configuration.ini` format is no longer supported. It is now mandatory to include the `Configuration.yml` file containing your config data.
{% endhint %}

The configuration file must be located in the same folder as the ScaResolver binary.

The configuration file has the format of KeyName: Value.

The file must follow the [yaml file format specification](https://yaml.org/spec/1.2.2/).

### Connecting to your SCA Environment

The config file includes parameters for configuring the connectivity to your SCA environment. By default these values are set for the US environment. If you are using the EU environment, you will need to adjust these values accordingly.

{% tabs %}
{% tab title="US Environment" %}
- ServerUrl - [https://api-sca.checkmarx.net](https://api-sca.checkmarx.net)
- AuthenticationServerUrl - [https://platform.checkmarx.net](https://platform.checkmarx.net)
- ScaAppUrl - [https://sca.checkmarx.net](https://sca.checkmarx.net)
{% endtab %}
{% tab title="EU Environment" %}
- ServerUrl - [https://eu.api-sca.checkmarx.net](https://eu.api-sca.checkmarx.net)
- AuthenticationServerUrl - [https://eu.platform.checkmarx.net](https://eu.platform.checkmarx.net.)
- ScaAppUrl - [https://eu.sca.checkmarx.net](https://eu.sca.checkmarx.net)
{% endtab %}
{% endtabs %}

## Configuration Arguments - Tables and Samples

The following tables describe the supported arguments that can be used in Resolver. You can submit `--help` to get the list of supported parameters.

{% tabs %}
{% tab title="Mandatory Arguments" %}
| Argument | Name | Config file key | Description | Used in mode | Default value |
| --- | --- | --- | --- | --- | --- |
| -a\| --account | Account | Account | Your SCA account a name. | Online, Upload | - |
| --authentication-server-url | Authentication Server URL<sup>1</sup> | AuthenticationServerUrl | The URL of the SCA Access Control server. | Online, Upload | [https://platform.checkmarx.net](https://platform.checkmarx.net) |
| --logs-path | Logs Directory<sup>2\]</sup> | LogsDirectory | The default name assigned the logs directory. |  | logs |
| -p\| --password | Password<sup>3\]</sup> | Password | The password for your SCA user account.<br>**Tip** You can configure a custom Environment Variable to use for the password. This is preferable to including a password in clear text in the config file. | Online, Upload | - |
| --containers-result-path | Path to read container results | ContainersResultPath | Specify the path to the file of the saved containers results that you are uploading.<br>**Tip** Mandatory for container scans. | Upload | - |
| -r\|--resolver-result-path | Path to read ScaResolver results | ResolverResultPath | Specify the path to the file of the saved resolver results that you are uploading. | Upload | - |
| --containers-result-path | Path to save container results | ContainersResultPath | Specify the path to the directory/file where the containers results will be saved (for future upload).<br>**Tip** Mandatory for container scans, `--scan-containers`. | Offline | - |
| -r\|--resolver-result-path | Path to save ScaResolver results | ResolverResultPath | Specify the path to the directory/file where the resolver results will be saved (for future upload). | Offline | - |
| -n\| --project-name | Project Name | ProjectName | To scan an existing SCA Project, enter the Project name. Alternatively, you can enter a new Project name in order to create a new Project in SCA. | All | - |
| --sso-provider | Provider name<sup>3\]</sup> | SsoProviderName | The name of your SSO provider. Alternatively, you can give the name of your Master Access Control instance. For more info see [SAML Authentication for Checkmarx SCA Resolver](saml-authentication-for-checkmarx-sca-resolver.md) | Online, Upload | - |
| --sca-app-url | SCA Application URL<sup>3\]</sup> | ScaAppUrl | The URL of the SCA web application. | Online, Upload | [https://sca.checkmarx.net](https://sca.checkmarx.net) |
| -s\| --scan-path | Scan Path | N/A | Path to the folder to be scanned.<br>**Note** This must be the path to a local folder that contains the source code, not to a zip archive or a code repository. | Online, Offline | - |
| --server-url | Server URL<sup>1\]</sup> | ServerUrl | The URL of the SCA API server. | Online, Upload | [https://api-sca.checkmarx.net](https://api-sca.checkmarx.net) |
| -u\| --username | Username<sup>3\]</sup> | Username | Your username for the SCA account. | Online, Upload | - |

1\] The default values for Server URL and Authentication Server URL are preconfigured in the config file, making it unnecessary to submit these arguments in the CLI.

2\] The default value for Logs Directory is preconfigured in the config file. There is no argument for adjusting this value in the CLI.

3\] Authentication is done either using your Checkmarx SCA credentials, or via your SSO provider. Therefore, you are required to submit either `-u| --username` and `-p| --password` or `--sso-provider` but not both.

Samples using mandatory arguments:

Linux/MacOS

```
./ScaResolver -s /home/jack/src/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!'
```

Windows

```
./ScaResolver.exe -s C:\home\jack\src\MyApp -n MyApp -a Checkmarx -u jack -p "demo123!"
```
{% endtab %}
{% tab title="Optional Arguments" %}
<table>
<thead>
<tr><th><p><strong><strong>Argument</strong></strong></p></th><th><p><strong><strong>Name</strong></strong></p></th><th><p><strong><strong>Config file key</strong></strong></p></th><th><p><strong><strong>Description</strong></strong></p></th><th><p><strong><strong>Used in mode</strong></strong></p></th><th><p><strong><strong>Default value</strong></strong></p></th></tr>
</thead>
<tbody>
<tr><td><p>N/A</p></td><td><p>Additional Manifest Patterns</p></td><td><p>AdditionalManifestPatterns</p></td><td><p>Allows the user to specify additional patterns to detect as manifest.</p><p><strong>Tip</strong></p><p>Currently supported only for pip.</p><p>Syntax:</p><pre><code>AdditionalManifestPatterns:  
  pip: 
    - example-*.txt</code></pre></td><td><p>Online, Offline</p></td><td><p>N/A</p></td></tr>
<tr><td><p>--project-tags</p></td><td><p>Add tags to project</p></td><td><p>N/A</p></td><td><p>Comma-separated tags to be assigned to the project. Tags can be a simple string or a key:value.</p></td><td><p>Online, Upload</p></td><td><p>None</p></td></tr>
<tr><td><p>--scan-tags</p></td><td><p>Add tags to scan</p></td><td><p>N/A</p></td><td><p>Comma-separated tags to be assigned per scan. Tags can be a simple string or a key:value.</p></td><td><p>Online, Upload</p></td><td><p>None</p></td></tr>
<tr><td><p>--break-on-manifest-failure</p></td><td><p>Break on manifest failure</p></td><td><p>BreakOnManifestFailure</p></td><td><p>When this flag is used, the scan will fail and error code 9 will be returned when resolution fails for one or more of the manifest files.</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--bypass-exitcode</p></td><td><p>Bypass exit code</p></td><td><p>BypassExitCode</p></td><td><p>If set as “true”, exit code will be overridden and set as 0, enabling it to pass through the CI/CD pipeline.</p></td><td><p>All</p></td><td><p>False</p></td></tr>
<tr><td><p>-c| --config-path</p></td><td><p>Change configuration file</p></td><td><p>N/A</p></td><td><p>Changes the cofig file used for the scan.</p></td><td><p>All</p></td><td><p>Configuration.yml</p></td></tr>
<tr><td><p>--include-archive-files</p></td><td><p>Custom extensions to be extracted</p></td><td><p>N/A</p></td><td><p>Submit comma-separated custom archives extensions to be extracted</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--netrc-path</p></td><td><p>Custom NetRc path</p></td><td><p>NetRcPath</p></td><td><p>Specify the path to the NetRc file to be used.</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--sbom-output-name</p></td><td><p>Custom sbom file name</p></td><td><p>SbomOutputName</p></td><td><p>Filename for the SBOM file. Defaults to cx-sbom.json if omitted.</p></td><td><p>Offline</p></td><td><p>cx-sbom.json</p></td></tr>
<tr><td><p>--sbom-output-path</p></td><td><p>Custom sbom file path</p></td><td><p>SbomOutputPath</p></td><td><p>Directory where the SBOM file is written. Defaults to the project directory if omitted.</p></td><td><p>Offline</p></td><td><p>Project directory</p></td></tr>
<tr><td><p>--override-default-excludes</p></td><td><p>Disable default exclusions</p></td><td><p>OverrideDefaultExcludes</p></td><td><p>When this is set, only the folders and files specified in the --excludes flag are excluded.</p></td><td><p>Online, Offline</p></td><td><p>false</p></td></tr>
<tr><td><p>--disable-delta-scan</p></td><td><p>Disable delta scan</p></td><td><p>DisableDeltaScan</p></td><td><p>Override the default behavior of running Delta scans when using Resolver in Checkmarx One.</p><p><strong><strong>Note</strong></strong>: For SCA standalone users, Resolver does not run Delta scans. Therefore, this flag is not relevant for standalone users.</p></td><td><p>Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--no-upload-manifest</p></td><td><p>Disable manifest upload</p></td><td><p>N/A</p></td><td><p>When this argument is set, the manifest files are <strong><strong>not</strong></strong> uploaded to Checkmarx SCA Cloud.</p><p><strong>Tip</strong></p><p>Preventing manifest uploads doesn’t affect the scan's effectiveness, but it may limit Checkmarx SCA’s ability to suggest precise mitigation actions.</p></td><td><p>Online</p></td><td><p>False (i.e., manifest files are uploaded)</p></td></tr>
<tr><td><p>--disable-parameter-sanitization</p></td><td><p>Disable parameters sanitization</p></td><td><p>DisableParameterSanitization</p></td><td><p>Disable sanitization of package managers' additional parameters.</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--sbom-first</p></td><td><p>Enables sbom resolution</p></td><td><p>EnableSbomFirst</p></td><td><p>Enables SBOM generation. When set, a CycloneDX 1.6 JSON file is produced after dependency resolution completes, covering both manifest-resolved and binary-detected components, and written to the output directory.</p></td><td><p>Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>-e| --excludes</p></td><td><p>Excludes</p></td><td><p>ExcludePatterns</p></td><td><p>Specify file and folder patterns to exclude from the zip file being scanned.</p><p>See examples below.</p><p><strong>Tip</strong></p><p>Using this argument adds to the list of exclusions; it does not override the default exclusions.</p></td><td><p>Online, Offline</p></td><td><p>Default excluded folders:</p><p>node_modules,</p><p>bower_components,</p><p>.git,</p><p>vendor,</p><p>Carthage</p></td></tr>
<tr><td><p>--include-extensionless-archives</p></td><td><p>Extensionless files to be extracted</p></td><td><p>N/A</p></td><td><p>Allows extraction of extensionless files</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--extract-archives</p></td><td><p>Extensions to be extracted</p></td><td><p>N/A</p></td><td><p>Submit comma-separated archives extensions to be extracted.</p><p><strong>Tip</strong></p><p>When you use the argument to add custom file types, that overrides the default types. If you want these types to be extracted, you must include them in the comma-separated list.</p></td><td><p>Online, Offline</p></td><td><p>“.zip, .ear, .war,.gz,.tgz,.whl,.rpm”</p><p><strong>Notice</strong></p><p>.gz is only supported for archives with a .tar folder inside.</p></td></tr>
<tr><td><p>--extract-depth</p></td><td><p>Extraction depth level</p></td><td><p>N/A</p></td><td><p>The depth level of file extraction.</p><p><strong>Tip</strong></p><p>Increasing the depth level improves the accuracy of the results but significantly increases the scan time.</p><p><strong>Tip</strong></p><p>This flag is relevant only for packages identified by unpacking archive files (e.g., .jars, .wars etc.), not for those identified via manifest files.</p></td><td><p>Online, Offline</p></td><td><p>1</p></td></tr>
<tr><td><p>--gradle-dev-scopes</p></td><td><p>Gradle Dev Scopes</p></td><td><p>N/A</p></td><td><p>Gradle user-defined dev dependencies scopes.</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--gradle-ignore-modules</p></td><td><p>Gradle Excluded Submodules</p></td><td><p>N/A</p></td><td><p>Ignore Gradle sub-modules.</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--gradle-exclude-scopes</p></td><td><p>Gradle Exclude Scopes</p></td><td><p>N/A</p></td><td><p>Gradle dependencies excluded scopes.</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--gradle-include-modules</p></td><td><p>Gradle Include Modules</p></td><td><p>N/A</p></td><td><p>Gradle includes only the desired project submodules.</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--gradle-include-scopes</p></td><td><p>Gradle Include Scopes</p></td><td><p>N/A</p></td><td><p>Gradle dependencies included scopes.</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--gradle-plugin-scopes</p></td><td><p>Gradle Plugin Scopes</p></td><td><p>N/A</p></td><td><p>Gradle user-defined plugin scopes.</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--help</p></td><td><p>Help</p></td><td><p>N/A</p></td><td><p>Shows a list of supported arguments for SCA Resolver in the console output.</p></td><td><p>All</p></td><td><p>N/A</p></td></tr>
<tr><td><p>--ignore-dev-dependencies</p></td><td><p>Ignore Dev Dependencies</p></td><td><p>IgnoreDevDependencies</p></td><td><p>Ignores dev dependencies in the pre-scan stage.</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--ignore-provided-dependencies</p></td><td><p>Ignore Provided Dependencies</p></td><td><p>IgnoreProvidedDependencies</p></td><td><p>Ignores provided dependencies in the pre-scan stage</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--ignore-test-dependencies</p></td><td><p>Ignore Test Dependencies</p></td><td><p>IgnoreTestDependencies</p></td><td><p>Ignores test dependencies in the pre-scan stage</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--images</p></td><td><p>Images to scan</p></td><td><p>N/A</p></td><td><p>Specify the container images to be scanned as a comma-separated list.</p><p><strong>Tip</strong></p><p>When this flag is used, the <code>--scan-containers</code> flag is also required.</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--ivy-report-target</p></td><td><p>Ivy report target</p></td><td><p>N/A</p></td><td><p>Specify the <code>target name</code> for the target for writing reports when resolving dependencies in Ivy.</p><p><strong>Tip</strong></p><p>If this flag is used, the “Path to save Ivy reports” flag must also be set.</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--log-level</p></td><td><p>Log Level</p></td><td><p>LogLevel</p></td><td><p>This value sets the lowest threshold for log messages.</p><p>Enter one of the following enum values:</p><p><em><em>Verbose</em></em>, <em><em>Debug</em></em>, <em><em>Information</em></em>, <em><em>Warning</em></em>, <em><em>Error</em></em>, <em><em>Fatal</em></em></p></td><td><p>All</p></td><td><p>Information</p></td></tr>
<tr><td><p>N/A</p></td><td><p>Maximum attempts to check scan status</p></td><td><p>ScanReportMaxRetries</p></td><td><p>The maximum number of requests sent to check the status of the scan.</p></td><td><p>All</p></td><td><p>2147483647</p></td></tr>
<tr><td><p>--containers-cache-path</p></td><td><p>Path to cache containers image</p></td><td><p>ContainersImagesCacheDirectory</p></td><td><p>Path to the directory where containers images cache will be written.</p><p><strong>Tip</strong></p><p>Only used when containers scan is enabled.</p></td><td><p>Online, Offline</p></td><td><p>Cache</p></td></tr>
<tr><td><p>--nugetcli-path</p></td><td><p>Path to nuget CLI executable</p></td><td><p>NugetCliPat</p></td><td><p>Specify the path to the NuGet CLI executable to use.</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--manifests-path</p></td><td><p>Path to project’s manifest</p></td><td><p>ManifestsPath</p></td><td><p>When this argument is set, the manifest file in the specified path is uploaded to Checkmarx SCA Cloud.</p></td><td><p>Upload</p></td><td><p>When this flag isn’t used, no manifest file is uploaded.</p></td></tr>
<tr><td><p>--ivy-report-files-dir</p></td><td><p>Path to save Ivy reports</p></td><td><p>N/A</p></td><td><p>Specify the <code>todir</code> for writing reports when resolving dependencies in Ivy.</p><p><strong>Tip</strong></p><p>If this flag is used, the “Ivy report target” flag must also be set.</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--private-dependency-name</p></td><td><p>Private dependency name</p></td><td><p>PrivateDependencyName</p></td><td><p>The name of the private package.</p><p>This flag must be used in conjunction with <code>--private-dependency-version</code> and <code>--private-dependency-type</code>.</p><p><strong>Tip</strong></p><p>You can designate a scan as a "Private Package" and assign a package version to it. Once a private package has been scanned, SCA will identify the risks affecting that package when that package version is used in any of your projects. You can download an article about private packages <a href="https://checkmarx.atlassian.net/wiki/spaces/CR/pages/6594035713/Checkmarx+SCA+Resources#Private-Packages">here</a>.</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--private-dependency-type</p></td><td><p>Private dependency type</p></td><td><p>PrivateDependencyType</p></td><td><p>The package manager used for accessing the private package. For example, Go, Nuget, Npm, maven etc.</p><p><strong>Tip</strong></p><p>The complete list of supported types is available via the Resolver help command.</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--private-dependency-version</p></td><td><p>Private dependency version</p></td><td><p>PrivateDependencyVersion</p></td><td><p>The version of the package.</p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>-t| --project-teams</p></td><td><p>Project Teams</p></td><td><p>N/A</p></td><td><p>Comma-separated list of teams to assign to a newly created project. If the project exists, this is ignored.</p><p>The full team hierarchy should be given, e.g: <code>/CxServer/Team01/Team01a</code></p><p>Team path should be prefixed by a forward slash: <code>/</code></p></td><td><p>Online, Upload</p></td><td><p>Project will be accessible to all users</p></td></tr>
<tr><td><p>--proxies</p></td><td><p>Proxy</p></td><td><p>N/A</p></td><td><p>The proxy to use for internet requests. You can enter comma-separated proxies for HTTP and HTTPS. You can also include authentication credentials for HTTPS. See <a href="running-scans-using-checkmarx-sca-resolver.md#UUID-af718204-6dfc-2b27-439e-419b9157d364_section-idm33346519836294">Proxy Scans</a></p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
<tr><td><p>--python-version</p></td><td><p>Python version</p></td><td><p>PythonVersion</p></td><td><p>Specify the Python version to be used for package resolution.</p><p>Enter one of the following enum values:</p><p><em><em>V2</em></em> or <em><em>V3</em></em></p></td><td><p>Online, Offline</p></td><td><p>V3</p></td></tr>
<tr><td><p>-q| --quiet</p></td><td><p>Quiet mode</p></td><td><p>N/A</p></td><td><p>When this flag is used, logs aren't returned to the console output. However, the logs are still written to the log files.</p></td><td><p>Online</p></td><td><p>False</p></td></tr>
<tr><td><p>--resolver-timeout</p></td><td><p>Resolver Timeout</p></td><td><p>N/A</p></td><td><p>Sets timeout in minutes to resolve dependencies. Fails to resolve if the timeout is reached.</p></td><td><p>Online, Offline</p></td><td><p>0 (infinite)</p></td></tr>
<tr><td><p>--scan-containers</p></td><td><p>Run containers scan</p></td><td><p>N/A</p></td><td><p>Scan the Dockerfiles in your project to identify the container images it uses. See <a href="running-scans-using-checkmarx-sca-resolver.md#UUID-af718204-6dfc-2b27-439e-419b9157d364_section-idm33346502401272">Container Scans</a></p><p><strong>Tip</strong></p><p>Requires installation of Syft v0.83.1 on the machine where you are running Resolver. Download <a href="https://github.com/anchore/syft/releases/tag/v0.83.1">here</a></p></td><td><p>Online, Offline</p></td><td><p>False</p></td></tr>
<tr><td><p>--containers-result-path</p></td><td><p>Save containers result output</p></td><td><p>N/A</p></td><td><p>Save containers results, which is helpful for troubleshooting. You need to specify the path to the directory where you want the output to be saved.</p><p><strong>Tip</strong></p><p>In Offline mode, this is a mandatory parameter. It is also mandatory when scanning via Checkmarx One CLI. For Checkmarx One CLI, the path must be set as <code>&lt;base_folder_path&gt;/.cxsca-container-results.json</code>.</p><ul><li><p>&lt;base_folder_path&gt; must be identical to the value given for <code>-s</code>.</p></li><li><p>The precise file name <code>.cxsca-container-results.json</code> must be used.</p></li></ul></td><td><p>Online</p></td><td><p>None</p></td></tr>
<tr><td><p>--save-evidence-path</p></td><td><p>Save resolved dependency output</p></td><td><p>N/A</p></td><td><p>Saves evidence of the resolved dependencies, which is helpful for troubleshooting. You need to specify the path to the directory where you want the output to be saved.</p></td><td><p>Online</p></td><td><p>None</p></td></tr>
<tr><td><p>--python-package-manager</p></td><td><p>Select Python package manager tool</p></td><td><p>N/A</p></td><td><p>Choose to resolve Python dependencies with pip or uv.</p></td><td><p>Online, Offline</p></td><td><p>pip</p></td></tr>
<tr><td><p>--severity-threshold</p></td><td><p>Severity Threshold</p></td><td><p>SeverityThreshold</p></td><td><p>The vulnerability severity level from which</p><p>to return an error exit code. Enter one of the following enum values: <em><em>Low</em></em>, <em><em>Medium</em></em>, <em><em>High</em></em> or <em><em>None</em></em> (do not test)</p></td><td><p>Online, Upload</p></td><td><p>None</p></td></tr>
<tr><td><p>--detection-types</p></td><td><p>Specifies which type of analysis to run</p></td><td><p>N/A</p></td><td><p>Choose whether to scan binaries only, manifests only, or both.</p><p>Send either binary, manifest or both.</p></td><td><p>Online, Offline</p></td><td><p></p></td></tr>
<tr><td><p>N/A</p></td><td><p>Time between scan report requests</p></td><td><p>ScanReportWaitForFinishDelayInSeconds</p></td><td><p>Time in seconds before resending the request for the scan’s risk report.</p></td><td><p>Online, Upload</p></td><td><p>5</p></td></tr>
<tr><td></td><td><p>Version</p></td><td><p>N/A</p></td><td><p>Prints the version to the console output.</p></td><td><p>All</p></td><td><p>N/A</p></td></tr>
<tr><td><p>N/A</p></td><td><p>Version of Graphviz</p></td><td><p>GraphvizVersion</p></td><td><p>Specify the version of Graphviz to be used for package resolution.</p></td><td><p>Online, Offline</p></td><td><p>N/A</p></td></tr>
<tr><td><p>N/A</p></td><td><p>Version of pipdeptree</p></td><td><p>PipDepTreeVersion</p></td><td><p>Specify the version of pipdeptree to be used for package resolution.</p></td><td><p>Online, Offline</p></td><td><p>None</p></td></tr>
</tbody>
</table>

Samples using some optional arguments:

Linux/MacOS

```
./ScaResolver -s /home/jack/src/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --log-level Debug --save-evidence-path ./evidences.json --extract-archives zip,ear --extract-depth 3 --gradle-exclude-scopes api,testCompile
```

Windows

```
./ScaResolver.exe -s C:\home\jack\src\MyApp -a Checkmarx -u jack -p “demo123!” --log-level Debug --save-evidence-path ./evidences.json --extract-archives zip,ear --extract-depth 3 --gradle-exclude-scopes api,testCompile
```

Sample of folder exclusions:

{% hint style="info" icon="pencil" %}
The syntax shown below excludes only folders with the precise name that is specified. If you would like to exclude all folders that have the specified string anywhere in the file path, then you need to omit the backslashes, like this: `*project2*`.
{% endhint %}

Linux/MacOS

```
./ScaResolver -s /home/jack/src/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' -e '*/project2/*,*/project 3/*'
```

Windows

```
./ScaResolver.exe -s C:\home\jack\src\MyApp -a Checkmarx -u jack -p “demo123!” -e "*\project2\*,*\project 3\*"
```

Sample of file exclusions:

Linux/MacOS

```
./ScaResolver -s /home/jack/src/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' -e '*.ext1,*file name.ext2'
```

Windows

```
./ScaResolver.exe -s C:\home\jack\src\MyApp -a Checkmarx -u jack -p “demo123!” -e "*.ext1,*file name.ext2"
```

Sample of tags:

Linux/MacOS

```
./ScaResolver -s /home/jack/src/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --project-tags "Dev" --scan-tags "version:0.2"-e '*.ext1,*file name.ext2'
```

Windows

```
./ScaResolver.exe -s C:\home\jack\src\MyApp -a Checkmarx -u jack -p “demo123!” --project-tags "Dev" --scan-tags "version:0.2"
```

Sample of private packages:

Linux/MacOS

```
./ScaResolver -s /home/jack/src/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --private-dependency-name 'my-private-package' --private-dependency-version '1.0.0' --private-dependency-type 'Npm'
```

Windows

```
./ScaResolver.exe -s C:\home\jack\src\MyApp -a Checkmarx -u jack -p “demo123!” --private-dependency-name 'my-private-package' --private-dependency-version '1.0.0' --private-dependency-type 'Npm'
```

Sample of SBOM capabilites:

The following example shows how to produce a CycloneDX 1.6 JSON file immediately after dependency resolution completes, covering both manifest-resolved and binary-detected components, and written to the output directory.

Linux/MacOS

```
./ScaResolver -s /home/jack/src/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --sbom-first "true" --sbom-output-name "mysbom.json" --sbom-output-path "C:\mypath"--project-tags "Dev" --scan-tags "version:0.2"-e '*.ext1,*file name.ext2'
```

Windows

```
./ScaResolver.exe -s C:\home\jack\src\MyApp -a Checkmarx -u jack -p “demo123!” --sbom-first "true" --sbom-output-name "mysbom.json" --sbom-output-path "C:\mypath"
```
{% endtab %}
{% tab title="Custom Parameters" %}
{% hint style="info" icon="pencil" %}
The custom parameters enable you to add additional parameters to the scan command. They do not override the package manager flag commands that are built into the Checkmarx SCA Resolver.
{% endhint %}

{% hint style="warning" %}
Certain special characters aren't supported for use in the arguments sent to the package managers. The following is the list of allowed characters:

- Numbers and letters (lower and upper case)
- Blank characters (space, tab, new line, etc)
- \_  -  =  +  \*  .  ,  :  @  '  "  /  \\

It is possible to bypass our sanitization process and allow all characters to pass by adding the `--disable-parameters-sanitization` flag.
{% endhint %}

| Argument | Name | Config file key | Description | Used in mode |
| --- | --- | --- | --- | --- |
| --bower-parameters | Bower Custom Parameters | None | Parameters to be appended to bower package manager directly | Online, Offline |
| --cocoapods-parameters | CocoaPods Custom Parameters | None | Parameters to be appended to CocoaPods package manager directly | Online, Offline |
| --composer-parameters | Composer Custom Parameters | None | Parameters to be appended to composer package manager directly | Online, Offline |
| --gradle-parameters | Gradle Custom Parameters | None | Parameters to be appended to Gradle package manager directly | Online, Offline |
| --ivy-parameters | Ivy Custom Parameters | None | Parameters to be appended to Ivy package manager directly | Online, Offline |
| --lerna-parameters | Lerna Custom Parameters | None | Parameters to be appended to lerna package manager directly | Online, Offline |
| --maven-parameters | Maven Custom Parameters | None | Parameters to be appended to maven package manager directly | Online, Offline |
| --npm-parameters | NPM Custom Parameters | None | Parameters to be appended to npm package manager directly | Online, Offline |
| --nuget-parameters | Nuget Custom Parameters | None | Parameters to be appended to nuget package manager directly | Online, Offline |
| --pip-parameters | Pip Custom Parameters | None | Parameters to be appended to pip package manager directly | Online, Offline |
| --poetry-parameters | Poetry Custom Parameters | None | Parameters to be passed to Poetry package manager directly | Online, Offline |
| --sbt-parameters | Sbt Custom Parameters | None | Parameters to be appended to sbt package manager directly | Online, Offline |
| --yarn-parameters | Yarn Custom Parameters | None | Parameters to be appended to yarn package manager directly | Online, Offline |

{% hint style="info" icon="pencil" %}
All custom parameters are not mandatory.
{% endhint %}

Sample using custom arguments:

Linux/MacOS

```
./ScaResolver -s /home/jack/src/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --gradle-parameters='-PUSERNAME=abc -PPASSWORD=cba'
```

Windows

```
./ScaResolver.exe -s C:\home\jack\src\MyApp -n MyApp -a Checkmarx -u jack -p “demo123!” --gradle-parameters="-PUSERNAME=abc -PPASSWORD=cba"
```
{% endtab %}
{% tab title="Report Arguments" %}
| Argument | Name | Config file key | Description | Enums | Used in mode | Default value |
| --- | --- | --- | --- | --- | --- | --- |
| --report-content | Report Content | None | Specify the type of content that will be included in the report. | <ul><li><p>All</p></li><li><p>Packages</p></li><li><p>Vulnerabilities</p></li><li><p>Licenses</p></li></ul> | Online, Upload | All |
| --report-extension | Report Extension | None | Specify the file type of report.<br>Note: You can specify multiple (comma separated) extension types in order to generate files of each type.<br>Note: CycloneDx reports must be in Json or Xml format. | <ul><li><p>Json</p></li><li><p>Xml</p></li><li><p>Csv (saved as zip with multiple Csv files)</p></li><li><p>Pdf</p></li></ul> | Online, Upload | Json |
| --report-path | Report Path | None | Specify the path to the location where the Report will be saved. | - | Online, Upload | reports |
| --report-type | Report Type | None | You can use this flag to generate a report. There are two types of reports:<br><ul><li><p>Risk Report - A comprehensive report of the risks identified by Checkmarx SCA.</p></li><li><p>CycloneDx - A Software Bill of Materials (SBOM) report using the CycloneDx format.</p></li></ul> | <ul><li><p>Risk</p></li><li><p>CycloneDx</p></li><li><p>None</p></li></ul> | Online, Upload | None |

Risk Report sample:

Linux/MacOS

```
./ScaResolver -s /Users/DemoUser/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --report-extension Pdf,Json,Csv --report-type Risk
```

Windows

```
./ScaResolver.exe -s C:\Users\DemoUser\MyApp -n MyApp -a Checkmarx -u jack -p "demo123!" --report-extension Pdf,Json,Csv --report-type Risk
```

You can generate an SBOM Report in json or xml format when running a scan using Checkmarx SCA Resolver (version 1.5.52+).

SBOM Report sample:

Linux/MacOS

```
./ScaResolver -s /Users/DemoUser/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --report-extension Xml,Json --report-type CycloneDx
```

Windows

```
./ScaResolver.exe -s C:\Users\DemoUser\MyApp -n MyApp -a Checkmarx -u jack -p "demo123!" --report-extension Xml,Json --report-type CycloneDx
```
{% endtab %}
{% tab title="Exploitable Path Arguments" %}
To run a scan using the **Exploitable Path** feature, in addition to the regular mandatory arguments, you also need to add the following arguments, see [Exploitable Path](https://app.gitbook.com/s/XSPACE_USER_GUIDE/exploitable-path).

{% hint style="info" %}
Attributes marked as Mandatory in this table, are mandatory only when running an Exploitable Path scan. When running an Exploitable Path scan in Upload mode, you can either include the attributes that specify the account and Project info or the path to the result file.
{% endhint %}

| Argument | Name | Config file key | Description | Mandatory | Used in | Default value |
| --- | --- | --- | --- | --- | --- | --- |
| --sast-result-path | Path to read SAST results | SastResultPath | Specify the path to the file of the saved SAST results that you are uploading. | For Upload mode, either this attribute with the path to the result file or info about the account and Project is mandatory. | Upload | false |
| --sast-result-path | Path to save SAST results | SastResultPath | Specify the path to the directory/file where the SAST results will be saved (for future upload). | YES (for Offline mode) | Offline | false |
| --cxpassword | SAST Authentication server password | SastPassword | Your password for the SAST Authentication server | YES | All | - |
| --cxuser | SAST Authentication server username | SastUserName | Your username for the SAST Authentication server | YES | All | - |
| --cxprojectid | SAST Project ID | SastProjectId | The ProjectId of the Project that you created in SAST for running the SCA Exploitable Path feature. | Either the Project ID or the Project name is mandatory. | All | - |
| --cxprojectname | SAST Project name | SastProjectName | The Project name of the Project that you created in SAST for running the SCA Exploitable Path feature. | Either the Project ID or the Project name is mandatory. | All | - |
| --cxserver | SAST Server endpoint | SastServer | Your CxServer endpoint.<br>e.g., [https://checkmarxServer/](https://checkmarxServer/) | YES | All | - |
| N/A | Timeout for receiving response from SAST | EngineResultsReceiveTimeOutMinutes | Maximum time to wait to receive the results from the SAST engine. | NO | All | 15 min. |
| N/A | Timeout for sending request to SAST | EngineResultsReceiveTimeOutMinutes | Maximum time to wait to send the request to the SAST engine. | NO | All | 2 min. |
| N/A | Time period to check for SAST results | OldResultsThresholdMinutes | The time period for which SAST results will be checked. If multiple results exist, the most recent will be used.<br>**Tip** Exploitable Path is based on results from the most recent full SAST scan of the project, results from incremental scans aren't considered.<br>**Tip** There is no CLI argument for this parameter, so it must be set in the config file. | NO | All | 1 day |

Sample using Exploitable Path:

Linux/MacOS

```
./ScaResolver -s /home/jack/src/MyApp -n MyApp -a Checkmarx -u jack -p 'demo123!' --cxuser bob --cxpassword 'demoabc!' --cxprojectname DemoCxProject --cxserver 'https://checkmarxServer'
```

Windows

```
./ScaResolver.exe -s C:\home\jack\src\MyApp -a Checkmarx -u jack -p "demo123!" --cxuser bob --cxpassword "demoabc!" --cxprojectname DemoCxProject --cxserver "https://checkmarxServer"
```

<details>
<summary>Exploitable Path offline mode sample</summary>

Offline command (Linux)

```
./ScaResolver offline -s Test -n projectName -r scaResults/results.json --sast-result-path sastResults/results.json --cxuser test --cxpassword test --cxprojectid projectId --cxserver http://localhost
```

Upload command (Linux)

```
./ScaResolver upload -n projectName -r scaResults/results.json --sast-result-path sastResults/results.json -a scaTenant -u scaUser -p scaPassword
```

</details>
{% endtab %}
{% endtabs %}
