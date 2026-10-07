# Result Status Codes for Source Resolver

The Source Resolver returns a status code for each manifest file that was scanned. This code indicates whether or not the resolution was successful and gives information about the execution and outcome of the scan.

## Success Status Codes

### FullResults

The manifest file was resolved successfully and the resolved dependencies were returned in the results.

### PartialResults

The initial resolution process failed for this manifest file for one of the reasons described below under “Failed status” (e.g., repository not accessible, invalid file format etc.). However, the package manager’s fallback resolution process was run successfully and yielded partial results for resolved dependencies.

{% hint style="info" icon="pencil" %}
Fallback resolution is only done for scans run in the SCA Cloud, not for scans run using SCA Resolver.
{% endhint %}

### ShouldNotBeResolved

Checkmarx SCA determined that this file is used to support the resolution process but is not intended to be resolved itself. Therefore, no dependencies were returned for this file.

### UserExcluded

This manifest file was included in the list of files or folders that were excluded from scanning for this project. Therefore, it wasn’t resolved and no dependencies were returned for this file.

## Failed Status Codes

### PackageManagerNotAvailable

Checkmarx SCA wasn’t able to resolve this manifest file because the required package manager is not installed or is not available in the scanning environment. Check the package manager installation page to determine what package managers and tools are needed for resolving this manifest file.

### PrerequisiteFailed

Checkmarx SCA wasn’t able to resolve this manifest file because you are missing some of the prerequisites that are needed for running this package manager in SCA. Check the package manager installation page to determine which prerequisites you need to set up.

### FileNotFound

Resolution of this manifest file failed because one or more of the files needed for resolving this manifest file were not found or were not accessible.

### InvalidFile

Resolution of this manifest file failed because one or more of the files needed for resolving this manifest file were not formatted as required (e.g., a json file that doesn’t conform with json rules).

### CommandExecutionFailed

Resolution of this manifest file failed because one or more of the commands used by the package manager failed.

### PrivateArtifactoryInaccessible

Resolution of this manifest file failed because Checkmarx SCA didn’t have access to some of the dependencies that are hosted in a private artifactory. You can fix this problem either by making sure that all dependencies are available on public artifactories, or by using the SCA Resolver to run the scan in a local environment that has access to your private artifactories.

### HttpRequestFailed

Resolution of this manifest file failed because one or more of the http requests used for the resolution failed.

### FailedToResolve

Resolution of this manifest file failed for some unknown reason. Contact support to try to identify the cause of the problem.
