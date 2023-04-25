#!/bin/bash

# first lets see who we are...
id
whoami
echo $UID $EUID

if [[ -f "/etc/passwd" ]]
then
	echo "yes, there is a '/etc/passwd' file inside the container"
else
	echo "no, there isn't a '/etc/passwd' file inside the container"
fi

# now lets see that we can write data to a file...
while true
do
	echo "I'm still running and my id is $UID..."
	echo "some more data" >> datafile.txt
	sleep 1
done
