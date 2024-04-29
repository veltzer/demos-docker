# MySQL reconfigured

MySQL official image (MySQL:latest) is by default is configured with general log turned off.

Create an image of MySQL which is configured with the log turned on.
Make that log be visible through the docker logging system:

```bash
    $ docker logs -f [container_name]
```
