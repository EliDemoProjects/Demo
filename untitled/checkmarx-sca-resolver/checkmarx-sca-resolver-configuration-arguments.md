# Checkmarx SCA Resolver Configuration Arguments

Most Checkmarx SCA Resolver configuration parameters can be submitted either as command line arguments or by editing the **configuration.yml** file.

{% hint style="info" icon="pencil" %}
Certain parameters must be submitted via the config file. Therefore, it is mandatory to include the configuration.yml file (which is included in the Checkmarx SCA Resolver download) in the same folder as the ScaResolver binary.
{% endhint %}

{% hint style="info" %}
The info provided on this page relates to running Resolver as a standalone tool. If you are running Resolver via an external platform such as the Checkmarx One CLI tool or plugins, or the CxSAST/CxSCA CLI tool or plugins, then only Offline arguments can be used. In addition, the mandatory arguments differ for different platforms. See the relevant [SAST/SCA Integrations](../../document/preview/7297/#UUID-09af4cb8-95d4-d86a-48f3-5e0e5176366b) documentation for details.
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
* ServerUrl - [https://api-sca.checkmarx.net](https://api-sca.checkmarx.net)
* AuthenticationServerUrl - [https://platform.checkmarx.net](https://platform.checkmarx.net)
* ScaAppUrl - [https://sca.checkmarx.net](https://sca.checkmarx.net)
{% endtab %}

{% tab title="EU Environment" %}
* ServerUrl - [https://eu.api-sca.checkmarx.net](https://eu.api-sca.checkmarx.net)
* AuthenticationServerUrl - [https://eu.platform.checkmarx.net](https://eu.platform.checkmarx.net)
* ScaAppUrl - [https://eu.sca.checkmarx.net](https://eu.sca.checkmarx.net)
{% endtab %}
{% endtabs %}

## Configuration Arguments - Tables and Samples

The following tables describe the supported arguments that can be used in Resolver. You can submit `--help` to get the list of supported parameters.

{% tabs %}
{% tab title="Mandatory Arguments" %}
| Argument                    | Name                                  | Config file key         | Description                                                                                                                                                                                                                       | Used in mode    | Default value                                                    |
| --------------------------- | ------------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ---------------------------------------------------------------- |
| -a\| --account              | Account                               | Account                 | Your SCA account a name.                                                                                                                                                                                                          | Online, Upload  | -                                                                |
| --authentication-server-url | Authentication Server URL<sup>1</sup> | AuthenticationServerUrl | The URL of the SCA Access Control server.                                                                                                                                                                                         | Online, Upload  | [https://platform.checkmarx.net](https://platform.checkmarx.net) |
| --logs-path                 | Logs Directory<sup>2]</sup>           | LogsDirectory           | The default name assigned the logs directory.                                                                                                                                                                                     |                 | logs                                                             |
| -p\| --password             | Password<sup>3]</sup>                 | Password                | <p>The password for your SCA user account.<br><strong>Tip</strong> You can configure a custom Environment Variable to use for the password. This is preferable to including a password in clear text in the config file.</p>      | Online, Upload  | -                                                                |
| --containers-result-path    | Path to read container results        | ContainersResultPath    | <p>Specify the path to the file of the saved containers results that you are uploading.<br><strong>Tip</strong> Mandatory for container scans.</p>                                                                                | Upload          | -                                                                |
| -r\|--resolver-result-path  | Path to read ScaResolver results      | ResolverResultPath      | Specify the path to the file of the saved resolver results that you are uploading.                                                                                                                                                | Upload          | -                                                                |
| --containers-result-path    | Path to save container results        | ContainersResultPath    | <p>Specify the path to the directory/file where the containers results will be saved (for future upload).<br><strong>Tip</strong> Mandatory for container scans, <code>--scan-containers</code>.</p>                              | Offline         | -                                                                |
| -r\|--resolver-result-path  | Path to save ScaResolver results      | ResolverResultPath      | Specify the path to the directory/file where the resolver results will be saved (for future upload).                                                                                                                              | Offline         | -                                                                |
| -n\| --project-name         | Project Name                          | ProjectName             | To scan an existing SCA Project, enter the Project name. Alternatively, you can enter a new Project name in order to create a new Project in SCA.                                                                                 | All             | -                                                                |
| --sso-provider              | Provider name<sup>3]</sup>            | SsoProviderName         | The name of your SSO provider. Alternatively, you can give the name of your Master Access Control instance. For more info see [SAML Authentication for Checkmarx SCA Resolver](saml-authentication-for-checkmarx-sca-resolver.md) | Online, Upload  | -                                                                |
| --sca-app-url               | SCA Application URL<sup>3]</sup>      | ScaAppUrl               | The URL of the SCA web application.                                                                                                                                                                                               | Online, Upload  | [https://sca.checkmarx.net](https://sca.checkmarx.net)           |
| -s\| --scan-path            | Scan Path                             | N/A                     | <p>Path to the folder to be scanned.<br><strong>Note</strong> This must be the path to a local folder that contains the source code, not to a zip archive or a code repository.</p>                                               | Online, Offline | -                                                                |
| --server-url                | Server URL<sup>1]</sup>               | ServerUrl               | The URL of the SCA API server.                                                                                                                                                                                                    | Online, Upload  | [https://api-sca.checkmarx.net](https://api-sca.checkmarx.net)   |
| -u\| --username             | Username<sup>3]</sup>                 | Username                | Your username for the SCA account.                                                                                                                                                                                                | Online, Upload  | -                                                                |

1] The default values for Server URL and Authentication Server URL are preconfigured in the config file, making it unnecessary to submit these arguments in the CLI.

2] The default value for Logs Directory is preconfigured in the config file. There is no argument for adjusting this value in the CLI.

3] Authentication is done either using your Checkmarx SCA credentials, or via your SSO provider. Therefore, you are required to submit either `-u| --username` and `-p| --password` or `--sso-provider` but not both.

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
<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Argument</strong></td><td><strong>Name</strong></td><td><strong>Config file key</strong></td><td><strong>Description</strong></td><td><strong>Used in mode</strong></td><td><strong>Default value</strong></td></tr><tr><td>N/A</td><td>Additional Manifest Patterns</td><td>AdditionalManifestPatterns</td><td><p>Allows the user to specify additional patterns to detect as manifest.</p><p><strong>Tip</strong></p><p>Currently supported only for pip.</p><p>Syntax:</p><pre><code>AdditionalManifestPatterns:  
  pip: 
    - example-*.txt
</code></pre></td><td>Online, Offline</td><td>N/A</td></tr><tr><td>--project-tags</td><td>Add tags to project</td><td>N/A</td><td>Comma-separated tags to be assigned to the project. Tags can be a simple string or a key:value.</td><td>Online, Upload</td><td>None</td></tr><tr><td>--scan-tags</td><td>Add tags to scan</td><td>N/A</td><td>Comma-separated tags to be assigned per scan. Tags can be a simple string or a key:value.</td><td>Online, Upload</td><td>None</td></tr><tr><td>--break-on-manifest-failure</td><td>Break on manifest failure</td><td>BreakOnManifestFailure</td><td>When this flag is used, the scan will fail and error code 9 will be returned when resolution fails for one or more of the manifest files.</td><td>Online, Offline</td><td>False</td></tr><tr><td>--bypass-exitcode</td><td>Bypass exit code</td><td>BypassExitCode</td><td>If set as “true”, exit code will be overridden and set as 0, enabling it to pass through the CI/CD pipeline.</td><td>All</td><td>False</td></tr><tr><td>-c| --config-path</td><td>Change configuration file</td><td>N/A</td><td>Changes the cofig file used for the scan.</td><td>All</td><td>Configuration.yml</td></tr><tr><td>--include-archive-files</td><td>Custom extensions to be extracted</td><td>N/A</td><td>Submit comma-separated custom archives extensions to be extracted</td><td>Online, Offline</td><td>None</td></tr><tr><td>--netrc-path</td><td>Custom NetRc path</td><td>NetRcPath</td><td>Specify the path to the NetRc file to be used.</td><td>Online, Offline</td><td>None</td></tr><tr><td>--sbom-output-name</td><td>Custom sbom file name</td><td>SbomOutputName</td><td>Filename for the SBOM file. Defaults to cx-sbom.json if omitted.</td><td>Offline</td><td>cx-sbom.json</td></tr><tr><td>--sbom-output-path</td><td>Custom sbom file path</td><td>SbomOutputPath</td><td>Directory where the SBOM file is written. Defaults to the project directory if omitted.</td><td>Offline</td><td>Project directory</td></tr><tr><td>--override-default-excludes</td><td>Disable default exclusions</td><td>OverrideDefaultExcludes</td><td>When this is set, only the folders and files specified in the --excludes flag are excluded.</td><td>Online, Offline</td><td>false</td></tr><tr><td>--disable-delta-scan</td><td>Disable delta scan</td><td>DisableDeltaScan</td><td><p>Override the default behavior of running Delta scans when using Resolver in Checkmarx One.</p><p><strong>Note</strong>: For SCA standalone users, Resolver does not run Delta scans. Therefore, this flag is not relevant for standalone users.</p></td><td>Offline</td><td>False</td></tr><tr><td>--no-upload-manifest</td><td>Disable manifest upload</td><td>N/A</td><td><p>When this argument is set, the manifest files are <strong>not</strong> uploaded to Checkmarx SCA Cloud.</p><p><strong>Tip</strong></p><p>Preventing manifest uploads doesn’t affect the scan's effectiveness, but it may limit Checkmarx SCA’s ability to suggest precise mitigation actions.</p></td><td>Online</td><td>False (i.e., manifest files are uploaded)</td></tr><tr><td>--disable-parameter-sanitization</td><td>Disable parameters sanitization</td><td>DisableParameterSanitization</td><td>Disable sanitization of package managers' additional parameters.</td><td>Online, Offline</td><td>False</td></tr><tr><td>--sbom-first</td><td>Enables sbom resolution</td><td>EnableSbomFirst</td><td>Enables SBOM generation. When set, a CycloneDX 1.6 JSON file is produced after dependency resolution completes, covering both manifest-resolved and binary-detected components, and written to the output directory.</td><td>Offline</td><td>False</td></tr><tr><td>-e| --excludes</td><td>Excludes</td><td>ExcludePatterns</td><td><p>Specify file and folder patterns to exclude from the zip file being scanned.</p><p>See examples below.</p><p><strong>Tip</strong></p><p>Using this argument adds to the list of exclusions; it does not override the default exclusions.</p></td><td>Online, Offline</td><td><p>Default excluded folders:</p><p>node_modules,</p><p>bower_components,</p><p>.git,</p><p>vendor,</p><p>Carthage</p></td></tr><tr><td>--include-extensionless-archives</td><td>Extensionless files to be extracted</td><td>N/A</td><td>Allows extraction of extensionless files</td><td>Online, Offline</td><td>None</td></tr><tr><td>--extract-archives</td><td>Extensions to be extracted</td><td>N/A</td><td><p>Submit comma-separated archives extensions to be extracted.</p><p><strong>Tip</strong></p><p>When you use the argument to add custom file types, that overrides the default types. If you want these types to be extracted, you must include them in the comma-separated list.</p></td><td>Online, Offline</td><td><p>“.zip, .ear, .war,.gz,.tgz,.whl,.rpm”</p><p><strong>Notice</strong></p><p>.gz is only supported for archives with a .tar folder inside.</p></td></tr><tr><td>--extract-depth</td><td>Extraction depth level</td><td>N/A</td><td><p>The depth level of file extraction.</p><p><strong>Tip</strong></p><p>Increasing the depth level improves the accuracy of the results but significantly increases the scan time.</p><p><strong>Tip</strong></p><p>This flag is relevant only for packages identified by unpacking archive files (e.g., .jars, .wars etc.), not for those identified via manifest files.</p></td><td>Online, Offline</td><td>1</td></tr><tr><td>--gradle-dev-scopes</td><td>Gradle Dev Scopes</td><td>N/A</td><td>Gradle user-defined dev dependencies scopes.</td><td>Online, Offline</td><td>None</td></tr><tr><td>--gradle-ignore-modules</td><td>Gradle Excluded Submodules</td><td>N/A</td><td>Ignore Gradle sub-modules.</td><td>Online, Offline</td><td>None</td></tr><tr><td>--gradle-exclude-scopes</td><td>Gradle Exclude Scopes</td><td>N/A</td><td>Gradle dependencies excluded scopes.</td><td>Online, Offline</td><td>None</td></tr><tr><td>--gradle-include-modules</td><td>Gradle Include Modules</td><td>N/A</td><td>Gradle includes only the desired project submodules.</td><td>Online, Offline</td><td>None</td></tr><tr><td>--gradle-include-scopes</td><td>Gradle Include Scopes</td><td>N/A</td><td>Gradle dependencies included scopes.</td><td>Online, Offline</td><td>None</td></tr><tr><td>--gradle-plugin-scopes</td><td>Gradle Plugin Scopes</td><td>N/A</td><td>Gradle user-defined plugin scopes.</td><td>Online, Offline</td><td>None</td></tr><tr><td>--help</td><td>Help</td><td>N/A</td><td>Shows a list of supported arguments for SCA Resolver in the console output.</td><td>All</td><td>N/A</td></tr><tr><td>--ignore-dev-dependencies</td><td>Ignore Dev Dependencies</td><td>IgnoreDevDependencies</td><td>Ignores dev dependencies in the pre-scan stage.</td><td>Online, Offline</td><td>False</td></tr><tr><td>--ignore-provided-dependencies</td><td>Ignore Provided Dependencies</td><td>IgnoreProvidedDependencies</td><td>Ignores provided dependencies in the pre-scan stage</td><td>Online, Offline</td><td>False</td></tr><tr><td>--ignore-test-dependencies</td><td>Ignore Test Dependencies</td><td>IgnoreTestDependencies</td><td>Ignores test dependencies in the pre-scan stage</td><td>Online, Offline</td><td>False</td></tr><tr><td>--images</td><td>Images to scan</td><td>N/A</td><td><p>Specify the container images to be scanned as a comma-separated list.</p><p><strong>Tip</strong></p><p>When this flag is used, the <code>--scan-containers</code> flag is also required.</p></td><td>Online, Offline</td><td>None</td></tr><tr><td>--ivy-report-target</td><td>Ivy report target</td><td>N/A</td><td><p>Specify the <code>target name</code> for the target for writing reports when resolving dependencies in Ivy.</p><p><strong>Tip</strong></p><p>If this flag is used, the “Path to save Ivy reports” flag must also be set.</p></td><td>Online, Offline</td><td>False</td></tr><tr><td>--log-level</td><td>Log Level</td><td>LogLevel</td><td><p>This value sets the lowest threshold for log messages.</p><p>Enter one of the following enum values:</p><p><em>Verbose</em>, <em>Debug</em>, <em>Information</em>, <em>Warning</em>, <em>Error</em>, <em>Fatal</em></p></td><td>All</td><td>Information</td></tr><tr><td>N/A</td><td>Maximum attempts to check scan status</td><td>ScanReportMaxRetries</td><td>The maximum number of requests sent to check the status of the scan.</td><td>All</td><td>2147483647</td></tr><tr><td>--containers-cache-path</td><td>Path to cache containers image</td><td>ContainersImagesCacheDirectory</td><td><p>Path to the directory where containers images cache will be written.</p><p><strong>Tip</strong></p><p>Only used when containers scan is enabled.</p></td><td>Online, Offline</td><td>Cache</td></tr><tr><td>--nugetcli-path</td><td>Path to nuget CLI executable</td><td>NugetCliPat</td><td>Specify the path to the NuGet CLI executable to use.</td><td>Online, Offline</td><td>False</td></tr><tr><td>--manifests-path</td><td>Path to project’s manifest</td><td>ManifestsPath</td><td>When this argument is set, the manifest file in the specified path is uploaded to Checkmarx SCA Cloud.</td><td>Upload</td><td>When this flag isn’t used, no manifest file is uploaded.</td></tr><tr><td>--ivy-report-files-dir</td><td>Path to save Ivy reports</td><td>N/A</td><td><p>Specify the <code>todir</code> for writing reports when resolving dependencies in Ivy.</p><p><strong>Tip</strong></p><p>If this flag is used, the “Ivy report target” flag must also be set.</p></td><td>Online, Offline</td><td>False</td></tr><tr><td>--private-dependency-name</td><td>Private dependency name</td><td>PrivateDependencyName</td><td><p>The name of the private package.</p><p>This flag must be used in conjunction with <code>--private-dependency-version</code> and <code>--private-dependency-type</code>.</p><p><strong>Tip</strong></p><p>You can designate a scan as a "Private Package" and assign a package version to it. Once a private package has been scanned, SCA will identify the risks affecting that package when that package version is used in any of your projects. You can download an article about private packages <a href="https://checkmarx.atlassian.net/wiki/spaces/CR/pages/6594035713/Checkmarx+SCA+Resources#Private-Packages">here</a>.</p></td><td>Online, Offline</td><td>False</td></tr><tr><td>--private-dependency-type</td><td>Private dependency type</td><td>PrivateDependencyType</td><td><p>The package manager used for accessing the private package. For example, Go, Nuget, Npm, maven etc.</p><p><strong>Tip</strong></p><p>The complete list of supported types is available via the Resolver help command.</p></td><td>Online, Offline</td><td>False</td></tr><tr><td>--private-dependency-version</td><td>Private dependency version</td><td>PrivateDependencyVersion</td><td>The version of the package.</td><td>Online, Offline</td><td>False</td></tr><tr><td>-t| --project-teams</td><td>Project Teams</td><td>N/A</td><td><p>Comma-separated list of teams to assign to a newly created project. If the project exists, this is ignored.</p><p>The full team hierarchy should be given, e.g: <code>/CxServer/Team01/Team01a</code></p><p>Team path should be prefixed by a forward slash: <code>/</code></p></td><td>Online, Upload</td><td>Project will be accessible to all users</td></tr><tr><td>--proxies</td><td>Proxy</td><td>N/A</td><td>The proxy to use for internet requests. You can enter comma-separated proxies for HTTP and HTTPS. You can also include authentication credentials for HTTPS. See <a href="running-scans-using-checkmarx-sca-resolver.md#UUID-af718204-6dfc-2b27-439e-419b9157d364_section-idm33346519836294">Proxy Scans</a></td><td>Online, Offline</td><td>None</td></tr><tr><td>--python-version</td><td>Python version</td><td>PythonVersion</td><td><p>Specify the Python version to be used for package resolution.</p><p>Enter one of the following enum values:</p><p><em>V2</em> or <em>V3</em></p></td><td>Online, Offline</td><td>V3</td></tr><tr><td>-q| --quiet</td><td>Quiet mode</td><td>N/A</td><td>When this flag is used, logs aren't returned to the console output. However, the logs are still written to the log files.</td><td>Online</td><td>False</td></tr><tr><td>--resolver-timeout</td><td>Resolver Timeout</td><td>N/A</td><td>Sets timeout in minutes to resolve dependencies. Fails to resolve if the timeout is reached.</td><td>Online, Offline</td><td>0 (infinite)</td></tr><tr><td>--scan-containers</td><td>Run containers scan</td><td>N/A</td><td><p>Scan the Dockerfiles in your project to identify the container images it uses. See <a href="running-scans-using-checkmarx-sca-resolver.md#UUID-af718204-6dfc-2b27-439e-419b9157d364_section-idm33346502401272">Container Scans</a></p><p><strong>Tip</strong></p><p>Requires installation of Syft v0.83.1 on the machine where you are running Resolver. Download <a href="https://github.com/anchore/syft/releases/tag/v0.83.1">here</a></p></td><td>Online, Offline</td><td>False</td></tr><tr><td>--containers-result-path</td><td>Save containers result output</td><td>N/A</td><td><p>Save containers results, which is helpful for troubleshooting. You need to specify the path to the directory where you want the output to be saved.</p><p><strong>Tip</strong></p><p>In Offline mode, this is a mandatory parameter. It is also mandatory when scanning via Checkmarx One CLI. For Checkmarx One CLI, the path must be set as <code>&#x3C;base_folder_path>/.cxsca-container-results.json</code>.</p><ul><li>&#x3C;base_folder_path> must be identical to the value given for <code>-s</code>.</li><li>The precise file name <code>.cxsca-container-results.json</code> must be used.</li></ul></td><td>Online</td><td>None</td></tr><tr><td>--save-evidence-path</td><td>Save resolved dependency output</td><td>N/A</td><td>Saves evidence of the resolved dependencies, which is helpful for troubleshooting. You need to specify the path to the directory where you want the output to be saved.</td><td>Online</td><td>None</td></tr><tr><td>--python-package-manager</td><td>Select Python package manager tool</td><td>N/A</td><td>Choose to resolve Python dependencies with pip or uv.</td><td>Online, Offline</td><td>pip</td></tr><tr><td>--severity-threshold</td><td>Severity Threshold</td><td>SeverityThreshold</td><td><p>The vulnerability severity level from which</p><p>to return an error exit code. Enter one of the following enum values: <em>Low</em>, <em>Medium</em>, <em>High</em> or <em>None</em> (do not test)</p></td><td>Online, Upload</td><td>None</td></tr><tr><td>--detection-types</td><td>Specifies which type of analysis to run</td><td>N/A</td><td><p>Choose whether to scan binaries only, manifests only, or both.</p><p>Send either binary, manifest or both.</p></td><td>Online, Offline</td><td></td></tr><tr><td>N/A</td><td>Time between scan report requests</td><td>ScanReportWaitForFinishDelayInSeconds</td><td>Time in seconds before resending the request for the scan’s risk report.</td><td>Online, Upload</td><td>5</td></tr><tr><td></td><td>Version</td><td>N/A</td><td>Prints the version to the console output.</td><td>All</td><td>N/A</td></tr><tr><td>N/A</td><td>Version of Graphviz</td><td>GraphvizVersion</td><td>Specify the version of Graphviz to be used for package resolution.</td><td>Online, Offline</td><td>N/A</td></tr><tr><td>N/A</td><td>Version of pipdeptree</td><td>PipDepTreeVersion</td><td>Specify the version of pipdeptree to be used for package resolution.</td><td>Online, Offline</td><td>None</td></tr></tbody></table>

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

* Numbers and letters (lower and upper case)
* Blank characters (space, tab, new line, etc)
* \_  -  =  +  \*  .  ,  :  @  '  "  /  \\

It is possible to bypass our sanitization process and allow all characters to pass by adding the `--disable-parameters-sanitization` flag.
{% endhint %}

| Argument               | Name                        | Config file key | Description                                                     | Used in mode    |
| ---------------------- | --------------------------- | --------------- | --------------------------------------------------------------- | --------------- |
| --bower-parameters     | Bower Custom Parameters     | None            | Parameters to be appended to bower package manager directly     | Online, Offline |
| --cocoapods-parameters | CocoaPods Custom Parameters | None            | Parameters to be appended to CocoaPods package manager directly | Online, Offline |
| --composer-parameters  | Composer Custom Parameters  | None            | Parameters to be appended to composer package manager directly  | Online, Offline |
| --gradle-parameters    | Gradle Custom Parameters    | None            | Parameters to be appended to Gradle package manager directly    | Online, Offline |
| --ivy-parameters       | Ivy Custom Parameters       | None            | Parameters to be appended to Ivy package manager directly       | Online, Offline |
| --lerna-parameters     | Lerna Custom Parameters     | None            | Parameters to be appended to lerna package manager directly     | Online, Offline |
| --maven-parameters     | Maven Custom Parameters     | None            | Parameters to be appended to maven package manager directly     | Online, Offline |
| --npm-parameters       | NPM Custom Parameters       | None            | Parameters to be appended to npm package manager directly       | Online, Offline |
| --nuget-parameters     | Nuget Custom Parameters     | None            | Parameters to be appended to nuget package manager directly     | Online, Offline |
| --pip-parameters       | Pip Custom Parameters       | None            | Parameters to be appended to pip package manager directly       | Online, Offline |
| --poetry-parameters    | Poetry Custom Parameters    | None            | Parameters to be passed to Poetry package manager directly      | Online, Offline |
| --sbt-parameters       | Sbt Custom Parameters       | None            | Parameters to be appended to sbt package manager directly       | Online, Offline |
| --yarn-parameters      | Yarn Custom Parameters      | None            | Parameters to be appended to yarn package manager directly      | Online, Offline |

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
| Argument           | Name             | Config file key | Description                                                                                                                                                                                                                                                                       | Enums                                                                                             | Used in mode   | Default value |
| ------------------ | ---------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------- | ------------- |
| --report-content   | Report Content   | None            | Specify the type of content that will be included in the report.                                                                                                                                                                                                                  | <ul><li>All</li><li>Packages</li><li>Vulnerabilities</li><li>Licenses</li></ul>                   | Online, Upload | All           |
| --report-extension | Report Extension | None            | <p>Specify the file type of report.<br>Note: You can specify multiple (comma separated) extension types in order to generate files of each type.<br>Note: CycloneDx reports must be in Json or Xml format.</p>                                                                    | <ul><li>Json</li><li>Xml</li><li>Csv (saved as zip with multiple Csv files)</li><li>Pdf</li></ul> | Online, Upload | Json          |
| --report-path      | Report Path      | None            | Specify the path to the location where the Report will be saved.                                                                                                                                                                                                                  | -                                                                                                 | Online, Upload | reports       |
| --report-type      | Report Type      | None            | <p>You can use this flag to generate a report. There are two types of reports:<br></p><ul><li>Risk Report - A comprehensive report of the risks identified by Checkmarx SCA.</li><li>CycloneDx - A Software Bill of Materials (SBOM) report using the CycloneDx format.</li></ul> | <ul><li>Risk</li><li>CycloneDx</li><li>None</li></ul>                                             | Online, Upload | None          |

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

| Argument           | Name                                     | Config file key                    | Description                                                                                                                                                                                                                                                                                                                                                                                           | Mandatory                                                                                                                   | Used in | Default value |
| ------------------ | ---------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------- | ------------- |
| --sast-result-path | Path to read SAST results                | SastResultPath                     | Specify the path to the file of the saved SAST results that you are uploading.                                                                                                                                                                                                                                                                                                                        | For Upload mode, either this attribute with the path to the result file or info about the account and Project is mandatory. | Upload  | false         |
| --sast-result-path | Path to save SAST results                | SastResultPath                     | Specify the path to the directory/file where the SAST results will be saved (for future upload).                                                                                                                                                                                                                                                                                                      | YES (for Offline mode)                                                                                                      | Offline | false         |
| --cxpassword       | SAST Authentication server password      | SastPassword                       | Your password for the SAST Authentication server                                                                                                                                                                                                                                                                                                                                                      | YES                                                                                                                         | All     | -             |
| --cxuser           | SAST Authentication server username      | SastUserName                       | Your username for the SAST Authentication server                                                                                                                                                                                                                                                                                                                                                      | YES                                                                                                                         | All     | -             |
| --cxprojectid      | SAST Project ID                          | SastProjectId                      | The ProjectId of the Project that you created in SAST for running the SCA Exploitable Path feature.                                                                                                                                                                                                                                                                                                   | Either the Project ID or the Project name is mandatory.                                                                     | All     | -             |
| --cxprojectname    | SAST Project name                        | SastProjectName                    | The Project name of the Project that you created in SAST for running the SCA Exploitable Path feature.                                                                                                                                                                                                                                                                                                | Either the Project ID or the Project name is mandatory.                                                                     | All     | -             |
| --cxserver         | SAST Server endpoint                     | SastServer                         | <p>Your CxServer endpoint.<br>e.g., <a href="https://checkmarxserver/">https://checkmarxServer/</a></p>                                                                                                                                                                                                                                                                                               | YES                                                                                                                         | All     | -             |
| N/A                | Timeout for receiving response from SAST | EngineResultsReceiveTimeOutMinutes | Maximum time to wait to receive the results from the SAST engine.                                                                                                                                                                                                                                                                                                                                     | NO                                                                                                                          | All     | 15 min.       |
| N/A                | Timeout for sending request to SAST      | EngineResultsReceiveTimeOutMinutes | Maximum time to wait to send the request to the SAST engine.                                                                                                                                                                                                                                                                                                                                          | NO                                                                                                                          | All     | 2 min.        |
| N/A                | Time period to check for SAST results    | OldResultsThresholdMinutes         | <p>The time period for which SAST results will be checked. If multiple results exist, the most recent will be used.<br><strong>Tip</strong> Exploitable Path is based on results from the most recent full SAST scan of the project, results from incremental scans aren't considered.<br><strong>Tip</strong> There is no CLI argument for this parameter, so it must be set in the config file.</p> | NO                                                                                                                          | All     | 1 day         |

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
