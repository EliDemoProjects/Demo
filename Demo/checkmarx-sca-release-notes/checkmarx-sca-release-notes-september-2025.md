# Checkmarx SCA Release Notes September 2025

{% include ".gitbook/includes/note-031596ef.md" %}

{% include ".gitbook/includes/warning-d19d3540.md" %}

## SCA Updates

### Show Exploitable Method Details

On the Risk Details page, we now show details about the vulnerable methods that expose the vulnerability to exploitation. When the relevant details are available, we show the vulnerable file path, class, and method. This visibility increases transparency into how we evaluate exploitable paths, and provides actionable data for cases where full exploitable path analysis is not possible.

## SCA Resolver

Download the latest version [here](https://app.gitbook.com/s/XSPACE_RESOLVER/checkmarx-sca-resolver-changelog).

### Version 2.12.36 (September 25, 2025)

- Improved resilience while saving package results.
- For Pip, improved handling of resources during dependency resolution.
- For Nuget, improved handling of special characters.
