# Scanning a Project

## Preparing your Source Code for Scanning

If the source code uses a “lock” file, you must also include the package.json file in the project folder.

## Running a Scan Manually

You can manually run a scan of an existing Project through the web application, using one of the following methods:

{% hint style="info" icon="pencil" %}
If you haven’t yet set up a Project for the source code that you would like to scan, then first create the Project as described in [Creating a Project - Project Types](creating-a-project---project-types.md).
{% endhint %}

- On the Project page, hover over the Scan icon located on the top right corner of the page and click the Scan Project button.

  <div align="left"><figure><img src=".gitbook/assets/img-37487e3fe7f72e901f8f47223626caaa.png" alt=""></figure></div>

{% hint style="info" icon="pencil" %}
If the Project has not yet been scanned, then the Scan now button is shown in the center of the screen. Otherwise, the procedure is identical whether this is the initial scan or a rescan of a Project that has already been scanned.
{% endhint %}

- On the Dashboard (Home page), in the Projects pane, click on![](.gitbook/assets/img-1d1787297384426534f8e8ba6ac6cb44.png) in the row of the desired Project and select Scan Project.

  <div align="left"><figure><img src=".gitbook/assets/img-9653796c1ac8a63951d7073e732a8afc.png" alt=""></figure></div>

- For a **General** project, the Scan project dialog opens. Enter the zip file or Git URL, since Checkmarx SCA does not save this information.

  <div align="left"><figure><img src=".gitbook/assets/img-08dc5c30a2eacb3ef4af9f55e705f0d7.png" alt="" width="50%"></figure></div>

- For a **GitHub** project, the scan starts immediately, since Checkmarx SCA saves the access token and Git URL.

{% hint style="warning" %}
If the access token has been deleted from GitHub, you will get an error message when you try to re-scan the project.
{% endhint %}

## Scan Automation

You can set up integrations that will automatically trigger scans as part of your SDLC, e.g., scanning the project before each build. This can done using the Checkmarx CLI plugin or specialized plugins for various platforms (e.g., Jenkins, Azure DevOps etc.), see [Checkmarx SCA - Integrations and Plugins](https://app.gitbook.com/s/XSPACE_INTEGRATIONS/).
