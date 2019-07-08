### Lessons four notes.

Only discussing the differences from the previous lesson.

Iterate over (count over) the lines in the file
object f, count them into a object called num_lines

Line description

10. our file name, we will use one first, then change to two.
13. create an object in memory called num_words
set it's value to 0.
Run the program with python3 on the command line
15. create an list object in memory called 
words to hold a count of the number of words in 
each line we process.
19. Print out a line as it is read in, one by one.
20. Create an object called split_line, call the 
split() function on the object called line using
the dot notation line.split()
21. print out the split_line object
22. calculate the number of items in the list object
split_line using the len function.
23. print out the length using fsting method.
24. Use the append function on the words list object
add the length of the line that was processed.
26. Print out what the words list looks like.
27. Use the sum() function on the words list
print out the Number of words.


Note: you don't need to create the extra object
line_split, it could have been printed like this:hkk

```
print(f'A split line looks like this: \n{line.split()}')
```
but this example is to help people learn so I break things out a bit
to help with the learning.


Run this with

```
python3 three.py
```

Then change the line:

```
file_name = 'input-files/one.txt'
```

to read:

```
file_name = 'input-files/two.txt'
```

Run this again with

```
python3 three.py
```

