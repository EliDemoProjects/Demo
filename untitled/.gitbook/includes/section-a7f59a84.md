### Prerequisites

- To run Resolver scans, it is required to have [Syft](https://github.com/anchore/syft/blob/main/README.md) version 0.83.1 installed on the machine where you are running Resolver. Download and install Syft from [https://github.com/anchore/syft/releases/tag/v0.83.1](https://github.com/anchore/syft/releases/tag/v0.83.1).

- If you would like to scan images that are not in your local Dockerfile, you need to have the name and tag for each of the images.

- If you are using a private repo, you need to be authenticated for your registry.

  {% hint style="info" icon="pencil" %}
  Authentication can be done via Docker or Podman.

  Alternatively, you can use the syft login command, as follows: `syft login <private_registry_domain> -u <your_username> -p <your_password>`

  Before running the scan, it is recommended to verify that you are able to access the image on your local machine.
  {% endhint %}
