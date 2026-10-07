# Checkmarx SCA Release Notes July 2024

{% include ".gitbook/includes/note-031596ef (1).md" %}

{% include ".gitbook/includes/warning-d19d3540 (1).md" %}

## Identifying "Framework" Dependencies

We now identify packages that are installed as part of the Framework installation. We label these packages as "Framework", and enable filtering the results to exclude these packages. This eliminates unnecessary noise, since these packages can't be remediated without updating the version of the overall framework. This feature is currently supported only for .NET projects.
