#!/usr/bin/env bash
id
whoami
echo "UID is $UID and EUID is $EUID"
/sbin/capsh --print
ps -ef
# this does not work anyway...
# which reboot
# echo "are you ready for a reboot????..."
# sleep 5
# reboot
