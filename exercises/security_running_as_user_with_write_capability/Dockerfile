FROM bash:latest
RUN mkdir /app_folder
COPY app.sh /app_folder
RUN chown 1000:1000 /app_folder
USER 1000:1000
WORKDIR /app_folder
CMD ["./app.sh"]
# CMD ["ls", "-l"]
