# Files Used for Manifest Resolution

The following is a list of the files (manifest and other types) used by Checkmarx SCA for resolving the manifest files in order to discover the dependency tree. It is important to ensure that these files are included in the project that you submit for the Checkmarx SCA scan.

{% hint style="info" icon="pencil" %}
The default behavior is that the content of these files is sent to the Checkmarx SCA Cloud for analysis. If you are running the scan using Checkmarx SCA Resolver, you have the option to prevent the files from being uploaded by using the `--no-upload-manifest` flag.
{% endhint %}

- Maven

  - pom.xml
  - settings.xml
  - build.properties
  - versions.properties
- Gradle

  - \*.gradle
  - gradle-wrapper.properties
  - build.gradle.kts
  - gradle.properties
  - gradlew
  - gradlew.bat
  - gradle-wrapper.jar
- Ivy

  - ivy.xml
  - build.xml

  SBT

  - build.sbt
  - plugins.sbt
- NPM

  - package.json
  - package-lock.json
  - lerna.json
  - .npmrc
  - npm-shrinkwrap.json
- Yarn

  - yarn.lock
  - .yarnrc
  - package.json
- Bower

  - bower.json
- NuGet

  - \*.csproj
  - nuget.config
  - packages.config
  - project.assets.json
  - packages.lock.json
- PIP

  - requirements.txt
  - requirements-\*.txt
  - requirement.txt
  - requirement-\*.txt
  - packages.txt
- Poetry

  - pyproject.toml
  - poetry.lock
- Pipenv

  - pipfile
  - pipfile.lock
- Composer

  - composer.json
  - composer.lock
- SwiftPm

  - Package.swift
  - Package.lock
- Carthage

  - Cartfile
  - Cartfile.private
  - Cartfile.resolved
- RubyGems

  - gemfile
- Go Modules

  - go.mod
  - go.sum
- Cpan

  - cpanfile
  - cpanfile.snapshot
- Pub

  - pubspec.lock
- General

  - VERSION

All files sent to Checkmarx SCA (either in manifest only or in regular scans) are saved for a period of 24 hours for scan analysis purposes.

For long term purposes (autoscanning and debugging customer complaints) only the list of manifests that are already listed per package manager in the documentation are saved.
