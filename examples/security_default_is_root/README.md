# Security Default is root

This demo shows that by default docker runs it's process
as root.

To see this you can use:
    $UID
    $EUID
    $USER
    whoami
    id
    ps
    capsh --print
