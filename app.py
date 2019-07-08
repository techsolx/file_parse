#!/usr/bin/env python3

file_name = './input-file.txt'

num_lines = 0
num_words = 0
num_letters = 0

lines = []
words = []
letters = {}

with open(file_name, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)

with open(file_name, 'r') as f:
    for line in f:
        # print(line)
        print(line.split())
        num_words = len(line.split())
        words.append(num_words)

print("Number of words:")
print(sum(words))


with open(file_name, 'r') as f:
    for line in f:
        # print(line)
        print(line.split())
        num_words = len(line.split())
        words.append(num_words)
print("Number of words:")
print(sum(words))


with open(file_name, 'r') as f:
    data = f.read()
    print(len(data))
