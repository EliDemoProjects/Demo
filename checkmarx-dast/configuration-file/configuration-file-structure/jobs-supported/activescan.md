# activescan

## Description

This job runs the active scanner. This actively attacks your applications and should therefore only be used on applications that you have permission to test.

By default, this job will actively scan the first context defined in the [environment](https://www.zaproxy.org/docs/desktop/addons/automation-framework/environment/) and so none of the parameters are mandatory.

## Job Structure

```
- parameters: {}
  policyDefinition:
    rules: []
  name: "activeScan"
  type: "activeScan"
```

## Possible parameters

Glossary

[addQueryParam: \<bool\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f23fcf58b) (Default - false)

If set will add an extra query parameter to requests that do not have one.

[context: \<string\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634b0a87574) (Default - first context)

Name of the context to attack.

[defaultPolicy: \<string\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f2889bf6b) (Default - default policy)

The name of the default scan policy to use.

[defaultStrength: \<string\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f54d3a396)

The default Attack Strength for all rules is either Low, Medium, High or Insane (not recommended).

[defaultThreshold: \<string\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f5a51b82e) (Default - Medium)

The default Alert Threshold for all rules, is either Off, Low, Medium, or High.

[delayInMs: \<int\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f2cfafe3a) (Default - 0)

The delay in milliseconds between each request, used to reduce the strain on the target.

[handleAntiCSRFTokens: \<bool\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f38cbcd7b) (Default - false)

If set, automatically handles anti-CSRF tokens.

[id: \<int\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f6536c160)

The rule id as per [https://www.zaproxy.org/docs/alerts/](https://www.zaproxy.org/docs/alerts/).

[injectPluginIdInHeader: \<bool\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f3de2033d)

If set, the relevant rule ID will be injected into the X-ZAP-Scan-ID header of each request.

[maxRuleDurationInMins: \<int\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f1a7c09cf) (Default - 0 unlimited)

The max time in minutes any individual rule will be allowed to run for.

[maxScanDurationInMins: \<int\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f1f30d63b) (Default - 0 unlimited)

The max time in minutes the active scanner will be allowed to run for.

[name: \<string\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f6af45504)

The name of the rule for documentation purposes - this is not required nor actually used.

[policyDefinition:](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f4f5142de)

The policy definition - is only used if the 'policy' is not set.

[policy: \<string\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f17ac04cd) (Default - default policy)

Name of the scan policy to be used.

[rules:](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f60be2327)

A list of one or more active scan rules and associated settings which override the defaults.

[scanHeadersAllRequests: \<bool\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f46f5e968) (Default - false)

If set then the headers of requests that do not include any parameters will be scanned.

[strength: \<string\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f71437ac1) (Default - Medium)

The Attack Strength for this rule is either Low, Medium, High, or Insane.

[threadPerHost: \<int\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f4c1738bb) (Default - 2)

The max number of threads per host.

[threshold: \<string\>](activescan.md#UUID-7c72e188-4032-3114-6a47-439c016ed6b6_N6565f75846399) (Default - Medium)

The Alert Threshold for this rule, is either Off, Low, Medium, or High.

[user: \<string\>](spider.md#UUID-7b593ea7-9401-9e48-8475-ea63687a1835_N65634b5c05297)

An optional user to use for authentication, must be defined in the environment.

| Name | Description | Type / Default |
| --- | --- | --- |
| context: | String: Name of the context to attack | String, default: first context |
| user: | String: An optional user to use for authentication, must be defined in the environment | String |
| policy: | String: Name of the scan policy to be used | String, default: Default Policy |
| maxRuleDurationInMins: | Int: The max time in minutes any individual rule will be allowed to run for | Int, default: 0 unlimited |
| maxScanDurationInMins: | Int: The max time in minutes the active scanner will be allowed to run for | Int, default: 0 unlimited |
| addQueryParam: | Bool: If set will add an extra query parameter to requests that do not have one | Bool, default: false |
| defaultPolicy: | String: The name of the default scan policy to use. | String, default: Default Policy |
| delayInMs: | Int: The delay in milliseconds between each request, used to reduce the strain on the target | Int, default 0 |
| handleAntiCSRFTokens: | Bool: If set, automatically handles anti-CSRF tokens | Bool, default: false |
| injectPluginIdInHeader: | If set, the relevant rule Id will be injected into the X-ZAP-Scan-ID header of each request, | Bool |
| scanHeadersAllRequests: | Bool: If set then the headers of requests that do not include any parameters will be scanned, | Bool, default: false |
| threadPerHost: | Int: The max number of threads per host | Int, default: 2 |
| policyDefinition: | The policy definition - is only used if the 'policy' is not set |  |
| defaultStrength: | The default Attack Strength for all rules is either Low, Medium, High, or Insane (not recommended). | String |
| defaultThreshold: | String: The default Alert Threshold for all rules, is either Off, Low, Medium, or High. | String, default: Medium |
| rules: | A list of one or more active scan rules and associated settings which override the defaults. |  |
| id: | Int: The rule id as per [https://www.zaproxy.org/docs/alerts/](https://www.zaproxy.org/docs/alerts/) |  |
| name: | String: The name of the rule for documentation purposes - this is not required nor actually used. | String |
| strength: | The Attack Strength for this rule is either Low, Medium, High, or Insane. | String, default: Medium |
| threshold: | The Alert Threshold for this rule, is either Off, Low, Medium, or High. | String, default: Medium |
