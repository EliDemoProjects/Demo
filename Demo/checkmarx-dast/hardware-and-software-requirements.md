# Hardware and Software Requirements

This page details the hardware and software requirements to run DAST in your environment.

## Recommendations and Limitations

This section lists requirements and recommendations for hardware and configurations

### Hardware Requirements and Recommendations When Running DAST CLI

The following hardware configurations are required or recommended:

Minimum Requirements

- RAM: 8GB-16GB

- The number of CPUs will depend on the level of concurrency control applied to the various jobs:

  Each DAST CLI worker should have 3 GB and 2 CPUs available.

  Example setups:

  - Set a virtual Linux machine with 16GB and 4 VCPU.
  - Set two Checkmarx One-workers with a limit of 3GB and 2 VCPUs.

### Operating System

Run the DAST CLI in any operating system that supports Docker, such as Windows, MacOS, and Linux.

### Limitations

Performance

- For very large environments (1000+ URLs), it is recommended to use filters (on the configuration file) or increase overall system/environment resources to avoid abnormal CPU consumption on the database.

General

- When running from Checkmarx One, DAST has a time-out limit of two hours and forty-five minutes. Running DAST from a pipeline is recommended if more time is needed.
- DAST has a 150MB zip file limit for uploading the results into Checkmarx One.
