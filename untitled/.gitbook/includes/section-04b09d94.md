### Running a Container Scan on a Specific Image

1. Add the `--scan-containers` flag to the SCA Resolver scan command.

2. If you want to scan only specific images (not an entire project), do the following:

   1. Create a "dummy" folder in your project (for use in the `-s` parameter) and give it a name that indicates that it is used for scanning images, e.g., scan_ecr_image.
   2. In the Resolver scan command, for the `-s` parameter give the path to the "dummy" folder that you created, e.g., `/Users/DemoUser/scan_ecr_image`.

3. Add the `--images` flag followed by a comma separated list of images. Specify each image using the following syntax {image_name}:{image_tag}.

Example of scanning a specific image:

The following example shows a command to run a container scan on specific images.

{% tabs %}
{% tab title="Linux/MacOS" %}
```
./ScaResolver -s /Users/DemoUser/scan_ecr_image -n DemoImageScan -a Checkmarx -u jack -p 'demo123!' --scan-containers --images “debian:11, alpine:latest”
```
{% endtab %}
{% tab title="Windows" %}
```
./ScaResolver.exe -s C:\Users\DemoUser\scan_ecr_image -n DemoImageScan -a Checkmarx -u jack -p "demo123!" --scan-containers --images “debian:11, alpine:latest”
```
{% endtab %}
{% endtabs %}
