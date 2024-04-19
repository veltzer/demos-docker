import jenkins.model.*
import hudson.security.*

def instance = Jenkins.getInstance()

def hudsonRealm = new HudsonPrivateSecurityRealm(false)
hudsonRealm.createAccount(
	System.getenv("JENKINS_USER"),
	System.getenv("JENKINS_PASS"),
)
instance.setSecurityRealm(hudsonRealm)

def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
instance.setAuthorizationStrategy(strategy)

jenkinsUrl = System.getenv("JENKINS_URL")
def locationConfig = JenkinsLocationConfiguration.get()
locationConfig.setUrl(jenkinsUrl)

// Recommended to not run builds on the built-in node
instance.setNumExecutors(0)

instance.save()
