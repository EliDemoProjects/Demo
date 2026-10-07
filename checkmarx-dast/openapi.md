# openapi

## Description

This job allows you to spider all the endpoints addressed in the Swagger file. Versions 1.2, 2.0, and 3.0 are supported.

## Jobs structure

```
- type: openapi         
    parameters:
      apiFile: "C:\\Users\\OpenAPI.yaml"  
      apiUrl: ""  
      context: "Default Context"   
      targetUrl: "http://TestURL.com/*"  
```

## Possible parameters

Glossary

[apiFile: \<string\>](openapi.md#UUID-2dd5fd3a-68a0-76c0-6358-1264f42cb69f_N6565f0062f9cb) (Default - null, no definition will be imported)

The local file containing the OpenAPI definition.

[Context: \<string\>](openapi.md#UUID-2dd5fd3a-68a0-76c0-6358-1264f42cb69f_N6565f05d50dff) (Default - null, no context will be used)

Context to use when importing the OpenAPI definition.

[targetUrl: \<string\>](openapi.md#UUID-2dd5fd3a-68a0-76c0-6358-1264f42cb69f_N6565f0a37af0a) (Default - null, the target will not be overridden)

URL which overrides the target defined in the definition.

| Name | Description | Type / Default |
| --- | --- | --- |
| `apiFile:` | The local file containing the OpenAPI definition | String, null, no definition will be imported |
| `Context:` | Context to use when importing the OpenAPI definition | String, null, no context will be used |
| `targetUrl:` | URL which overrides the target defined in the definition | String, null, the target will not be overridden |
