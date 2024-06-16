# Health Check exercise

Bring up two apps using docker compose.

Make the first app start with a delay.

Use the docker health check feature to know when the first app is up.

There are two ways to use the health check:
* the container can explain to docker how to health check itself.
* we can explain to docker(/compose) how to health check the container in the `docker compose.yml` file.

In both cases you must state that you depend on the container with a state of healthy and not just depend
on the container.

Number 1 is better for obvious reasons.

See that the second one is brought up only after the first one is healthy.

look at the logs using:

```bash
docker compose logs
```

## References
- [link](https://docs.docker.com/reference/dockerfile/#healthcheck)
