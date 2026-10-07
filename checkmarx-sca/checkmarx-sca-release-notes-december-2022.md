# Checkmarx SCA Release Notes December 2022

We are excited to announce important improvements in our Checkmarx SCA web application…

## Key improvements

### Notifications

Users can now create customized **Notifications** to be sent automatically to the designated recipients when important events occur in the account. Notifications can be sent via email and/or by configuring webhooks for integration with other platforms.

{% hint style="info" icon="pencil" %}
There is a one-to-one relationship between notifications and projects. Meaning that each notification has a single project assigned to it, and each project can only be assigned to a single notification.
{% endhint %}

You can configure notifications for the following event types.

- **New vulnerability** - a new vulnerability was identified in a package that is used in the project.
- **Policy violation** - a scan of the project identified violations of the security policies that are assigned to the project.
- **Successful scan** - the project was scanned successfully.
- **Failed scan** - an attempted scan of the project failed.

By default, for each new project created in SCA a notification is configured to send **New vulnerability** and **Policy violation** notifications to the email of the user who created the project. You can edit or delete existing notifications and you can create new notifications (for projects that aren't yet assigned to a notification).

To learn more about notifications, see [Notifications](notifications.md).

### Tags

We now enable users to add Tags to projects and to scans. This makes it easy to identify projects and scans with specific characteristics by filtering the tables in the web portal by tags. For example, you can add the DEV tag to all projects still in development, and then filter to view all DEV projects. Tags can be simple strings or key:value pairs, enabling filtering by key, value or both.

Project tags can be configured when creating a project, and they can also be added deleted or edited at any time. Project tags are automatically inherited by all subsequent scans of the project. Scan tags can also be added for specific scans when running the scan.

## Checkmarx SCA Resolver Updates

We have released several new versions of Resolver with a wide range of improvements and bug fixes. Download the latest version of SCA Resolver [here](checkmarx-sca-resolver-download-and-installation.md).

### Improvements in Version 1.15.2

- Parameter values are now case insensitive.
- Added a new flag to cause the scan to fail and return exit code 9 when resolution fails for one or more of the manifest files.
- For PIP, fixed problem with the file path when using the -r flag inside a requirements.txt file.
