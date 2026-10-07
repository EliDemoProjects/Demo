# Creating a Project - Project Types

There are two types of Projects in SCA:

- **General** - upload the source code as a ZIP file, or enter a URL to a public repository.
- **GitHub** - integrate your Project with a private GitHub repository.

The following table shows the functionality of each type of Project:

| **Feature** | **General Project** | **GitHub Project** |
| --- | --- | --- |
| Location of source code | <ul><li><p>Local zip archive</p></li><li><p>CI/CD pipeline</p></li><li><p>Public GIT<sup>1</sup>repository</p></li></ul> | GitHub repository, using personal access tokens (PAT) |
| Scan trigger | <ul><li><p>Web platform</p></li><li><p>Plugins</p></li><li><p>API</p></li><li><p>Checkmarx SCA Resolver</p></li><li><p>Checkmarx SCA Agent</p></li></ul> | <ul><li><p>Web platform</p></li></ul> |
| Remediation through Pull Request | Not supported | Supported |
| Rescan method | Upload zip archive or specify URL each time that you run the scan | Rescan original GitHub repository<br>**Tip** Once the access token has been configured it can’t be changed for that Project. |

<sup>1</sup> Any GIT URL on which the “git clone” command can be used.
