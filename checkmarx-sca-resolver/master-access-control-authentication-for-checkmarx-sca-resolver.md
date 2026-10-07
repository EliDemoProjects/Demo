# Master Access Control Authentication for Checkmarx SCA Resolver

In order to run Checkmarx SCA Resolver in Online or Upload mode, you need to provide authentication credentials. For the standard authentication method, this is done by providing your Checkmarx SCA username and password. Alternatively, if you have integrated your Checkmarx SCA account with Master Access Control (see [Using Master Access Control (Replica Mode)](../checkmarx-sca-user-guide/user-management-and-access-control/using-master-access-control-replica-mode.md)), you can authenticate for Checkmarx SCA Resolver via Master Access Control.

In order to use Master Access Control authentication, you need to provide the name of your Master Access Control instance in the Resolver execution command. When the command is run, an automated browser will be downloaded and opened. It will prompt you to authenticate with your Master Access control username and password. Once the authentication has been completed you can resume using Checkmarx SCA Resolver from the Command interface.

{% hint style="info" icon="pencil" %}
Because the browser interaction is a necessary part of the Master Access Control authentication process, we don’t recommend using SAML authentication in pipelines.
{% endhint %}

## Run Command for Master Access Control Authentication

In order to use Master Access Control authentication for Checkmarx SCA Resolver, in the run command for Online and Upload modes, use the following arguments:

`-a | --account: your Checkmarx SCA account name`

`--sso-provider: the name of your Master Access Control instance`

{% hint style="info" icon="pencil" %}
The following arguments, which are used for standard authentication, are not used with Master Access Control authentication:

`-u : your username`

`-p : your password`
{% endhint %}

The following example shows a run command in Online mode using SAML authentication:

{% tabs %}
{% tab title="Linux/MacOS" %}
```
./ScaResolver -s /Users/DemoUser/MyApp -n MyApp -a CheckmarxDemo --sso-provider DemoMasterAccessControl
```
{% endtab %}

{% tab title="Windows" %}
```
./ScaResolver.exe -s C:\Users\DemoUser\MyApp -n MyApp -a CheckmarxDemo --sso-provider DemoMasterAccessControlokta
```
{% endtab %}
{% endtabs %}
