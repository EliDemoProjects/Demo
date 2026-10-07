# Installing Supported Package Managers for Resolver

To successfully resolve dependencies with Checkmarx SCA Resolver, you need to install the relevant package managers and other prerequisites in the environment where you will be running Resolver. You also need to prepare the project for package resolution by making sure that it is in a buildable state and that the relevant manifest files are included in the project directory.

When you run a scan, Checkmarx SCA uses your installed package managers to build a list of dependencies.

The following sections explain how to prepare your environment to run scans using Resolver. Documentation is provided separately for each supported package manager.

{% hint style="info" icon="pencil" %}
The documentation also provides test commands that can be run as part of your troubleshooting process in order to ensure that dependency resolution can succeed.
{% endhint %}

## Java Support in Checkmarx SCA

### Maven Dependency Resolver

**Manifest files:** `pom.xml`

**Package Manager used:** `Maven`

**Prerequisites:**

- JDK installed under the JAVA_HOME environment variable
- Make sure that any additional SDK needed for resolving dependencies in your project (e.g., Android SDK) is available in your local environment

#### Installation

Debian install command:

```
apt-get install maven
```

To ensure Maven is installed, run: `mvn --version` inside the project directory

If Maven is correctly installed, you should receive a message indicating which version is installed on your machine.

#### Dependency Resolution

Checkmarx SCA Resolver uses Maven to extract the dependency graph.

This process downloads the dependencies to the local cache folder (usually `.m2` ) and inspects the pom.xml files of the dependencies recursively to construct the graph.

