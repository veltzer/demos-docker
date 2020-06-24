#!/usr/bin/env bash

let i=0

while [[ true ]]
do
	echo "hello, scratch bash ($i)"
	/my_sleep
	let "i=i+1"
done
