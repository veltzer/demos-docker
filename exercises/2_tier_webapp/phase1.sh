#!/bin/bash -eux

export MYSQL_ROOT_PASSWORD=pass
if docker container inspect mysql > /dev/null
then
	docker kill mysql > /dev/null || true
	docker rm mysql > /dev/null || true
fi
docker run --name mysql --detach --network host -e MYSQL_ROOT_PASSWORD mysql:latest > /dev/null
sleep 10
mysql --defaults-file=mysql.conf --protocol tcp <<FINISH
CREATE DATABASE foo;
USE foo;
CREATE TABLE bar (value int);
INSERT INTO bar (value) VALUES(2);
INSERT INTO bar (value) VALUES(3);
INSERT INTO bar (value) VALUES(5);
INSERT INTO bar (value) VALUES(8);
SELECT * FROM bar;
FINISH
