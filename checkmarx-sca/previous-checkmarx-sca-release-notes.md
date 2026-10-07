# Previous Checkmarx SCA Release Notes

## August 26, 2021

NEW - AppSec Knowledge Center - Our new AppSec Knowledge Center can be accessed via the Checkmarx SCA web portal. The Knowledge Center enables you to search our extensive database for information about specific package versions and vulnerabilities. This enables you to check the open source packages that you want to use in your project in advance to make sure that you won’t be introducing security risks into the project.

The database includes CVEs and also vulnerabilities discovered by the Checkmarx Vulnerability Research Team (“Cx” vulnerabilities).

IMPROVED - The Exploitable Path feature (which checks whether the vulnerable open source packages are called from your proprietary code and whether the vulnerable methods are actually used by your code) now supports JavaScript projects (in addition to existing support for Java and Python). See [Exploitable Path](exploitable-path.md).

IMPROVED - Improved ability to identify packages based on file fingerprints (hashes).

NEW VERSIONS - We have released several new versions of Resolver with a wide range of improvements and bug fixes. The most recent release is 1.5.42.

The following are some highlights from the recent releases:

- Added support for iOS projects using SwiftPM, Carthage and CocoaPods package managers.
- Added support for providing a proxy to be used for requests via HTTP and HTTPS.

For additional details, see [Checkmarx SCA Resolver Changelog](checkmarx-sca-resolver-changelog.md).

## May 10, 2021

NEW - Exporting Risk Reports - You can now export Risk Reports, showing comprehensive info about the risks identified in each of your Checkmarx SCA Projects. The Risk Report shows the results of a specific scan of a Project, including both overall results as well as detailed info about the risks that were identified. You can export a Risk Report via the Checkmarx SCA web portal by navigating to the Scan Results page for the desired scan and clicking on the Export button at the top of the page. You can specify the desired file format (pdf, xml, json, or csv) as well as which sections to include in the report (**Packages**, **Vulnerabilities**, **Licenses**, or **All**). For more info, see [Scan Reports](sca-scan-reports.md).

You can also generate Risk Reports via Checkmarx SCA Resolver, see [Risk Report Arguments](checkmarx-sca-resolver-configuration-arguments.md).

NEW – The Bamboo plugin now supports Checkmarx SCA.

IMPROVED – Complex policy conditions - You can now configure complex conditions for security policies. You can create rules that include multiple conditions relating to the packages, vulnerabilities and licenses. Only when all of the conditions are met is the rule considered to be violated.

NEW VERSION - CLI version 1.1.5 (new numbering convention) was released.

- The new version includes the following new features and improvements.

  - The Exploitable Path feature for identifying attack vectors has been added for Checkmarx SCA scans.
  - The ‘CheckPolicy’ option now enforces Checkmarx SCA policies to break builds, as per policy action configuration.
  - The option to include source code with Checkmarx SCA scans has been added.
  - Private registries and environment variables have been added for Checkmarx SCA scans.
  - Project creation and Team assignment capabilities have been added for Checkmarx SCA scans.

NEW VERSION - Checkmarx SCA Resolver version 1.5.7 was released. Download links are available [here](checkmarx-sca-resolver-changelog.md).

- The new version of Checkmarx SCA Resolver, includes the following improvements:

  - Checkmarx SCA Resolver now uses the "--all" flag to force npm to list all dependencies (i.e., revert to version 6 results)
  - For Yarn, general improvements
  - Added support for Ivy package manager

## April 22, 2021

NEW VERSION - Checkmarx SCA Resolver version 1.5.4 was released. Download links are available [here](checkmarx-sca-resolver-changelog.md).

The new version of Checkmarx SCA Resolver, includes the following new features:

- There is now an option to run Checkmarx SCA Resolver in “Offline” mode. When a scan is run in “Offline” mode, it can then be run in “Upload” mode at a later time to execute the scan.
- When you run a scan using Checkmarx SCA Resolver, you can now set flags to export a comprehensive Risk Report of the scan results in json, xml, csv, or pdf format.

As well as the following improvements and bug fixes:

- Improved result parser for Bower
- Can now handle the exception when trying to extract compressed files that require a password
- Fixed bug causing scan to get stuck when Maven was not available
- Pip now resolves Python requirement files which contain an '-r' flag
- Fixed log name to include the local timezone of the machine (as opposed to showing UTC)

## March 25, 2021

NEW VERSION - Checkmarx SCA Resolver version 1.4.41 was released. Download links are available [here](checkmarx-sca-resolver-changelog.md).

The new version of Checkmarx SCA Resolver, includes the following improvements:

- Added ability to pass custom parameters Maven
- Fixed password leak to log
- Fixed argument parsing while replacing '\_' with '-'
- For npm, transitives of dev dependencies are now tagged as dev

## March 12, 2021

NEW VERSION - Checkmarx SCA Resolver version 1.4.34 was released. Download links are available [here](checkmarx-sca-resolver-changelog.md).

The new version of Checkmarx SCA Resolver includes the following improvements:

