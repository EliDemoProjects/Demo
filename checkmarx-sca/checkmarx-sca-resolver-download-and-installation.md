# Checkmarx SCA Resolver Download and Installation

{% hint style="warning" %}
As of May 3, 2026, the SCA Resolver MacOS Installer binary for version 2.13.3 has been re-signed. The checksum has been updated accordingly to reflect the new artifact.

This change affects all previous SCA Resolver MacOS Installer versions, which are now revoked. Users should update to version 2.13.3.
{% endhint %}

## Download Latest Version of Resolver

Use the relevant link to download the latest version of SCA Resolver.

{% hint style="info" icon="pencil" %}
The latest version of SCA Resolver is currently **2.16.2**.
{% endhint %}

- [Windows](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-win64.zip)
- [Debian](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-linux64.tar.gz)
- [Alpine Linux](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-musl64.tar.gz)
- [MacOS](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-macos64.tar.gz)
- [MacOS Installer](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-macos64.pkg)

Use the relevant link to download the checksum for the latest version of Resolver.

- [Windows sha256sum](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-win64.zip.sha256sum)
- [Debian sha256sum](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-linux64.tar.gz.sha256sum)
- [Alpine Linux sha256sum](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-musl64.tar.gz.sha256sum)
- [MacOS sha256sum](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-macos64.tar.gz.sha256sum)
- [MacOS Installer sha256sum](https://sca-downloads.s3.amazonaws.com/cli/latest/ScaResolver-macos64.pkg.sha256sum)

{% hint style="info" icon="pencil" %}
Links to download older versions of Resolver are available at [Checkmarx SCA Resolver Changelog](checkmarx-sca-resolver-changelog.md).
{% endhint %}

## Installation

{% hint style="info" icon="pencil" %}
The following procedure is relevant when you download Resolver as a zip archive. When you run the MacOS Installer you just need to follow the prompts to run the installer. The installer saves the Configuration.yml file to `/Library/ScaResolver/{version}/Configuration.yml`.
{% endhint %}

**To download and Install Checkmarx SCA Resolver:**

1. Use the appropriate link (shown above) to download the correct version of Checkmarx SCA Resolver for your OS.

2. Extract the compressed archive file.

   {% include ".gitbook/includes/note-215672c4.md" %}

3. Install all required resolution utilities, see [Installing Supported Package Managers for Resolver](installing-supported-package-managers-for-resolver.md)

**Installation Notes:**

- On **Ubuntu**, run the command as root before running, or if you encounter any startup issues.

```
apt update
apt install ca-certificates libgssapi-krb5-2
```

- On **Alpine Linux**, run the command as root before running, or if you encounter any startup issues.

```
apk add libstdc++ 
apk add glib
apk add krb5 pcre
apk add bash
```
