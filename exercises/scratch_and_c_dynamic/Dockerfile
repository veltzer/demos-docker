FROM scratch
COPY main /
ADD libc.so.6 /lib/x86_64-linux-gnu/libc.so.6
ADD ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2
CMD ["/main"]
