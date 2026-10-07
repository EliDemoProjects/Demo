# passiveScan-wait

## Description

This job waits for the passive scanner to finish scanning the requests and responses in the current queue. You should typically run this job after the jobs that explore your application, such as the spider jobs or those that import API definitions. If any more requests are sent by the engine or proxied after this job has run then they will be processed by the passive scanner. You can run this job as many times as you need to.

## Jobs structure

```
 - type: passiveScan-wait            
    parameters:
      maxDuration: 5                   
```

## Possible parameters

Glossary

[maxDuration: \<int\>](passivescan-wait.md#UUID-f69915f1-29d3-2685-8cec-8e231cdae59f_N6565ef8c2ac79) (Default - 0 is unlimited)

Max time to wait for the passive scanner.

| Name | Description | Type / Default |
| --- | --- | --- |
| `maxDuration:` | `Max time to wait for the passive scanner` | Int, default: 0 unlimited |
