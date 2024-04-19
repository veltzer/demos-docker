FROM jenkins/jenkins:latest
# FROM jenkins/jenkins:lts

# Documentation can be found here: https://github.com/jenkinsci/docker/blob/master/README.md

# the next line does not work because the initiall password is created dynamically
# RUN rm /var/jenkins_home/secrets/initialAdminPassword

# install plugins, get the list of plugins by installing a system and then,
# on that system, issuing:
# $ ls /var/jenkins_home/plugins/*.jpi > plugins.txt
# and then removing the .jpi suffix of each line
COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --verbose -f /usr/share/jenkins/ref/plugins.txt

# trying to copy users definitions
COPY --chown=jenkins:jenkins users /var/jenkins_home/users

# restore backup of volume
# USER root:root
# COPY backup.tar.gz /tmp
# RUN tar xvf /tmp/backup.tar.gz -C /var/jenkins_home
# RUN rm /tmp/backup.tar.gz
# USER jenkins:jenkins