It requires connectivity to a Maven repository to download those dependencies. By default, Maven uses the [Central Maven repo](https://repo.maven.apache.org/maven2/) but other repositories may be configured in a `settings.xml` file in the project root or in the global Maven folder in the local machine.

{% hint style="info" icon="pencil" %}
If you want to apply the settings in your `settings.xml` file to all `pom.xml` resolution, you can add the `settings.xml` file to a `.cxsca.configurations` folder in the root of the project. In this case, Checkmarx SCA will apply these settings to each module and sub-module in the project, overriding the local `settings.xml` settings.
{% endhint %}

**Testing Dependency Resolution**

You can test whether the dependency tree can be extracted successfully, by running the following command inside the folder where the manifest exists:

```
mvn dependency:tree
```

**Troubleshooting**

The following command can be used to troubleshoot problems with the dependency resolution.

```
mvn install -DskipTests
```

**Dev Dependencies**

Any dependency marked with `<scope>test</scope>` is considered a Dev dependency in Checkmarx SCA

#### Multi-Module Maven project

A multi-module project has a root `pom.xml` file and multiple modules, each in a sub-directory.

The root `pom.xml` has the following structure:

```
  <modules>
    <module>module1</module>
    <module>module2</module>
  </modules>
```

To successfully resolve dependencies, the project needs to be in a "buildable" state.

{% hint style="info" icon="pencil" %}
If your multi-module code fails the dependency tree generation, try building it first and then executing the dependency tree command. If it succeeds post-build, it is possible that one of your modules is missing an explicit dependency statement for a dependency that is fulfilled due to module build order.
{% endhint %}

If SCA Resolver is not being run “post build”, please run the following command before invoking the Resolver scan.

```
mvn install -DskipTests
```

{% hint style="info" icon="pencil" %}
When running Resolver via a third party plugin, make sure that Resolver is executed only for the parent module and not for each of the sub-modules.

For example, for the exec-maven-plugin, the `exec:exec` profile that runs the SCA command needs the `--projects .` argument, with the `.` indicating that only the parent module is compiled, e.g., `mvn -f <PATH_TO_PARENT_PROJECT_POM.XML> -s <ABSOLUTE_PATH_TO_settings.xml> exec:exec --activate-profiles sca --errors --projects .`
{% endhint %}

### Gradle Dependency Resolver

**Manifest files:** `build.gradle` , `build.gradle.kts`

**Package Manager used:** `gradle`

**Prerequisites:**

- JDK installed under the JAVA_HOME environment variable
- Make sure that any additional SDK needed for resolving dependencies in your project (e.g., Android SDK) is available in your local environment

#### Installation

Debian install command:

```
apt-get install gradle
```

To ensure Gradle is installed, run: `gradle --version` inside the project directory

#### Dependency Resolution

The dependency resolution process downloads the dependencies to the local cache folder (usually `.gradle` )

It requires connectivity to a java repository to download those dependencies. By default, the Maven Central is used ([link](https://repo.maven.apache.org/maven2/)) but other repositories may be configured in a `build.gradle` file, or in global Gradle settings.

##### Dev Scopes

Each Gradle scope that contains the word "test" or "development" is defaulted to `dev scope`.

##### Test

Run this command inside the folder where the manifest exists, to test whether the dependency tree can be extracted successfully:

```
gradle dependencies -q --no-daemon -Dorg.gradle.jvmargs=-Xmx1g
```

#### Multi-Module Gradle project

A multi-module project has a `settings.gradle` file with list of included modules. Each module resides in a sub-directory.

Checkmarx SCA Resolver recognizes this file, and resolves the modules of the project one-by-one using the main settings, calling the following command in the root folder per module (give by `modulename`):

```
gradle modulename:dependencies -q --no-daemon -Dorg.gradle.jvmargs=-Xmx1g
```

#### Gradle Wrapper

Gradle is commonly shipped with a wrapper script, called `gradlew` in the root directory of the project.

Checkmarx SCA Resolver detects the wrapper and uses the script instead of the global “gradle” command.

For example:

```
./gradlew dependencies -q --no-daemon -Dorg.gradle.jvmargs=-Xmx1g
```

Invoking the `gradlew` script may download and compile a desired Gradle version, usually within the `gradle/wrapper/gradle-wrapper.properties` file. Gradle Wrapper requires JRE to run and install Gradle.

To learn more, visit [https://docs.gradle.org/current/userguide/gradle_wrapper.html](https://docs.gradle.org/current/userguide/gradle_wrapper.html)

### Ivy Dependency Resolver

**Manifest files:** `build.xml`, `ivy.xml`

**Package Manager used:** `Apache Ivy`

**Prerequisites:** JDK installed under the JAVA_HOME environment variable

#### Installation

Debian:

1. Download Apache Ant from [https://downloads.apache.org/ant/binaries/](https://downloads.apache.org/ant/binaries/) (version 1.10.x is tested and approved).
2. Uncompress the downloaded file into a directory (ANT_HOME).
3. Set the `ANT_HOME` environment variable to the directory where the uncompressed Apache Ant files were saved.
4. Add `${ANT_HOME}/bin` to the `PATH` environment variable.
5. Download Apache Ivy from [https://downloads.apache.org/ant/ivy/](https://downloads.apache.org/ant/ivy/) (version 2.5.x is tested and approved).
6. Uncompress the downloaded file into a directory.
7. Copy `apache-ivy-2.5.x/ivy-2.5.x.jar` from the Apache directory to `${ANT_HOME}/lib`.
8. To ensure Apache Ant is installed, run `ant -version`
9. To ensure Apache Ivy is installed, run ant inside your Ivy project folder

**Dependency Resolution**

Each `ivy.xml` file will tentatively be associated with a `build.xml` file. For each ivy.xml file, configurations will be fetched. Each corresponding build.xml file will be modified to contain a specific target which will download the dependencies to the local cache folder (usually `.ivy2`) and generate XML report files based on the configurations fetched from `ivy.xml`.

The XML report files will be used to construct the dependency tree.

This process requires connectivity to a repository to download those dependencies. By default, Apache Ivy uses the Central Maven repo ([https://repo.maven.apache.org/maven2/](https://repo.maven.apache.org/maven2/) ) but other repositories may be configured in an ivysettings.xml file.

At the end of the process, `build.xml` files which were modified will be restored back to their original content.

**Test**

Check the configurations for a particular `ivy.xml`.

Add the following target to the corresponding build.xml (inside `<project> tag`), ensuring that `{CONFS}` contains a comma separated list of the configurations from `ivy.xml`.

```
    <target name="generateIvyReportsforDependencyScan" description="Generate Ivy report files">

        <ivy:resolve />

        <ivy:report graph="false" xsl="false" xml="true" conf="{CONFS}" todir="./ivyReports" />

    </target>
```

Run `ant generateIvyReportsforDependencyScan` in `build.xml` location and check that the `ivyReports` folder was created and contains one .xml file per specified configuration.

## .NET Support in Checkmarx SCA

### NuGet Dependency Resolver

**Manifest files:** `*.csproj`, `packages.config`, `*.vbproj`

**Package Manager used:** `dotnet cli` or `nuget cli`

For `dotnet cli`, the minimum required SDK version is 2.1.816.

It is required to have either `dotnet cli` or `nuget cli` installed. If, due to your project requirements, you have both package managers installed, `dotnet cli` will be tried first and only if it fails will `nuget cli` be used.

#### Installation

Install `dotnet cli` or `nuget cli`, according to your project requirements.

To test dotnet installation, run the following command:

```
dotnet --version
```

To test nuget installation, run the following command:

```
nuget
```

#### Dependency Resolution

NuGet restore command downloads the dependencies to the local machine. The `nuget.config` file is used to configure custom repositories to be used.

Checkmarx SCA Resolver uses NuGet to create a lock file and parses it to extract the full dependency graph.

{% hint style="info" icon="pencil" %}
If you want to apply the settings in your `nuget.config` file to all `*.csproj` resolution, you can add the `nuget.config` file to a `.cxsca.configurations` folder in the root of the project. In this case, Checkmarx SCA will apply these settings to each module and sub-module in the project, overriding the local `nuget.config` settings.
{% endhint %}

**Test**

Checkmarx SCA Resolver requires the project to be in a ‘buildable’ state for the packages to be resolved.

Depending on which package manager you are using, run the appropriate command inside the folder where the manifest exists. A file named `package.lock.json` is created with the dependency tree.

For dotnet cli, run:

```
dotnet restore --force-evaluate --use-lock-file
```

For nuget cli, run:

```
nuget restore -Force -UseLockFile
```

## JavaScript Support in Checkmarx SCA

### NPM Dependency Resolver

**Manifest files:** `package.json`(required), `package-lock.json`

Package Manager used: `npm`

#### Installation

Requirements:

- NPM package manager version 6.x or version 8 from 8.18.0 and above
- Git client (some npm packages are directly pulled from a Git repo)
- Optional: Lerna - for Lerna projects (see below)

Debian install command:

```
apt-get install npm git
npm -g install npm@8.11.0
npm install -g lerna
```

Alpine install command:

```
apk add --update npm git
npm -g install npm@8.11.0
npm install -g lerna
```

To ensure NPM is installed, run: `npm --version`

#### Dependency Resolution

Checkmarx SCA Resolver uses NPM to parse the lock file (`package-lock.json`) and to extract the dependency graph. If the lock file does not exist, the Resolver creates it.

When creating a lock file, NPM connects to the NPM registry to collect metadata.

Checkmarx SCA Resolver attempts to create a lock file without installing dependencies, by using the `--package-lock-only` flag to the `npm install` command - this is the default behavior.

In some specific cases where package-lock creation is disabled by the project configuration, the Resolver runs a regular install which downloads the dependencies to a `node_modules` folder.

Custom NPM registries may be configured inside the `package.json` file, or in project / global configurations, usually `.npmrc` files.

{% hint style="info" icon="pencil" %}
If you want to apply the settings in your `.npmrc` file to all `package.json` resolution, you can add the `.npmrc` file to a `.cxsca.configurations` folder in the root of the project. In this case, Checkmarx SCA will apply these settings to each module and sub-module in the project, overriding the local `.npmrc` settings.
{% endhint %}

**Test**

To generate a lock file, run the following command inside the project directory (a `package-lock.json` file is created):

```
npm i --package-lock-only
```

If creating a lock file is disabled by the NPM configuration, run the following command:

`npm install --ignore-scripts` instead.

If the file already exists, or created in the step above, run the following command to extract the dependency graph:

```
npm ls --json
```

**Dev Dependencies**

Any dependency under `devDependencies` section is considered Dev.

To generate a list of dev dependencies, Checkmarx SCA Resolver runs the following command on the lock file.

For NPM version 6:

```
npm ls --json --dev
```

For NPM version 7 or higher:

```
npm ls --json --include dev
```

#### Monorepo Projects using Lerna

This project structure uses Lerna build tool to manage multiple NPM modules inside one project.

The root folder of the project has a `lerna.json` file defining the modules.

Simply resolving each module individually will be inaccurate since peer modules reference each other.

Checkmarx SCA Resolver recognizes the use of Lerna, and uses it to extract the complete dependency graph.

The command used is:

```
lerna bootstrap --hoist
```

This creates a lock file in the root folder with the complete project dependencies.

### Yarn Dependency Resolver

**Manifest files:** `package.json`(required), `yarn.lock`(required)

**Package Manager used:** `yarn`

#### Installation

Requirements:

- Yarn
- Git client (some npm packages are directly pulled from a Git repo)

Debian install command:

```
apt-get install yarn git
```

To ensure Yarn is installed, run: `yarn --version`

#### Dependency Resolution

Checkmarx SCA Resolver parses the lock file (`yarn.lock`) and to extract the dependency graph. If the lock file does not exist, the Resolver creates it.

When creating a lock file, Yarn connects to the NPM registry to collect metadata and downloads the dependencies to the local machine

Custom NPM registries may be configured inside the `package.json` file, or in project / global configurations, usually `.yarnrc`files.

**Test**

To generate a lock file, run the following command inside the project directory. A `yarn.lock` file is created.

```
yarn install --ignore-scripts
```

**Dev Dependencies**

Any dependency under `devDependencies` in the `package.json` file is considered as a dev dependency.

#### Yarn Workspaces

This project structure uses Yarn feature to manage multiple modules inside one project.

The `package.json` file has a `workspaces` section that lists the local paths of modules

Checkmarx SCA Resolver recognizes the use of Yarn Workspaces, and installs the dependencies from the root folder location only, running `yarn install --ignore-scripts`

This creates a lock file in the root folder with the complete project dependencies.

### Bower Dependency Resolver

**Manifest files:** `bower.json`

**Package Manager used:** `bower`

#### Installation

Requirements:

- NPM
- Bower

Debian install command:

```
apt-get install npm
npm install -g bower
```

Alpine install command:

```
apk add –update npm
npm install -g bower
```

To ensure Bower is installed, run: `bower --version`

#### Dependency Resolution

Checkmarx SCA Resolver uses the `bower-dependency-tree` module to generate a tree of dependencies.

This is an NPM module. In case it is not installed, Checkmarx SCA Resolver installs it using NPM.

**Test**

Ensure installation of the `bower-dependency-tree` module with the following command:

```
npm install -g bower-dependency-tree
```

Then, using the following command, run it to generate the dependency tree inside the project root folder:

```
bower-dependency-tree
```

## Python Support in Checkmarx SCA

### PIP Dependency Resolver

**Manifest files:** `requirements.txt`, `requirements-*.txt`, `requirement.txt`, `requirement-*.txt`, `pyproject.toml`. `setup.cfg`, and `setup.py`

**Package Manager used:** `pip`

#### Installation

Requirements:

- Python
- PIP

Debian install command:

```
apt-get install python python-pip
```

Alpine install command:

```
apk add --update py-pip py3-setuptools
```

To ensure pip is installed, run: `pip -V`

{% hint style="info" icon="pencil" %}
You also need to have virtualenv installed on your machine. You can install virtualenv by running:

`- pip install virtualenv pipdeptree graphviz`OR

\- `pip3 install virtualenv pipdeptree graphviz`

You can verify the installation by running:

`virtualenv --version`
{% endhint %}

#### Dependency Resolution

Checkmarx SCA Resolver ensures the installations of the dependencies in manifest, and uses `pipdeptree` utility to construct the dependency graph

The Resolver creates a temporary virtual environment to install the dependencies, using the command:

```
python -m virtualenv random-name
```

Then, all commands are run in the virtual environment and the `pipdeptree` utility is temporarily installed there. For example, this is an install command on Linux:

```
source random-name/bin/activate && python -m pip install -r requirements.txt
```

**Test**

Checkmarx SCA Resolver requires the dependencies to be installed to extract the full tree. Use the following command:

```
python -m pip install -r requirements.txt
```

The full flow of extracting dependencies is this for Linux

```
python -m virtualenv random-name
source random-name/bin/activate && python -m pip install -r requirements.txt
source random-name/bin/activate && python -m pip install pipdeptree
source random-name/bin/activate && python -m pipdeptree --graph-output dot -e pipdeptree,setuptools,wheel,graphviz
```

- \* on Windows, the command line for virtual environment activation is

`random-name\Scripts\activate`

#### Python 2 vs Python 3

When Python 3 is installed, Checkmarx SCA Resolver may execute the Python commands `python3` and `pip3`.

Checkmarx SCA Resolver first attempts to run `python3`, and if it is not found, it attempts to run `python`.

You can use the `--python-version` flag or `PythonVersion` configuration argument to explicitly specify which Python version to use for the manifest file resolution.

### Poetry Dependency Resolver

**Manifest files:** `pyproject.toml` (required). `poetry.lock`

**Package Manager used:** `Poetry`

#### Installation

Requirements:

- Python

Linux, macOS, Windows (WSL) install command:

```
curl
-sSL https://install.python-poetry.org | python3 –apt-get install python python-pip
```

To ensure Poetry is installed, run:

```
poetry --version
```

#### Dependency Resolution

Checkmarx SCA Resolver ensures the installations of the dependencies in manifest to extract the dependency tree of the project.

**Test**

Use the following command to install dependencies::

```
poetry install
```

Use the following command to extract the dependency tree:

```
poetry show --tree
```

## PHP support in Checkmarx SCA

### Composer Dependency Resolver

**Manifest files:** `composer.json`(required),`composer.lock`

**Package Manager used:** `composer`

#### Installation

Requirements:

- PHP CLI
- composer
- Optional: PHP packages required to install dependencies: php-curl

Debian install command:

```
apt-get install php-cli php-curl composer
```

Alpine install command:

```
apk add –update php-cli php-curl composer
```

To ensure composer is installed, run: `composer --version`

#### Dependency Resolution

Checkmarx SCA Resolver install the dependencies using composer. Composer installs and downloads the dependencies to the local machine.

Afterwards, Composer is used to the detect dependencies

**Test**

Checkmarx SCA Resolver requires the dependencies to be installed to extract the full tree. Use the following command:

```
composer install
composer show --tree --format json
```

**Dev Dependencies**

Dependencies under `require-dev` are considered as dev by Checkmarx SCA.

## Scala Support in Checkmarx SCA

### SBT Dependency Resolver

**Manifest files:** `build.sbt`

**Package Manager used:** `sbt`

#### Installation

Requirements: sbt

To install, visit: [https://www.scala-sbt.org/download.html](https://www.scala-sbt.org/download.html)

To make sure sbt is installed correctly, make sure you can invoke `sbt` inside the project folder by running the following command:

`sbt --script-version`

#### Dependency Resolution

The dependency resolution process involves downloading and building the scala project using the `sbt "compile"` command. Checkmarx SCA Resolver uses the IVY reports generated during the build process to gather the dependency graph.

They can be found under the `target/scala-*/reports/*.xml`, where `scala-*` can be any Scala version used, such as `scala-2.13`.

Those XML files are parsed to generate the tree of dependencies.

**Test**

Run the following command in the project root:

```
sbt "compile"
```

After a successful build, validate that XML files are generated inside the `target/scala-*/reports/*.xml` folders, where `scala-*` can be any Scala version used, such as `scala-2.13`.

## iOS Support in Checkmarx SCA

### SwiftPm Dependency Resolver

**Manifest files:** `Package.swift`

**Package Manager used:** `SwiftPm`

#### Installation

**Debian:**

Use the following procedure to ensure that version 5.3.3 of SwiftPm is installed as well as other necessary tools.

1. Install dependencies: `apt install -y clang libicu-dev libtinfo5 libncurses5 libxml2`

2. Download SwiftPM: `wget https://swift.org/builds/swift-5.3.3-release/ubuntu1804/swift-5.3.3-RELEASE/swift-5.3.3-RELEASE-ubuntu18.04.tar.gz`

3. Extract: `tar -xvzf swift-5.3.3-RELEASE-ubuntu18.04.tar.gz && rm -f swift-5.3.3-RELEASE-ubuntu18.04.tar.gz`

4. Update path environment variable: `export PATH=$PATH:{extractedPath}/usr/bin`, with `{extractedPath}` representing the path where you ran the previous command.

5. To ensure SwiftPm is installed correctly, open a console and run the following command:

   `swift package –-version`

   If the swift package manager is correctly installed, you should receive a message indicating which version is installed on your machine.

#### Dependency Resolution

The dependency resolution process uses SwiftPm’s capabilities to calculate all the dependencies.

If a `Package.swift` file exists, then Checkmarx SCA Resolver uses that to calculate the dependencies. It also checks if the folders declared on the manifest file, `.target` and .`testTarget`, are present on the project.

If there is only a `Package.resolved` file, then the package resolution is done from that file, without executing any commands.

**Test**

Run the following command in the project root:

`swift package show-dependencies`

After a successful build, check if the output contains the dependencies for the project.

### Carthage Dependency Resolver

Manifest files: `Cartfile`(required), `Cartfile.private`, `Cartfile.resolved`

{% hint style="info" icon="pencil" %}
At least one `.private` or `.resolved` file must be included.
{% endhint %}

**Package Manager used:** none

**Requirements:** none

{% hint style="info" %}
Officially, Carthage has a hard dependency on MacOS and XCode. However, Checkmarx SCA uses custom handling and resolution of the manifest files to suppress this requirement. This approach provides a platform independent resolution without any installation prerequisites.
{% endhint %}

#### Installation: no installation needed

#### Dependency Resolution

The dependency resolution process involves downloading the manifest files from GitHub via API.

Checkmarx SCA Resolver uses `Cartfile`, `Cartfile.private` and `Cartfile.resolved` files to gather the info needed to generate the set of dependencies. When the dependencies repository includes the `Cartfile.resolved` files, these are used to avoid resolving the versions again.

**Test:** no testing needed

{% hint style="info" icon="pencil" %}
Since there are no specific requirements for the package manager, there is no need to perform any prerequisite test before using Carthage in Checkmarx SCA.
{% endhint %}

#### Limitations

Carthage resolution uses GitHub API to resolve the packages. GitHub limits unauthenticated users to 300 requests per hour. This may affect the resolution capabilities. To bypass this limitation, on Checkmarx SCA Resolver you can define the `GithubToken` environment variable with up to 4 tokens (separated by “-”) obtained from a GitHub account.

Repositories that are referenced as “git sources” aren’t considered for resolution unless they are hosted on GitHub.

### CocoaPods Dependency Resolver

**Manifest files:** `Podfile`(required), `Podfile.lock`

**Package Manager used:** `CocoaPods`

#### Installation

Debian install command:

```
apt -q install ruby-full -y && apt-get install -y --no-install-recommends ruby ruby-dev make gcc libcurl4 libc6-dev git && gem install cocoapods
```

This command will install the latest available version of CocoaPods, Ruby and other necessary tools.

To ensure that CocoaPods is installed, run `pod --version --allow-root`

#### Dependency Resolution

If `Podfile.lock` does not exist, dependencies from Podfile will be installed and the `Podfile.lock` file will be generated. This file will then be parsed, creating the dependency tree.

**Test**

Run the following command where Podfile is located:

`pod install --allow-root`

After running successfully, check if Podfile.lock file was created.

## Go Support in Checkmarx SCA

### Go Modules Dependency Resolver

**Manifest files:** `go.mod`(required), `go.sum`

**Package Manager used:** `GoModules`

#### Installation

**Debian:**

Use the following procedure to install Go version 1.16.6 and other necessary tools.

1. Download Go: `wget https://golang.org/dl/go1.16.6.linux-amd64.tar.gz`

2. Extract: `tar -xvzf go1.16.6.linux-amd64.tar.gz && rm -f go1.16.6.linux-amd64.tar.gz`

3. Update path environment variable: `export PATH=$PATH:{extractedPath}/go/bin` . {extractedPath} should be replaced by the path where you ran the previous command.

4. To ensure Go is installed correctly, open a console and run the following command: `go version`.

   If Go is correctly installed, you should receive a message indicating which version is installed on your machine.

#### Dependency Resolution

If “go.sum” does not exist, dependencies from “go.mod” will be installed and “go.sum” file will be generated. Then a dependency graph will be generated that is used to build the dependency tree.

**Test**

1. Run the following command where go.mod is located: `go mod download`
2. After running successfully, check if go.sum file is created. Then run the following command: `go mod graph`
3. After a successful build, check if the output contains the dependencies for the project.

## Container Scan in Checkmarx SCA

**Manifest files:** `Dockerfile*`

**Package Manager used:** none

### Installation

No Installation needed

### Dependency Resolution

The dependency resolution process involves downloading the manifest files from Docker Hub via API.

Checkmarx SCA Resolver uses **Dockerfile\*** files information to collect and generate the set of dependencies based on docker layers.

**Test**

Since there are no package manager specific requirements, there is no need to perform any prerequisite test before using container scans in Checkmarx SCA.

#### Limitations

**Authentication**

Docker Hub API has restrictions for anonymous requests. We offer the possibility to authenticate your requests through these environment variables:

- DOCKERHUBUSERNAME
- DOCKERHUBTOKEN

{% hint style="info" icon="pencil" %}
Authenticating with Docker Hub also enables Resolver to access your private repositories.
{% endhint %}

**Build Arguments**

Some projects may contain build arguments that are required for layer resolution.

Checkmarx SCA Resolver supports the use of a `.env_cxsca-container-build-args` file, which can be added to repository code to provide custom build-arguments to Dockerfile `FROM` instructions. We recommend using this file when the docker is present and the build process requires arguments in order to enhance the docker layer resolution and improve results.

For more info about using custom build arguments, see [Container Scans](container-scans.md).

## RubyGems Dependency Resolver

Manifest files: `gemfile` (required), `gemfile.lock`

**Package Manager** **used**: RubyGems

### Installation

Debian install command:

```
apt -q install ruby-full -y && gem install bundler
```

This command will install the latest available version of Ruby, RubyGems and Bundler.

To ensure that RubyGems is installed, run `gem --version`

To ensure that Bundler is installed, run `bundler --version`

### Dependency Resolution

If `gemfile.lock` does not exist, dependencies from `gemfile` will be installed and the `gemfile.lock` file will be generated. This file will then be parsed, creating the dependency tree.

**Test**

Run the following command where gemfile is located:

```
bundler
```

After running successfully, check if `gemfile.lock` file was created.

## Unity Package Manager Dependency Resolver

**Manifest files:** `manifest.json`(required), `package.json` (required)

**Package Manager used:** none

**Requirements:** none

{% hint style="info" %}
Unity’s SDK, although cross platform, has a hard dependency on .NET framework, which requires Mono to be supported on all the supported platforms. Checkmarx uses custom handling and resolution of the manifest files in order to suppress this requirement. This approach provides platform agnostic resolution without any installation prerequisites.
{% endhint %}

### Installation

No Installation needed

### Dependency Resolution

The dependency resolution process involves two elements, determining the package version (which is found in the `manifest.json`) and determining which Unity version is in use (which is found in the `package.json`).

**Test:** none

{% hint style="info" icon="pencil" %}
Since there are no specific requirements for the package manager, there is no need to perform a prerequisite test before using Unity in Checkmarx SCA.
{% endhint %}

### Limitations

Since Checkmarx SCA Resolver doesn’t use the Unity Package Manager, it is possible that some transitive dependencies may be left out if the packages are not included in the scan.

## Perl Support in Checkmarx SCA

### Cpan Dependency Resolver

**Manifest files:** `cpanfile` (required), `cpanfile.snapshot` (optional)

**Package Manager used:** `cpan` and `carton`

#### Installation

Debian install command:

```
apt -q install perl -y && cpan install Carton
```

This command will install the latest available version of Perl, Cpan and Carton.

To ensure that Cpan is installed, run `cpan --version`

To ensure that Carton is installed, run `carton --version`

#### Dependency Resolution

If `cpanfile.snapshot` does not exist, dependencies from `cpanfile` will be installed and the `cpanfile.snapshot` file will be generated. This file will then be processed to create the dependencies tree.

**Test:**

Run the following command where cpanfile is located:

```
carton
```

After running successfully, check if `cpanfile.snapshot` file was created.

#### Limitations

Many Cpan packages must be compiled as part of the resolution process. The environment where the scan is performed must be able to compile these dependencies. Otherwise, the resolution will fail.

Cpan does not support development and testing packages. This is done to improve scan speeds.

## Pub Support in Checkmarx SCA

### Pub Dependency Resolver

**Manifest files:** `pubspec.lock` (required)

**Package Manager used:** none

**Requirements:** none

#### Installation: no installation needed

#### Dependency Resolution

The dependency resolution process involves downloading the manifest files.

Checkmarx SCA Resolver uses the `pubspec.lock` file to gather the info needed to generate the set of dependencies.

**Test:** no testing needed

#### Limitations

- We only identify direct dependencies in Pub, not transitive dependecies.
- We only identify Malicious Packages in Pub, not packages with vulnerabilities.
