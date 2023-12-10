- build a webserver in docker built on python + flask.
	* you can find examples like these all over the web
	* you will also need to make sure the flask module is installed.
- use port 8080 since that's the only port that is opened for the machine
	you have on AWS. (this doesnt matter if you are not exercising on AWS).
- you will need to install the 'flask' python module. You do that using
	$ pip install flask
- you will need to make sure your port 8080 is open and exposed to the outside
	work.
	In order to open your network to be able to access docker you will need:
	$ docker run --network ...
	or
	$ docker run -p ...
- access you webserver via:
	http://[your_ip]:8080/
