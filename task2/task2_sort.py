#!/usr/bin/env python

import sys

def takeCount(elem):
    return elem[1];

L = []

# input comes from STDIN
for line in sys.stdin:
      # remove leading and trailing whitespace
      word, count = line.strip().split('\t', 1)
      L.append( (word, int(count) ) )

# sort the tuples
L.sort()

# output the sorted tuples
for (word, count) in L:
    print('%s\t%d' % (word, count) )