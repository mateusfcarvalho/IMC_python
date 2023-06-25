FROM jenkins/jenkins:lts

USER root

# Instalar Python e npm
RUN apt-get update \
    && apt-get install -y python3 python3-pip npm \
    && apt-get clean


ENV JENKINS_OPTS="--httpPort=8888"

USER jenkins

EXPOSE 8888

# Executar o Jenkins
CMD ["/usr/local/bin/jenkins.sh"]
