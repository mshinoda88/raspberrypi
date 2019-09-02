#!/usr/bin/env python3
import subprocess

file_path="./test.jpg"
subprocess.getoutput("raspistill -w 400 -h 300 -o {0} -t 1".format(file_path))

