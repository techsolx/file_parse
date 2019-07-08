#!/usr/bin/env python3

'''
Open a file, count the number
of words in that file using a
space as a delimeter between character
groups.
'''

file_name = 'input-files/one.txt'

num_lines = 0
num_words = 0

words = []

with open(file_name, 'r') as f:
    for line in f:
        print(f'A line looks like this: \n{line}')
        split_line = line.split()
        print(f'A split line looks like this: \n{split_line}')
        length = len(split_line)
        print(f'The length of the split line is: \n{length}')
        words.append(length)
        print(f'Words now looks like this: \n{words}')

print(f'Number of words: \n{sum(words)}')
