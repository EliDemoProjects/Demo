# Generate a ZAP Configuration File

In this section, we explain how a ZAP configuration file can be generated.

1. Install ZAP on your local machine. Download ZAP from the following link: [https://www.zaproxy.org/download/](https://www.zaproxy.org/download/)
2. Open ZAP.
3.  In the hierarchy under Contexts, double-click Default Context.

    <div align="left"><figure><img src="../.gitbook/assets/img-f1773731ab6dd0ec7a499bd3ef6fb055.png" alt=""><figcaption></figcaption></figure></div>
4.  Define the URL to do the test. Select the Include in Context option, click Add, enter the URL, and click Add.

    <div align="left"><figure><img src="../.gitbook/assets/img-85c4da43b1af31c21353fe3314299285.png" alt=""><figcaption></figcaption></figure></div>
5.  Select Authentication and choose the method matching your target's login flow. The supported options are HTTP/NTLM Authentication and Form-based Authentication. The example below shows Form-based Authentication; for HTTP/NTLM, ZAP prompts for the realm, hostname, and credentials instead of a login form URL.

    <div align="left"><figure><img src="../.gitbook/assets/img-6cecd3b775c8b8c5b5318ed1f02b31f1.png" alt=""><figcaption></figcaption></figure></div>
6.  Create the user(s) you want to use on the scans.

    <div align="left"><figure><img src="../.gitbook/assets/img-b4aaac25650de52a97ef82c42daae2e2.png" alt=""><figcaption></figcaption></figure></div>
7.  Click the + button at the bottom of the window and then click Automation.

    <div align="left"><figure><img src="../.gitbook/assets/img-67b0100732e92ed0367caea0fe73588c.png" alt=""><figcaption></figcaption></figure></div>
8.  Click the New Plan button.

    <div align="left"><figure><img src="../.gitbook/assets/img-be6169405535fdfd4aa5ae1640f7c65d.png" alt=""><figcaption></figcaption></figure></div>
9.  Select one of the following profiles:

    Each job performs a specific task in the scan - for example, spider and spiderAjax crawl the target to discover URLs, openapi tests endpoints from an OpenAPI/Swagger spec, and report generates the results report. For the full list of supported jobs and what each configures, see [Jobs Supported](configuration-file-structure/jobs-supported/).

    *   For a web scan, select the Full Scan profile.

        <div align="left"><figure><img src="../.gitbook/assets/img-0b30e97ed78687973fa157bbc4d706e8.png" alt=""><figcaption></figcaption></figure></div>
    *   For an API scan select the OpenAPI profile.

        <div align="left"><figure><img src="../.gitbook/assets/img-3ac07cf6a133bceb57a364d14ecca617.png" alt=""><figcaption></figcaption></figure></div>

    <div data-gb-custom-block data-tag="hint" data-style="info" data-icon="pencil" class="hint hint-info"><p>The type of jobs presented will depend on the add-ons installed. If some of the intended jobs don't appear go to the manage add-on option and install them.</p></div>

    <div align="left"><figure><img src="../.gitbook/assets/img-6153197bf1eddbc6b00f9e6d9516bf99.png" alt=""><figcaption></figcaption></figure></div>
10. Click Save.
11. Double-click on each job if you want to change the context associate or in some cases (Spider Ajax for example) to determine the user to use in the job.

    <div align="left"><figure><img src="../.gitbook/assets/img-0936243b1a69797b7889ccf883b90dfc.png" alt=""><figcaption></figcaption></figure></div>

    <div align="left"><figure><img src="../.gitbook/assets/img-597f37febed73632935d7917daaebd3e.png" alt=""><figcaption></figcaption></figure></div>

    <div align="left"><figure><img src="../.gitbook/assets/img-f3a5b9eb9bd5287f27ed492d79f2a97b.png" alt=""><figcaption></figcaption></figure></div>
12. To save the plan, click the Save As button and then choose the folder.

    <div align="left"><figure><img src="../.gitbook/assets/img-2c3207a4695b453ffede22f0a44a0b7a.png" alt=""><figcaption></figcaption></figure></div>

    <div align="left"><figure><img src="../.gitbook/assets/img-36eb9d167c27c6e1de0a21824b94210a.png" alt=""><figcaption></figcaption></figure></div>

{% hint style="warning" %}
Large scans can hit a size limit if the crawler follows static assets. Exclude paths like \*.css, \*.js, \*.png, \*.svg, \*.woff to keep the scan efficient.
{% endhint %}

{% hint style="info" %}
When running via the Checkmarx platform, start with 2–4 for numberOfBrowsers/threadPerHost/threadCount rather than higher values.
{% endhint %}

Here are two examples of configuration files. One for a web scan and the second for an API scan. They are viewable in a text editor like Notepad.

After saving the plan, this file is ready to use. To run a scan with it, see [Running a Scan](../running-a-scan/dast-running-a-scan.md): when creating a new scan for a Web environment, upload this file in the Upload Configuration file section (for an API environment, you'll also need to select a Swagger/Postman file).

{% hint style="info" %}
You can also download the sample Web/API configuration files above and edit them directly instead of building a plan from scratch in the ZAP GUI.
{% endhint %}

[API SCAN](https://download.checkmarx.com/cxcustomersdocuments/api.yaml)

[WEB SCAN](https://download.checkmarx.com/cxcustomersdocuments/web.yaml)
