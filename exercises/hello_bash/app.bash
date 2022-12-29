#!/usr/bin/env bash

let i=0

while true
do
	echo "hello, bash ($i)"
	sleep 1
	let "i=i+1"
done
