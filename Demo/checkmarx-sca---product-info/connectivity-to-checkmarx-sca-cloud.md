# Connectivity to Checkmarx SCA Cloud

In order to access Checkmarx SCA Cloud, you will need to have access to the relevant URLs, shown below. You may need to add these to your firewall allowlists or proxies.

{% hint style="info" icon="pencil" %}
This is necessary for accessing the Checkmarx SCA web portal as well as for sending request to Checkmarx SCA Cloud using APIs, Checkmarx SCA Resolver, Checkmarx SCA Agent or CI/CD plugins.
{% endhint %}

## Checkmarx SCA Endpoints

{% hint style="info" icon="pencil" %}
We recommend adding the Checkmarx services **URLs** to your firewall rules **and not the IP addresses**. Since the IPs of Checkmarx service endpoints are not necessarily static, adding them directly to the firewall might not be effective.
{% endhint %}

The URLs are accessed by HTTPS protocol on port 443.

The Checkmarx SCA services are hosted in AWS, and have a dynamic IP address range.

Specific plugins have support for HTTP proxy.

For more information, see [SAST/SCA Integrations](/document/preview/7297#UUID-09af4cb8-95d4-d86a-48f3-5e0e5176366b)

### US Environment

Plugins that use the Checkmarx SCA cloud for scanning require access to the following URLs:

- Checkmarx SCA API - [https://api-sca.checkmarx.net](https://api-sca.checkmarx.net)
- Access Control URL - [https://platform.checkmarx.net](https://platform.checkmarx.net)
- Checkmarx SCA Web Application - [https://sca.checkmarx.net](https://sca.checkmarx.net)
- Code upload endpoint - [https://uploads.sca.checkmarx.net](https://uploads.sca.checkmarx.net/)

### EU Environment

Plugins that use the Checkmarx SCA cloud for scanning require access to the following URLs:

- Checkmarx SCA API - [https://eu.api-sca.checkmarx.net](https://eu.api-sca.checkmarx.net)
- Access Control URL - [https://eu.platform.checkmarx.net](https://eu.platform.checkmarx.net.)
- Checkmarx SCA Web Application - [https://eu.sca.checkmarx.net](https://eu.sca.checkmarx.net)
- Code upload endpoint - [https://uploads.eu.sca.checkmarx.net](https://uploads.eu.sca.checkmarx.net/)

{% hint style="info" %}
The minimal supported plugin versions for working with the EU environment are as follows:

- CxConsole/CLI - version 2020.4.4
- TeamCity - version 2020.3.8
- Jenkins - version 2020.4.3
{% endhint %}

### Report Downloads

In order to download scan reports, you will need to add the following S3 domain pattern to your allowlist: `*.s3.us-east-1.amazonaws.com`

This is relevant for both US and EU environments.

{% hint style="info" %}
If access to these downloads is blocked, this may cause some plugin workflows to fail.
{% endhint %}
