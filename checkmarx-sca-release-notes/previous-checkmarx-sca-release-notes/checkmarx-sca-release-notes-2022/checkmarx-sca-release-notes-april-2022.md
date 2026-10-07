# Checkmarx SCA Release Notes April 2022

We are excited to announce important improvements in our Checkmarx SCA web application…

## Checkmarx SCA Resolver Updates

We have released several new versions of Resolver with a wide range of improvements and bug fixes. The most recent release is 1.8.9.

The following are some highlights from the recent releases:

* Container Scan - Added support for container images hosted on Microsoft Container Registry (MCR) (e.g., mcr.microsoft.com/dotnet/sdk:latest). For more information, see [Container Scans](../../../checkmarx-sca-product-info/container-scans.md).
* Exploitable Path - you can now use the "--proxies" flag with Exploitable Path scans in order to send the traffic through a proxy.
* Added additional Debug logs for commands that are taking too long to execute.

Download the latest version of Resolver [here](../../../checkmarx-sca-resolver/checkmarx-sca-resolver-download-and-installation/).

## Improvements and Bug Fixes

| Status | Item            | Description                                                                               |
| ------ | --------------- | ----------------------------------------------------------------------------------------- |
| UPDATE | Gradle 6.9      | Added support for Gradle version 6.9.                                                     |
| UPDATE | Support for MCR | Added support for scanning container images hosted on Microsoft Container Registry (MCR). |
