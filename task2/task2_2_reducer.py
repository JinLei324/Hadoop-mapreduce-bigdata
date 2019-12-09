#!/usr/bin/env python
import sys
import re
#identity reducer...

L={}
i=0 
for line in sys.stdin:
    line = line.strip()
    arg = line.split('\t')
    arg[0]= 3072500 - int(arg[0])    
    if(arg[0] not in L.keys()):
        L[arg[0]]=arg[1]
        if(len(L.keys())<31):
            print ("{0}\t{1}".format(arg[0],arg[1]))