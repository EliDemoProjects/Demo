# Checkmarx SCA (REST) API - POST Token

## Method

### POST

## Description

Submit your **username**, **password**, and **Tenant Account** name to obtain an Access Token for use during the current session.

{% hint style="warning" %}
To use the Checkmarx SCA APIs you need to use a local user account that was created through Checkmarx SCA User Management and not an account that was added via Master Access Control.
{% endhint %}

When using APIs, you have the same permissions that your user account has in the web portal (UI). For example, a user with a Viewer role will only be able to perform GET APIs but not POST, PUT etc. Also, you can only access Projects that are assigned to a Team in which you are a member.

At the beginning of each new session, you need to submit your **username**, **password**, and **Tenant Account** name using this API and receive an Access Token in the response. The Access Token is then submitted for authentication with each API call during this session. The Access Token is valid for an hour, after which you will need to resubmit your credentials to obtain a new Access Token.

## Workflow

1. `POST /identity/connect/token` and generate an Access Token

2. Apply the Access Token to all API requests as shown in the following example:

   `curl -X GET https://api-sca.checkmarx.net/risk-management/projects -H "Authorization: bearer {{access_token}}"`

## URL

- US Environment - https://platform.checkmarx.net/identity/connect/token
- EU Environment - https://eu.platform.checkmarx.net/identity/connect/token

## cURL Sample

```
curl 'https://platform.checkmarx.net/identity/connect/token' \
--data-urlencode "username=DemoUser" \
--data-urlencode "password=Demo1234" \
--data-urlencode "acr_values=Tenant:DemoTenant" \
--data-urlencode "scope=sca_api" \
--data-urlencode "client_id=sca_resource_owner" \
--data-urlencode "grant_type=password"
```

{% hint style="info" icon="pencil" %}
If you would like to use this token also for the Access Control APIs, then set the scope as:

--data-urlencode "scope=sca_api access_control_api"
{% endhint %}

## Media Type (header)

Accept: application/x-www-form-urlencoded

## Parameters

Body Parameters - Required

| Parameter | Type | Enum | Description |
| --- | --- | --- | --- |
| username | string | - | Your Checkmarx SCA username. |
| password | string | - | Your Checkmarx SCA password. |
| acr_values | string | - | The name of the tenant account preceded by **Tenant:**<br>e.g., Tenant:DemoTenant |
| scope | string | sca_api | To access the SCA APIs, set the scope as “sca_api”.<br>To access the Access Control APIs, set the scope as “access_control_api”. |
| client_id | string | sca_resource_owner | Client_id must be set a “sca_resource_owner”. |
| grant_type | string | password | Grant_type must be set as “password”. |

## Success Response

Code: 200 OK

| Attribute | Type | Description |
| --- | --- | --- |
| access_token | string | A string which is used for authentication when submitting API requests. |
| expires_in | integer | Time left until the token expires (given in seconds).<br>Tokens are valid for one hour. |
| token_type | string | The type of authentication, e.g Bearer. |

### Sample Success Response

```
{
    "access_token": "12345zI1NiIsIHmtpZCI6IjU2OTM3MjlGOTcyNTRFRjhCNDU0RjBFMkE4RDBCRkEzNEEwRTc5OTYIiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJWcE55bjVjbFR2aTBWUERpcU5DX28wNE9lWkIkifQ.QoYgWkAp2PFRlNAK22TSBdoGUvTz29XlNoIU8zuaadZL2ptRSOeqso1kcEYA4MTK_JuLVzqcZIGbJ9MlVdIyeGH8O6Sp25O-9ZhPtRRIqhKMB3Pc95uMw1kbOyjVDxNT4G3yJZkqIn6uLh9gXdwlAMYw4SHLPSIY5xI0sx6QhA89E8044fORlevhpT8cBf7dLIr0Q_73K7n1n3gC-amDAzgW2-kby6b6c5tWv7h_CGORa2NfwgWAaNatkjy4IQEfjk60SS7YyX1vJVN7iVcO0CgnMNioi4pxfT8abcde",
    "expires_in": 3600,
    "token_type": "Bearer"
}
```
