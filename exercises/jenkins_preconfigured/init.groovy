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

instance.setRootUrl(System.getenv("JENKINS_URL"))

instance.save()
