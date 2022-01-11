FROM ubuntu:latest
RUN useradd user --uid 1000
RUN mkdir /home/user
COPY app.sh /home/user
RUN chown -R user:user /home/user
USER user
WORKDIR /home/user
CMD ["./app.sh"]
