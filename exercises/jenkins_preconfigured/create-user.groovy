#!/usr/bin/env groovy

import jenkins.model.*
import hudson.security.*

def jenkins = Jenkins.getInstance()
def user = User.get(env.JENKINS_USER)
if (!user) {
  println "Creating user ${env.JENKINS_USER}"
  user = User.create(env.JENKINS_USER, env.JENKINS_PASS)
  user.save()
} else {
  println "User ${env.JENKINS_USER} already exists"
}
