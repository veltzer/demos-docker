FROM mysql:latest

COPY custom.cnf /etc/mysql/conf.d

COPY init.sh /docker-entrypoint-initdb.d/
