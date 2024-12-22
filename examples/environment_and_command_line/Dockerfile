FROM python:3-alpine
COPY app.py /
ENV MARK veltzer
# ENTRYPOINT will not allow command line arguments
# ENTRYPOINT "/app.py"
# CMD can add command line argument and you can even overwrite them at "docker run" time.
CMD [ "/app.py", "with", "arguments" ]
