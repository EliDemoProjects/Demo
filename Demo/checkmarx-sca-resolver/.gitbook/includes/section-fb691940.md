#### Running a Container Scan on your Dockerfile

- Run an SCA Resolver scan, using the `--scan-containers` flag in the scan command.

{% hint style="info" icon="pencil" %}
When running a container scan in Offline mode, you must use the `--containers-result-path` flag to specify the container results output location. Then, when running Upload, you need to use the same flag to refer to the file location.
{% endhint %}

**Example of scanning the project's Dockerfile:**

The following example shows a command to run a container scan on the Dockerfile in your project.

{% tabs %}
{% tab title="Linux/MacOS" %}
```
./ScaResolver -s /Users/DemoUser/DemoProject -n DemoImageScan -a Checkmarx -u jack -p 'demo123!' --scan-containers
```
{% endtab %}
{% tab title="Windows" %}
```
./ScaResolver.exe -s C:\Users\DemoUser\DemoProject -n DemoImageScan -a Checkmarx -u jack -p "demo123!" --scan-containers
```
{% endtab %}
{% endtabs %}
