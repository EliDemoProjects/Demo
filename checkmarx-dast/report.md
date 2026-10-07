# report

## Description

`The report job allows you to generate reports using any of the installed report templates.`

{% hint style="info" icon="pencil" %}
This jobs is only supported in the pipeline approach (using the docker image to run the DAST scan) and for the traditional-pdf format.
{% endhint %}

## Job Structure example

```
- parameters:
    template: "traditional-pdf"
    reportDir: ""
    reportTitle: "ZAP Scanning Report"
    reportDescription: ""
  name: "report-pdf"
  type: "report"
```

## Possible parameters

Glossary

[confidences: \<list\>](report.md#UUID-329b6646-53b2-895a-3647-97e6d05f868e_N6565fb8b16af0) (Default - all)

The confidences to include in this report. High, Medium, Low, or falsepositive.

[displayReport: \<boolean\>](report.md#UUID-329b6646-53b2-895a-3647-97e6d05f868e_N6565fad7d0da3) (Default - false)

Display the report when generated.

[reportDescription: \<string\>](report.md#UUID-329b6646-53b2-895a-3647-97e6d05f868e_N6565faa60b050)

The report description.

[reportDir: \<string\>](report.md#UUID-329b6646-53b2-895a-3647-97e6d05f868e_N6565f9f1d36a8)

The directory into which the report will be written.

[reportFile: \<string\>](report.md#UUID-329b6646-53b2-895a-3647-97e6d05f868e_N6565fa2d3bac7) (Default - \{{yyyy-MM-dd}}-ZAP-Report-\[\[site\]\])

The report file pattern.

[reportTitle: \<string\>](report.md#UUID-329b6646-53b2-895a-3647-97e6d05f868e_N6565fa817d973)

The report title.

[risks: \<list\>](report.md#UUID-329b6646-53b2-895a-3647-97e6d05f868e_N6565fb11cf4d3) (Default - all)

The risks to include in this report. High, Medium, Low, or Info.

[sections: \<list\>](report.md#UUID-329b6646-53b2-895a-3647-97e6d05f868e_N6565fbe4d9e79) (Default - all)

The template sections to include in this report - see the relevant template.

[template: \<string\>](report.md#UUID-329b6646-53b2-895a-3647-97e6d05f868e_N6565f9b8ba309) (Default - traditional-html)

The template ID.

| Name | Description | Type / Default |
| --- | --- | --- |
| template: | The template id | String, default: traditional-html |
| reportDir: | The directory into which the report will be written | String |
| reportFile: | The report file name pattern | String, default: \{{yyyy-MM-dd}}-ZAP-Report-\[\[site\]\] |
| reportTitle: | The report title | String |
| reportDescription: | The report description | String |
| displayReport: | Display the report when generated | Boolean, default: false |
| risks: | The risks to include in this report | List, default: all<br><ul><li><p>high</p></li></ul><br><ul><li><p>medium</p></li></ul><br><ul><li><p>low</p></li></ul><br><ul><li><p>info</p></li></ul> |
| confidences: | The confidences to include in this report | List, default: all<br><ul><li><p>high</p></li></ul><br><ul><li><p>medium</p></li></ul><br><ul><li><p>low</p></li></ul><br><ul><li><p>falsepositive</p></li></ul> |
| sections: | The template sections to include in this report - see the relevant template | List, default all |
