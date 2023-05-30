#!/bin/sh

# ./main.elf

./main.elf &
pid=$!
if wait $pid
then
	echo "It exited successfully"
else
	code=$?
	echo "It exited with failure ($?)"
	# this works only if you add CAP_SYSLOG capability
	dmesg
	# these *** DONT *** work from inside containers by default (without adding software or
	# capabilities that is).
	# dmesg
	# there is no /var/log for log
	# /var/log/{syslog,message} do not exist
	# /proc/meminfo is not correct as it shows the memory of the host and not the containers
	# cat /proc/meminfo
	# there is not journalctl inside the container
	# journalctl -k
	# cat /dev/kmsg
fi
