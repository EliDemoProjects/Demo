# Spider Ajax

The AJAX Spider is a crawler of AJAX-rich sites called Crawljax. You can use it to identify the pages of the targeted site. You can combine it with the (normal) spider for better results.

The spiderAjax job allows you to run the Ajax Spider - it is slower than the traditional spider but handles modern web applications well.

If the runOnlyIfModern is set to True then the [passiveScan-wait](passivescan-wait.md) job MUST be run before this one (as well as after it) and the Modern Web Application rule installed and enabled. If either of those things are not done then the Ajax spider will always run and a warning output. If they are both done and no Modern Web Application alert is raised then the assumption is made that this is a traditional app and therefore the Ajax spider is not needed.

## Jobs structure

```
- type: spiderAjax                   # The Ajax spider is slower than the normal spider but handles modern apps well.
  name: "spiderAjax"
    parameters:
      context: "Default Context"
      user: "test_user"
      url: ""
      maxDuration: 60
      maxCrawlDepth: 10
      numberOfBrowsers: 1
      runOnlyIfModern: false
```

## Possible parameters

| Name | Description | Type / Default |
| --- | --- | --- |
| `context:` | The context mentioned in ENV: | String |
| `user:` | User to be used for authentication (optional), generally inherited from ENV context | String, inherited from Context |
| `url:` | URL to start spidering | String, inherited from Context |
| `maxDuration:` | Maximum duration time for spider analysis; it will impact the duration of the scan and should reflect the goal of the DAST scan | Integer, default: 0 unlimited |
| `maxCrawlDepth:` | Maximum depth of analysis, the spider will continue following links when crawling the application; it will impact the duration of the scan and should reflect the goal of the DAST scan | Integer, default: 10, 0 is unlimited |
| `numberOfBrowsers:` | The number of browsers the spider will use, more will be faster but will use up more memory | Integer, default: 1 |
| `runOnlyIfModern:` | If true then the spider will only run if a "modern app" alert is raised; it is recommended to force the spider by setting it to false | Boolean, default: false |
| `inScopeOnly:` | If true then any URLs requested which are out of scope will be ignored; for microservices / multi-endpoint applications the setting should be set to false | Boolean, default: true |
| `browserId:` | Browser ID to use | String, default: firefox-headless |
| `clickDefaultElems:` | When enabled only click the default elements: a, button, and input; to be modified only for specific scenarios of spidering applications that are more complex in terms of Ajax interactions | Boolean, default: true |
| `clickElemsOnce:` | When enabled only click each element once; to be modified only for specific scenarios of spidering applications that are more complex in terms of Ajax interactions | Boolean, default: true |
| `eventWait:` | The time in milliseconds to wait after a client-side event is fired | Integer, default: 1000 |
| `maxCrawlStates:` | The maximum number of crawl states the crawler should crawl | Integer, default: 0 unlimited |
| `randomInputs:` | When enabled random values will be entered into the input element | Boolean, default: true |
| `reloadWait:` | The time in milliseconds to wait after the URL is loaded | Integer, default: 1000 |
| `elements:` | A list of HTML elements to click - will be ignored unless clickDefaultElems is false |  |
| -"a" | It represents the HTML element LINK |  |
| -"button" | It represents the HTML element Button |  |
| -"input" | It represents the HTML element Input |  |
