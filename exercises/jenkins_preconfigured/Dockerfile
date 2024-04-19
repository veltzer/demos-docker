FROM jenkins/jenkins:latest
# FROM jenkins/jenkins:lts

# Documentation can be found here: https://github.com/jenkinsci/docker/blob/master/README.md

# install plugins, get the list of plugins by installing a system and then,
# on that system, issuing:
# $ ls /var/jenkins_home/plugins/*.jpi > plugins.txt
# and then removing the .jpi suffix of each line
COPY --chown=jenkins:jenkins plugins_docker_k8s_ocean.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --verbose -f /usr/share/jenkins/ref/plugins.txt

# don't run the setup wizard and have constant user and password
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
ENV JENKINS_USER="admin"
ENV JENKINS_PASS="admin"
ENV JENKINS_URL="http://localhost:8080"
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/init.groovy
