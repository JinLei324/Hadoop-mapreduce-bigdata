#!/usr/bin/env python
 
import sys
import re

for line in sys.stdin:
    line = line.strip()
    arg = line.split('\t')
    arg[1]=3072500-int(arg[1])
    print ("{0}\t{1}".format(arg[1], arg[0]))