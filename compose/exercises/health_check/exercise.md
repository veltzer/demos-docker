# Health Check exercise

Bring up two apps using docker compose.

Make the first app start with a delay.

Use the docker health check feature to know when the first app is up.

Make the second app depend on the health check of the first one.

See that the second one is brought up only after the first one is healthy.

## References
- [link](https://docs.docker.com/reference/dockerfile/#healthcheck)
