FROM python:3-alpine
COPY bad_logs.py /
# here we want a shell to allow for the redirections
CMD /bad_logs.py > /dev/null 2> /dev/null
