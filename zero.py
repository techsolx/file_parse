#!/usr/bin/env python3

'''
Open a file,
print out the contents,
close the file.
'''
file_object = open('zero.txt', 'r')
the_contents = file_object.read()
print(the_contents)
file_object.close()
