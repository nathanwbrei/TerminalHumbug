#!/usr/bin/env python
from subprocess import Popen
import sys
 
def say_blocking(msg):
    p = Popen(['say', msg])
    p.communicate()
 
while True:
    say_blocking(sys.stdin.readline())