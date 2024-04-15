FROM jenkins/jenkins:lts
# the next line does not work because the initiall password is created dynamically
# RUN rm /var/jenkins_home/secrets/initialAdminPassword

# restore backup of volume
# USER root:root
# COPY backup.tar.gz /tmp
# RUN tar xvf /tmp/backup.tar.gz -C /var/jenkins_home
# RUN rm /tmp/backup.tar.gz
USER jenkins:jenkins
