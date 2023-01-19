#!/usr/bin/env bash

function handle_sigint() {
	echo "killing my kids..."
	kill -9 $PID1 $PID2
}

trap handle_sigint INT

./app1.bash &
PID1=$!
./app2.bash &
PID2=$!
wait $PID1
wait $PID2
