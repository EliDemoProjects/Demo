# Configuration File Structure

On this page, we will address the configuration file structure.

The configuration file has two major parts: environment (env:) and job (jobs:).

## Configuration file example

```
---
env:
  contexts:
    - name: "Default Context"
      urls:
        - "http://testhtml5.vulnweb.com/"
      includePaths:
        - "http://testhtml5.vulnweb.com/.*"
      excludePaths: []
      authentication:
        method: "form"
        parameters:
          loginPageUrl: "http://testhtml5.vulnweb.com/#/popular"
          loginRequestUrl: "http://testhtml5.vulnweb.com/login"
          loginRequestBody: "username={%username%}&password={%password%}"
        verification:
          method: "response"
          loggedInRegex: "Logout"
          loggedOutRegex: "Login"
          pollFrequency: 60
          pollUnits: "requests"
          pollUrl: ""
          pollPostData: ""
      sessionManagement:
        method: "cookie"
        parameters: {}
      technology:
        exclude: []
      users:
        - name: "test_user"
          credentials:
            password: "admin"
            username: "admin"
  parameters:
    failOnError: true
    failOnWarning: false
    progressToStdout: true
  vars: {}
jobs:
  - parameters:
      scanOnlyInScope: true
      enableTags: false
    rules: []
    name: "passiveScan-config"
    type: "passiveScan-config"
  - parameters:
      context: "Default Context"
      user: "test_user"
      url: ""
      maxDuration: 0
      maxDepth: 0
      maxChildren: 0
    name: "spider"
    type: "spider"
  - parameters: {}
    name: "passiveScan-wait"
    type: "passiveScan-wait"
  - parameters:
      template: "risk-confidence-html"
      reportDir: ""
      reportTitle: "ZAP Scanning Report"
      reportDescription: ""
    name: "report"
    type: "report"
```
