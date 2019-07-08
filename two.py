#!/usr/bin/env python3

'''
Open a file, using a context manager,
load that into an object called data
count the number of characters by calculating
the length using the len function.
Print out the information using fstrings

'''

file_name = 'input-files/two.txt'

with open(file_name, 'r') as f:
    data = f.read()
    length = len(data)

print(f'Data object is: \n{data}')
print(f'Number of characters: {length}')
