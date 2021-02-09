#!/bin/bash
while [[ true ]]
do
	echo "I'm still running and my id is $UID..."
	echo "some more data" >> datafile.txt
	sleep 1
done
