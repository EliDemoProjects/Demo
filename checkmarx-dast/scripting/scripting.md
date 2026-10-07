# Scripting

This page describes the general concepts and paradigms when adding scripts to the ZAP-Scan. Checkmarx DAST can run scans via the DAST-CLI (a self-managed, containerized scanner you configure with a YAML file) or via CheckmarxOne (Checkmarx's hosted platform). Scripting extends what the underlying ZAP engine does during a scan, and because scripts run arbitrary code, this capability is available only in the DAST-CLI.

{% hint style="warning" %}
Script jobs are supported only on the DAST-CLI and are blocked for CheckmarxOne users for security reasons.
{% endhint %}

## Scripts - Overview

The ZAP-Engine can execute external code (scripts) during the ZAP-scan.

This code interacts with ZAP internal objects and can be used to extract information not normally exported from the Engine or to influence the flow of the scan.

The ZAP-Engine comes with a series of built-in scripts that are ready to use. Also, there are community scripts that can be used as a base for custom scripts, tailor-made for specific sites: [ZAP Community Scripts repo](https://github.com/zaproxy/community-scripts)

Built-in scripts can be enabled or disabled, and custom scripts can be added or removed.

## Supported languages:

* JavaScript (ECMAScript)
* Zest
* Any language that supports JSR 223 (Groovy, Kotlin, Python, Ruby…)
* For more information, see: [https://www.zaproxy.org/docs/desktop/start/features/scripts/](https://www.zaproxy.org/docs/desktop/start/features/scripts/)

{% hint style="info" %}
DAST includes only two ZAP script engines - ZEST and GraalJS - so the broader scripting flexibility available in ZAP does not fully apply unless you manually adjust scripts through the DAST‑CLI. Because GraalJS executes JavaScript on the JVM rather than in a standard ECMAScript environment, its behavior differs from typical JavaScript engines, and some ECMAScript features are not supported.
{% endhint %}

## Script-categories

Scripts are divided into categories:

* Authentication - executed when the Engine detects it needs to authenticate before proceeding
* Encode/Decode - help encode/decode payloads to be used by other scripts
* HTTP Sender - executed on captured requests and/or responses
* Proxy - change the behavior of ZAP’s internal proxy
*   Selenium - effective for jobs that utilize Selenium (Spider-Ajax for example);

    Can extract/modify data and/or DOM from within the browser
* Session Management - executed after authentication (if applicable), used to reuse the session during the scan
*   Stand Alone - executed before or after a scan;

    Can be used for authentication in a demo, or to extract internal-engine-information

    (for example, extracting the list of attacked URLs).

## Scripts structure

Many scripts contain:

* Functions triggered by the ZAP-Engine’s objects. Those functions receive objects that expose the internal objects of ZAP to the script code, for example, request, response, session, and user credentials. Each script category uses a different set of methods, see [https://github.com/zaproxy/community-scripts](https://github.com/zaproxy/community-scripts) for detailed examples
*   A function that defines the required parameters for the script:

    getRequiredParamsNames() { return \[“param1“, “param2”, …]; }
*   A function that defines the optional parameters for the script:

    getOptionalParamsNames() { return \[“param1“, “param2”, …]; }

## Automation

{% hint style="warning" %}
All script paths must be absolute paths due to a bug in the ZAP-Engine.
{% endhint %}

In order to use a script during the scan:

*   You must add a script job (see [examples](scripting.md) below) to the configuration file,

    in order to Add (custom scripts), or activate (built-in scripts) the script.
* Reference the script (in the Authorization and Session Management segments of the context)
* For more info: [https://www.zaproxy.org/docs/desktop/addons/script-console/automation/](https://www.zaproxy.org/docs/desktop/addons/script-console/automation/)

Each script job must contain the following parameters:

* action - add/remove/enable/disable. Use "add" for custom scripts you're introducing for the first time; use "enable"/"disable" to toggle built-in scripts that ZAP already ships with; use "remove" to delete a previously added custom script.
* type - the category (see Script-categories above)
* engine - the engine that will run the code
* name - a label for the script
* file - the absolute path to the script file. Alternatively, the script's content can be given inline via the inline parameter (leave file empty in that case).
* target - the URL this script applies to; leave as an empty string ("") if the script isn't scoped to a specific site, or set it to the site's base URL (as in the session example below) to scope the script

{% hint style="success" icon="key" %}
The job wrapper (\`type: "script"\` at the outer level) and the script's category (\`type\` inside \`parameters\`, e.g., \`"authentication"\`) both use the key name \`type\` but are unrelated. When copying an example, leave the outer \`type: "script"\` as-is. Only the inner \`type\` under \`parameters\` should change to match the category of script you're adding.
{% endhint %}

### Script Job Examples:

* The script files are present at (or mounted into) /home/ubuntu

```
- parameters:
    action: "add"
    type: "authentication"
    engine: "ECMAScript : Graal.js"
    name: "ginandjuice"
    file: "/home/ubuntu/ginandjuice_auth.js"
    target: ""
    inline: ""
  name: "script"
  type: "script"
```

```
- parameters:
    action: "add"
    type: "session"
    engine: "ECMAScript : Graal.js"
    name: "ginandjuice_session"
    file: "/home/ubuntu/ginandjuice_session.js"
    target: "https://ginandjuice.shop"
    inline: ""
  name: "script"
  type: "script"
```

{% hint style="info" icon="pencil" %}
DAST-CLI supports Graal.js and Zest out of the box since these script engines are integrated into the ZAP package. CheckmarxOne users are blocked from using scripts for security reasons.

Other engines are required to add a plugin (which is not supported in the DAST-Workers).

Examples of engine names:

* `ECMAScript : Graal.js` - supported out of the box in DAST-CLI
* `Zest : Mozilla Zest` - supported out of the box in DAST-CLI
* `ECMAScript : Oracle Nashorn` - requires an additional ZAP plugin; not available in DAST-Workers
* `python : jython` - requires an additional ZAP plugin; not available in DAST-Workers
{% endhint %}

### Referencing Scripts in the Configuration

Authentication and session management can directly reference scripts.

The scripts must be added in a script-job in order to be available

```
env:
  contexts:
    - name: "GinAndJuice"
      ...
      authentication:
        method: "script"
        parameters:
          script: "/home/ubuntu/ginandjuice_auth.js"
          scriptEngine: "ECMAScript : Graal.js"
          ...
      sessionManagement:
        method: "script"
        parameters:
          script: "/home/ubuntu/ginandjuice_session.js"
          scriptEngine: "ECMAScript : Graal.js"
      ...
```

## DAST-CLI

The script files, like the configuration file, must be mounted inside the container for the ZAP-CLI (within the DAST-CLI container) to utilize them.

There are no other required modifications on the docker run command except for mounting the script files.

See [Installing the DAST CLI in a Pipeline](../using-the-dast-cli/dast-installing-the-dast-cli-in-a-pipeline.md) for more details on the docker run command.

## GinAndJuice

* These files are to be used as a reference for how scripts are built and how a configuration file can add and link scripts to the authorization process. They will require modifications to run as a demo.
*   Due to a bug in the Windows GUI for ZAP, the authorization script must use hard-coded credentials when running a regular proxy scan.

    Running scans in automation (ZAP-CLI or GUI) works as expected.

[ginandjuice\_session.js](https://download.checkmarx.com/cxcustomersdocuments/ginandjuice_session.js): the session management script referenced by the \`sessionManagement\` job in the example config.

[ginandjuice\_yaml](https://download.checkmarx.com/cxcustomersdocuments/gin_juice_script+\(1\).yaml): the full automation config file that ties the two scripts above into a GinAndJuice scan context.

[ginandjuice\_auth.js](https://download.checkmarx.com/cxcustomersdocuments/ginandjuice_auth.js): the authentication script referenced by the \`authentication\` job in the example config; requires hard-coded credentials to be edited in before use.
