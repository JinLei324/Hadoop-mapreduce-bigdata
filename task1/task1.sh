#! /bin/bash
cat 1.txt | ./task1_mapper.py | ./task1_reducer.py > 2.txt
