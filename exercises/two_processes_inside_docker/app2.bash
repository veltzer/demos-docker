#!/usr/bin/env bash

let i=0
while [[ true ]]
do
	echo "hello, from app 2 ($i)"
	sleep 1
	let "i=i+1"
done
