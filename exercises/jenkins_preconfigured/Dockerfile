FROM jenkins/jenkins:lts
USER root:root
COPY backup.tar.gz /tmp
RUN tar xvf /tmp/backup.tar.gz -C /var/jenkins_home
RUN rm /tmp/backup.tar.gz
USER 1000:1000
