# Spider

## Description

The Spider is a tool that automatically discovers new resources (URLs) on a particular site. It begins with a list of URLs to visit, called seeds, which depend on how the Spider is run. The Spider then visits these URLs, identifies all the hyperlinks on the page and adds them to the list of URLs to visit and the process continues recursively as long as new resources are found.

## Jobs structure

```
 - type: spider
   name: "spider"
    parameters:
      context: "Default Context"
      user: "test_user"
      url: ""
      maxDuration: 0
      maxDepth: 0
      maxChildren: 0
```

## Possible parameters

[browserId: \<string\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N656350a6e3e81) (Default - firefox-headless)

Browser ID to use.

[clickDefaultElems: \<boolean\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65635113ab462) (Default - true)

When enabled only click the default element: 'a', 'button', and 'input'; to be modified only for specific scenarios of spidering applications that are more complex in terms of Ajax interactions.

[clickElemsOnce: \<boolean\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N656352a5d84d6) (Default - true)

When enabled only click each element once; to be modified only for specific scenarios of spidering applications that are more complex in terms of Ajax interactions.

[context: \<string\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634b0a87574)

The context mentioned in ENV:

[elements:](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N6563573a190dc)

A list of HTML elements to click - will be ignored unless `clickDefaultElems` is false.

- "a" - represents the HTML element LINK.
- "button" - represents the HTML element BUTTON.
- "input" - represents the HTML element Input.

[eventWait: \<integer\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N6563558cbf1e4) (Default - 1000)

The time in milliseconds to wait after a client-side event is fired.

[inScopeOnly: \<boolean\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634ff8eacd9) (Default - true)

If true then any URLs requested which are out of scope will be ignored; for microservices / muti-endpoint applications the setting should be set to false.

[maxCrawlDepth: \<integer\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634c6dcb0da) (Default - 10, 0 is unlimited)

At maximum depth of analysis, the spider will continue following links when crawling the application; it will impact the duration of the scan and should reflect the goal of the DAST scan.

[maxCrawlStates: \<integer\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N656355fb716d7) (Default - 0 is unlimited)

The maximum number of crawl states the crawler should crawl.

[maxDuration: \<integer\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634bfad8ddb) (Default - 0 is unlimited)

Maximum duration time for spider analysis; it will impact the duration of the scan and should reflect the goal of the DAST scan.

[numberOfBrowsers: \<integer\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634d1b9f6d7) (Default - 1)

The number of browsers the spider will use, more will be faster but will use up more memory.

[randomInputs: \<boolean\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N6563567a69b5f) (Default - true)

When enabled random values will be entered into the input element.

[reloadWait: \<integer\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N656356e43e988) (Default - 1000)

The time in milliseconds to wait after the URL is loaded.

[runOnlyIfModern: \<boolean\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634db1c9b72) (Default - false)

If true then the spider will only run if a "modern app" alert is raised; it is recommended to force the spider by setting it to false.

[url: \<string\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634bb4c3625) (Default - inherited from context)

URL to start spidering.

[user: \<string\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634b5c05297) (Default - inherited from context)

An optional user to use for authentication must be defined in the env.

| Name | Description | Type / Default |
| --- | --- | --- |
| `context:` | The context mentioned in ENV: | String |
| `user:` | `An optional user to use for authentication must be defined in the env` | String, inherited from Context |
| `url:` | URL to start spidering | String, inherited from Context |
| `maxDuration:` | Maximum duration time for spider analysis; it will impact the duration of the scan and should reflect the goal of the DAST scan | Integer, default: 0 unlimited |
| `maxCrawlDepth:` | At maximum depth of analysis, the spider will continue following links when crawling the application; it will impact the duration of the scan and should reflect the goal of the DAST scan | Integer, default: 10, 0 is unlimited |
| `numberOfBrowsers:` | The number of browsers the spider will use, more will be faster but will use up more memory | Integer, default: 1 |
| `runOnlyIfModern:` | If true then the spider will only run if a "modern app" alert is raised; it is recommended to force the spider by setting it to false | Boolean, default: false |
| `inScopeOnly:` | If true then any URLs requested which are out of scope will be ignored; for microservices / multi-endpoint applications the setting should be set to false | Boolean, default: true |
| `browserId:` | Browser Id to use | String, default: firefox-headless |
| `clickDefaultElems:` | When enabled only click the default element: 'a', 'button', and 'input'; to be modified only for specific scenarios of spidering applications that are more complex in terms of Ajax interactions | Boolean, default: true |
| `clickElemsOnce:` | When enabled only click each element once; to be modified only for specific scenarios of spidering applications that are more complex in terms of Ajax interactions | Boolean, default: true |
| `eventWait:` | The time in milliseconds to wait after a client-side event is fired | Integer, default: 1000 |
| `maxCrawlStates:` | The maximum number of crawl states the crawler should crawl | Integer, default: 0 unlimited |
| `randomInputs:` | When enabled random values will be entered into the input element | Boolean, default: true |
| `reloadWait:` | The time in milliseconds to wait after the URL is loaded | Integer, default: 1000 |
| `elements:` | A list of HTML elements to click - will be ignored unless clickDefaultElems is false |  |
| <ul><li><p>"a"</p></li></ul> | It represents the HTML element LINK |  |
| <ul><li><p>"button"</p></li></ul> | It represents the HTML element Button |  |
| <ul><li><p>"input"</p></li></ul> | It represents the HTML element Input |  |
