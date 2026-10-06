# Checkmarx SCA Release Notes August 2022

We are excited to announce important improvements in our Checkmarx SCA web application…

## Key improvements

### New Supported Languages and Package Managers

#### Ruby

We added support for Ruby projects, using RubyGems package manager to resolve `Gemfile` and `Gemfile.lock` manifest files.

#### Poetry

We added support for Poetry package manager for Python projects. Resolution is done using `pyproject.toml` (mandatory) and `poetry.lock` (optional) files.

#### C++

We now do file analysis (fingerprints) for C++ files (.cpp, .c, .h, .hpp, .a, .o, .so) hosted in GitHub or Conan Central.

### Risk Management

We have updated the Risk Management capabilities for Checkmarx SCA. Users can now change the state of risks (To Verify, Not Exploitable, Proposed not Exploitable, Confirmed or Urgent) and also add comments.

While viewing the Risk Details page for a specific risk, you can open a side panel with tabs for New Action (i.e. making changes) and for viewing History of changes made.

<div align="left"><figure><img src="../.gitbook/assets/img-ef1b72408bc5af0c62c5b29d9188fc9c (1).png" alt="" width="75%"><figcaption></figcaption></figure></div>

{% hint style="info" icon="pencil" %}
Only users with the `manage-risk` role (e.g. Admin, SCA Manager) are able to change the state of a Risk and add Comments.
{% endhint %}

#### Viewing Change History

Comments and state changes are shown in the All Risks table. Not Exploitable risks are marked with a strikethrough line. Hover over the comment icon to view the comment.

<div align="left"><figure><img src="../.gitbook/assets/img-0c8b6e879b2c6bf03644f4712ca5b452 (1).png" alt=""><figcaption></figcaption></figure></div>

In addition, a detailed history of all changes is shown in the Management of Risk panel > History tab. For each change that was made, the name of the user who made the change and the time of the change are shown. In addition, for state changes, the new state is shown alongside the previous state.

<div align="left"><figure><img src="../.gitbook/assets/img-b3ae1576cd2db6abab95d6aa21f1d5d4 (1).png" alt="" width="50%"><figcaption></figcaption></figure></div>

For more information about managing risk, see [Risk Management](https://app.gitbook.com/s/XSPACE_USER_GUIDE/risk-management--beta-).

## Improvements and Bug Fixes

| Status | Item             | Description                                                |
| ------ | ---------------- | ---------------------------------------------------------- |
| UPDATE | Private packages | Improved handling of private packages for Maven and Nuget. |
