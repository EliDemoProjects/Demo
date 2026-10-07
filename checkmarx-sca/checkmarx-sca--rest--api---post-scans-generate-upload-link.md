# Checkmarx SCA (REST) API - POST Scans Generate Upload Link

## Description

This API is used when the source code for your Project is in a zip file. This API generates an upload link for uploading the zip file to be scanned. The upload link generated in this step will then be used in the **PUT Upload Link** and **POST Scan** calls.

## Method

### POST

{% include ".gitbook/includes/section-1ed6de35.md" %}

## URL

- US Environment - https://api-sca.checkmarx.net/api/uploads
- EU Environment - https://eu.api-sca.checkmarx.net/api/uploads

## cURL Sample

```
curl -X PUT " https://api-sca.checkmarx.net/risk-management/settings/projects/1a73fc26-b7aa-4ecd-b2dd-d3aebfc1da21" -H "accept: application/json" -d "{ "enableExploitablePath": true}”
```

## Media Type (header)

Authorization: Bearer \<access_token\>

Accept: application/json

## Parameters

There are no parameters.

## Success Response

Code: 200 OK

Attributes:

| Attribute | Type | Enums | Description |
| --- | --- | --- | --- |
| url | string | - | The url that will be needed for the next two steps of the flow (**PUT Upload Link** and **POST Scan**) for scanning a ZIP file. |

### Sample Success Response

```
{
    "url": "https://microservice-scanrunner-prod-scanuploadsstorage-1ojrycav225s8.s3.amazonaws.com/8ecasfaf-ace0-4cfe-9033-b6e3868b3062/20209412-052543303_pb4xceya.obb?AWSAccessKeyId=ASIA43BGVO4IRRFUV57V&Expires=1618206943&x-amz-security-token=IQoJb3JpZ2luX2VjEFsHaCXVzLWVhc3QtMSJIMEYCIQDYRu7m9z%2FiuwVDrMrFti5iFDq%2FsHr15F2CYEpbfOfALlwIhALFS5jzyEoYag6Qc61Xe6PyWz%2FnPvdS9FxhWror6YFgZKr4DCLIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQAhoMODgyNjk2ODc3ODQxAIgy%2BSAJ9Oy%2F2H5%2FpR88qkgOj9SL%2B0s0kz8c%2BZ810rENDr7jKFn7M8%2BHVJW1HevJvaKHrFz%2BpF49HCis1clBsiCCEB%2Bu6ZSKZmdli0MxKv5ORkP6DGh0Y3EzD7S7GgbTCYO5tDAmhoAn4FsRa1kVvwUBVadfkeSw%2FfN034dexr%2Bskuasdx2aesaacwTS%2F7eoX9USUlg%3D&Signature=RVxqR4srfQDMC5wXKbhasdfGDP0Fs%3D"
}
```

## Error Response

|  |
| --- |
| {% tabs %}<br>{% tab title="Status code: 400" %}<br>Message: `Bad data.`<br>{% endtab %}<br>{% tab title="Status code: 500" %}<br>Message: `InternalServerError`<br>{% endtab %}<br>{% endtabs %} |