- Added a flag to ignore submodules in Gradle
- For Gradle, we now detect settings.gradle.kts files
- For Nuget, we now ignore project references inside of .csproj files
- For PIP, we now detect files with the following file names: “requirement-\*.txt” and “requirements-\*.txt”
- For Composer, the vendor folder is now ignored by the scanner
- Logs are now saved in ScaResolver path by project name unless a fully qualified path is configured in the "LogsDirectory" configuration

## March 7, 2021

IMPROVED - Enhanced Exploitable Path functionality

NEW VERSION - Checkmarx SCA Resolver version 1.4.28 was released. Download links are available [here](checkmarx-sca-resolver-changelog.md).

The new version of Checkmarx SCA Resolver includes the following improvements:

- Added ability to pass custom parameters to Bower, Composer, Lerna, NPM, Nuget, Pip, SBT, and Yarn project scans

- Added ability to disable upload of manifest files

- SCA scans now extract compressed files of type .zip, .war, .ear. Also, the user can add a flag to specify custom file types for extraction.

- For Exploitable Path scans, the config file key "OldResultsThresholdMinutes" was added, enabling users to customize the time period for which SAST results are checked. By default, this is now set as two weeks.

- Changed "Invalid SAST settings" to warning level instead of error

- Improved Gradle dev-dependencies detection

- Fixed NPM package-lock.json display error

- Fixed errors causing scan failures in Gradle, Bower and Maven

- For Exploitable Path scans, users now have the option of providing the SAST Project name instead of the Project ID

- Added Gradle dependency parser customizations:

  - Exclude scopes - include all scopes other than the specified exclusions
  - Include scopes - include only the specified scopes
  - Dev scopes - mark specific scopes to be analyzed as dev dependencies

## February 1, 2021

NEW - Added the ability to configure a Policy to cause builds to break whenever the specified threshold of security threats is detected, see Policy Management.

FIXED - Fixed agent authentication issue for working with CxServer version 9.3

FIXED - Fixed a bug in the upgrade recommendation logic

NEW VERSION - Checkmarx SCA Resolver version 1.4.14 was released. Download links are available [here](checkmarx-sca-resolver-changelog.md). The new version, includes the following improvements:

- Added support of the “Exploitable Path” feature for SAST users. This enables you to identify whether or not there is an exploitable path from your source code to a specific open source vulnerability, see [Exploitable Path](exploitable-path.md).
- Added support for Checkmarx SCA “Policies”. This enables you to cause builds to break whenever the specified threshold of security threats is detected, see [Policy Management](policy-management.md).
- Added the ability to pass custom parameters to Gradle project scans
- Improved Gradle robustness in multi-module projects and Gradle wrapper download
- Fixed BOM issue in composer.json file

## January 17, 2021

NEW - Policy Management is now GA!

NEW - SCA Agent beta is now available in GitHub and DockerHub.

NEW - Support for .Net 5.0.

IMPROVED - Exploitable Path enhancements.

