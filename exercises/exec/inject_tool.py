#!/usr/bin/python3

import sys
import subprocess

tool_to_inject=sys.argv[1]
container=sys.argv[2]
output = subprocess.check_output([
    "ldd",
    tool_to_inject,
]).decode()
for line in output.split("\n"):
    if "=>" not in line:
        continue
    lib=line.split("=>")[1].strip().split(" ")[0]
    # print(lib)
    subprocess.check_call([
        "echo",
        "docker",
        "cp",
        "-L",
        lib,
        f"{container}:{lib}",
    ])
subprocess.check_call([
    "echo",
    "docker",
    "cp",
    "-L",
    f"{tool_to_inject}",
    f"{container}:{tool_to_inject}",
])
