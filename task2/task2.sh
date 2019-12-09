#! /bin/bash

cat 1.txt | ./task2_mapper.py | ./task2_reducer.py | ./task2_2_mapper.py| ./task2_sort.py | ./task2_2_reducer.py > 3.txt
