#!/usr/bin/python

"""
This script checks the syntax of other python scripts.
It returns a bad error code to the parent if something goes wrong.

It's basically a more sophisticated version of something like this:
    python2 -m py_compile $< || python3 -m py_compile $<
"""

import sys
import subprocess

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} [filename]", file=sys.stderr)
    sys.exit(1)

filename = sys.argv[1]

# read the first line of the file
check_with = None
with open(filename, 'r') as f:
    for line in f:
        line = line.rstrip()
        if line == '#!/usr/bin/python2':
            check_with = 'python2'
            break
        if line == '#!/usr/bin/python3':
            check_with = 'python3'
            break
        if line.startswith('# CHECK_WITH'):
            check_with = line.split()[2]
            break
# check with python3 if in doubt
if check_with is None:
    check_with = 'python3'

if check_with is None:
    print(f"{sys.argv[0]}: could not find how to check file [{filename}]", file=sys.stderr)
    sys.exit(1)

# check the syntax
out = subprocess.check_output([
    check_with,
    '-m',
    'py_compile',
    filename,
]).decode()
# check that there is no output
if out != "":
    print(f"out is [{out}]")
    sys.exit(1)
