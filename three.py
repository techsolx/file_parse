#!/usr/bin/env python3

''' Open a file, count the number
of lines in that file.
'''

file_name = 'input-files/two.txt'
num_lines = 0

with open(file_name, 'r') as f:
    for line in f:
        num_lines += 1

print(f'Number of lines: {num_lines}')
