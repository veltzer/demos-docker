FROM ubuntu
RUN apt-get update -y
RUN apt-get install -y adduser
RUN adduser app1
RUN adduser app2
COPY app1.bash /home/app1
COPY app2.bash /home/app2
RUN chown app1:app1 /home/app1
RUN chown app2:app2 /home/app2
COPY run_two_apps.bash /
CMD ["/run_two_apps.bash"]