IMPROVED - Checkmarx SCA Resolver CLI allows you to ignore dev dependencies. For more information, see [Checkmarx SCA Resolver Configuration.](https://checkmarx.atlassian.net/wiki/spaces/CD/pages/1976074542/CxSCA+Resolver+Configuration)

IMPROVED - Gradle enhancements: Improved robustness; Support for identification of Gradle dev dependencies.

## November 12, 2020

IMPROVED - Checkmarx SCA UI improvements

FIXED - Various bug fixes

## October 20, 2020

NEW - Added support for specifying the Python version (2 or 3) in the configuration.

NEW - Dependency resolution now supports Nuget packages.config manifest files.

IMPROVED - Checkmarx SCA Resolver CLI Version 1.2.30 released. For more information, see [Checkmarx SCA Resolver Download.](checkmarx-sca-resolver-download-and-installation.md)

IMPROVED - Improved dependency resolution robustness and fixed several issues.

## September 30, 2020

NEW - EU Support – Checkmarx SCA is now deployed in a EU datacenter, in addition to the existing NA one.

NEW - Users can now filter their projects based on assigned teams.

NEW - TeamCity plugin is now available.

IMPROVED - Support improved for Dependency Resolution, in addition to some bug fixes.

## August 18, 2020

NEW - Support for Java multi-module projects

NEW - Added Account Settings page presenting: Customer license details & Additional account level configurations

NEW - Added the option (for Checkmarx SCA admins) for blocking any source code upload to the Checkmarx SCA cloud (including UI and GitHub scans)

NEW - Plugins now only send the manifest files and fingerprints to the Checkmarx SCA cloud. The following plugins were released to Technical Support only (not yet GA): Jenkins, CLI, & ADO. For more details, please reach out via the CxPM-SCA mailing list.

IMPROVED - Robust dependency resolution coverage for the following package managers: Maven (Java) & Gradle (Java)

IMPROVED - Reporting page performance improved for large scale deployments.

## July 21, 2020

NEW - When creating a GitHub project in the Checkmarx SCA cloud, the user can select which repository branch the project will be based.

NEW - The Scan Summary tab, added to the Risk Report page, shows the scan progress timeline and the resolving status of the configuration and manifest files.

NEW - Added support for resolving NPM projects managed with Lerna.

NEW - Added support for resolving NPM projects managed with Yarn Workspaces.

NEW - Projects can now be deleted, either one at a time or in bulk.

IMPROVED - The Risk Report page now displays Legal Risk in a filterable column.

FIXED - Fixed an issue in Gradle multi-module projects, which resulted in failure to parse the settings file.

## June 16, 2020

NEW - The Reporting page displays one table containing all the vulnerabilities in all the organization’s projects. The information in the table can be searched, filtered, and exported.

IMPROVED - NPM dependency resolution shows partial results, even if some of the dependencies are missing.

IMPROVED - Any public Git URL, which can be cloned, can be scanned from the Checkmarx SCA Web Application when scanning a General Project.

IMPROVED - A project can be assigned to “All Users,” making it visible to everyone regardless of their team associations.

FIXED - Fixed an issue that prevented filtering vulnerabilities by the Package column from working as expected, if the “Outdated” version option was selected.

## June 7, 2020

NEW - The new Jenkins plugin supports the Scan results Dashboard. The plugin is available at [https://www.checkmarx.com/plugins/](https://www.checkmarx.com/plugins/) . For more information, see [Checkmarx Plugin for Jenkins.](https://checkmarx.atlassian.net/wiki/spaces/CD/pages/1731168437/Checkmarx+Plugin+for+Jenkins)

NEW - Each project can be assigned to one or more teams, and only the members of those teams can view and manage the project.

NEW - The package information on the Reporting page can be sorted and filtered by vulnerability risk levels.

NEW - The package information on the Reporting page can be exported as a CSV file.

FIXED - Child packages of unresolved “Dev” packages are now also marked as “Dev”.

## June 2, 2020

NEW - CLI and Jenkins plugins support Checkmarx SCA scanning without any limit on the package size.

NEW - Support for resolving dependencies extended to Gradle Wrapper and multi-module Gradle projects.

IMPROVED - Exported risk report (via Export button) includes more information: scan time, project name, vulnerable package name, and version number. Also removed some possible duplicate entries.

IMPROVED - The UI for creating GitHub projects now displays the account name and the selected projects.

FIXED - Fixed bug that interfered with sorting projects by date when “never scanned” projects were included in the list.

FIXED - Fixed bug causing failures in Scala dependency resolution (SBT).

FIXED - Fixed bug causing .NET manifest files, which had no external dependencies, to be reported as failed.

## May 17, 2020

IMPROVED Any private GitHub repository can be searched when importing a project from a private account

IMPROVED Package view enhanced

## May 13, 2020

IMPROVED Python dependency resolver enhanced to increase accuracy and remove false positives

IMPROVED The error messages issued when a Git repository scan fails are now more informative

IMPROVED Account name is displayed together with the username

IMPROVED In package view, clicking on the vulnerabilities will open a detailed list of vulnerabilities

FIXED Fixed bug preventing the manifest file from being available after a risk recalculation

FIXED Fixed error causing, in rare situations, a vulnerability to be counted twice

## April 27, 2020

NEW Vulnerability tab: including vulnerable package path, references, and CVSS information

NEW Vulnerability package path shows the other vulnerable packages in the path and their risk levels

NEW Reporting page available displaying all packages in all the organization’s projects, providing a company-wide inventory of packages

IMPROVED Risk report page supports multiple tabs for packages and vulnerabilities

IMPROVED Last Scanned/Date column can be toggled to show relative time when last scanned or full date

IMPROVED Added support to Gradle-Kotlin projects with specific memory requirements

FIXED Fixed situation where the search filter disappears while the table remains filtered

FIXED Fixed bug preventing, in some cases, some NPM dependencies from being detected

FIXED Fixed bug causing some YARN scans to fail

FIXED Fixed bug causing some direct Python packages to be displayed as transient packages

## April 13, 2020

NEW Checkmarx SCA is now open to the Internet and can be accessed from anywhere

NEW User can extract the Scan ID from the meta data section on the Project and Scan Results pages, and include it when submitting support tickets

NEW Pull Request description includes upgrade content and CVE’s fixed in the upgrade

NEW API to query risk data by package name

IMPROVED Number of table items displayed is now configurable

IMPROVED Scan History page now displays the user who performed the scan

FIXED Cannot create project with duplicate name

FIXED Graph scales are dynamic, and show whole numbers

FIXED Fixed security issue on Git clone command

## March 16, 2020

NEW Added permissions and default roles to scan, manage projects, and view results

NEW Remediation: opening pull requests with fixes available for GitHub projects

NEW “Recalculate” button that recalculates results for existing projects on demand, without re-scanning the projects

NEW Jenkins Plugin and Cx Console plugin support Checkmarx SCA! (In beta mode, these plugins do not perform dependency resolution on-prem, but upload the zip file with code to the cloud

IMPROVED SCA CLI (internal) moved to .Net Core 3 and available as single executable

IMPROVED Scan warning issued when a private Artifactory is not accessible

IMPROVED UI - New create project screen

IMPROVED UI - New navigation pane

FIXED Token timeout alerts fixed

FIXED Ignoring a vulnerability no longer refreshes the page
