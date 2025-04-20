FROM jenkins/jenkins:lts

# USER root
# RUN sudo apt-get install docker.io
# RUN find / -name "jenkins-cli.jar"
# RUN find / -name "jenkins-plugin-manager.jar"
# RUN find / -name "*.jar"
# RUN apt-get install jenkins-cli
# Install Jenkins CLI plugin
# RUN jenkins-cli plugins install http://updates.jenkins-ci.org/latest/jenkins-cli.hpi

# Define your plugins in a file (replace with your actual plugins)
COPY plugins.txt /var/jenkins_home/plugins.txt

# Install plugins during startup
# RUN jenkins-cli plugins install --plugins-from=/var/jenkins_home/plugins.txt
RUN java -jar /opt/jenkins-plugin-manager.jar --plugin-file /var/jenkins_home/plugins.txt
