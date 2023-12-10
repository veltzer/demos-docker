- create a python app that receives:
	- a name
	- an interval
	and once every interval opens a constant filename and appends a line
	to the file with it's name.
	* find example in the folder of this exercise.
	See how it runs outside docker.
- package the app in a docker image.
- run two containers based on that image and make sure both containers
	write to *THE SAME FILE* by using the --volume flag to "docker run"
	and sharing a folder between them.
- on the host, observe the file changes using:
	$ tail -f [filename]
