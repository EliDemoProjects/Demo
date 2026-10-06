# Scanning Projects

You can run a scan of a Project as part of the initial Project configuration. You can also scan an existing Project at any time. Once the initial scan has been run on the Project there are two options for updating the results for the Project.

- **Rescan** - you can rerun the scan at any time. This executes a completely new scan on your current source code. This enables you to track the vulnerable packages throughout your SDLC and monitor the risks to your project as it develops. This option should be used when the source code has been changed since the previous scan, e.g., you have developed new features or you have taken steps to remediate the risks in your project.

  For GitHub Projects the scan runs automatically on the current source code in your repo; for General Projects you specify the .zip file or public repository URL each time that you run the scan.
- **Recalculate** - Checkmarx SCA recalculates the risks associated with your source code based on the data obtained by the previous scan. This will identify risks that have been recently discovered in the packages that are used by your project. This option should be used if you know that no significant changes have been made to the source code since the previous scan.
