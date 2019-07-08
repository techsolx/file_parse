#!/usr/bin/env python3

'''
Open a file, using a context manager,
print out the contents
'''

file_name = 'input-files/one.txt'

with open(file_name, 'r') as f:
    data = f.read()

print(data)
