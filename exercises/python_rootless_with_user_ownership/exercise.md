Create a python app that writes some data to disk periodically
=======================================
with open("datafile.txt") as f:
	while True:
		f.write("some data")
		time.sleep(1)
=======================================
Also make sure that the application prints it's user id with the following code:
=======================================
	import os
	print(f"my user id is {os.getuid()}")
=======================================
Create a docker image with python on it
Add you application to the image in a way that will allow it to run
*** NOT *** as a the root user.

Demonstrate that it works.
