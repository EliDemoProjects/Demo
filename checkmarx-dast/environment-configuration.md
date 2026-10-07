# Environment configuration

This section of the YAML configuration file defines the applications where the rest of the jobs can work.

At this stage, in terms of authentication mechanisms, there's support for form-based and HTTP/NTLM authentications.

Note : When testing targets that operate on default ports (80 for HTTP, 443 for HTTPS), the colon portion of the URL should not be included. Including that portion (for example: [http://example.com:80](http://example.com/)) may result in an inability to crawl or test the target. If a ‘default’ port is specified, the engine will treat it without the default port being included then it doesn’t match the expectation within the Context, and there’s nothing to interact with as part of the Context.

## Environment Structure

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
```

| Name | Description | Type / Default |
| --- | --- | --- |
| contexts: |  |  |
| name: context 1 | Name to be used to refer to this context in other jobs, mandatory |  |
| urls: | A mandatory list of top-level URLs will include everything under each URL. |  |
| includePaths: | List of all the base URLs to be scanned (optional) |  |
| excludePaths: | List of URLs to be excluded from being scanned (optional) |  |
| authentication: |  |  |
| method: | One of: 'HTTP,' 'form,' 'JSON,' or 'script' | String |
| parameters: | May include any required scripts. All of the parameters support vars except for the port. |  |
| hostname: | Only for 'HTTP' authentication | String |
| port: | Only for 'HTTP' authentication | Int |
| realm: | Only for 'HTTP' authentication | String |
| loginPageUrl: | The login page URL to read before making the request, only for 'form' or 'JSON' authentication | String |
| loginRequestUrl: | The login URL to request is only for 'form' or 'JSON' authentication. | String |
| loginRequestBody: | The login request body - if not supplied, a GET request will be used only for 'form' or 'JSON' authentication | String |
| script: | Path to a script, only for 'script' authentication | String |
| scriptEngine: | The name of the script engine to use, only for 'script' authentication | String |
| verification: |  |  |
| method: | One of the 'response,' 'request,' 'both,' 'poll' | String |
| loggedInRegex: | Regex pattern for determining if logged-in | String |
| loggedOutRegex: | Regex pattern for determining if logged out | String |
| pollFrequency: | The poll frequency, only for 'poll' verification |  |
| pollUnits: | The poll units, one of 'requests,' 'seconds,' only for 'poll' verification | String |
| pollUrl: | The URL to the poll is only for 'poll' verification. | String |
| pollPostData: | Post date to include in the poll, only for 'poll' verification | String |
| pollAdditionalHeaders: | List of additional headers for poll request, only for 'poll' verification |  |
| <ul><li><p>header:</p></li></ul> | The header name |  |
| value: | The header value |  |
| sessionManagement: |  |  |
| method: | Either 'cookie,' 'http,' or 'script.' | String |
| parameters: | List of 0 or more parameters - may include any required for scripts. |  |
| script: | Path to a script, only for 'script' session management | String |
| scriptEngine: | The name of the script engine to use, only for 'script' session management | String |
| technology: |  |  |
| exclude: | List of tech to exclude, as per [https://www.zaproxy.org/techtags/](https://www.zaproxy.org/techtags/) (just use last names) |  |
| users: | List of one or more users available to use for authentication |  |
| <ul><li><p>name:</p></li></ul> | The name of the user to be used by the jobs | String |
| credentials: | List of user credentials - may include any required for scripts. |  |
| username: | The username to use when authenticating, vars supported | String |
| password: | The password to use when authenticating, vars supported | String |
| vars: | List of 0 or more custom variables to be used throughout the config file |  |
| myVarOne: CustomConfigVarOne | Can be used as ${myVarOne} anywhere throughout the config |  |
| myVarTwo: ${myVarOne}.VarTwo | Can refer other vars |  |
| parameters: |  |  |
| failOnError: true | If set exit on an error |  |
| failOnWarning: false | If set exit on a warning |  |
| progressToStdout: true | If set, will write job progress to stdout. |  |
|  |  |  |
