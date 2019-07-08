## Parse Me

### Idea

Using Python3,
practice opening a file,

Start with a file using context manager
A context manager in Python is a common pattern
that is used to open files.
It allows for errors in opening the file 
without damaging the file.



### Lessons one, one.py

Line description
1. Hashbang, allows this file to be run on linux, mac, as a stand alone program.
Also let's the 'editor' know how to handle this file.
2. Blank line to break up the code and make it easiser to read.
Use one line between code segments, 2 before functions and classes.
3. Open a multi line comment with '''
4. & 5. are the comment
6. Close the multi line comment with '''
7. Blank line
8. Create an object in memory called file_name
assign that object a string called 'input-files/one.txt'
9. Blank line
10. Using a context manager, open a file object for reading 'r', 
name that file object f.
It is good practice to use the with keyword when dealing with file objects. The
advantage is that the file is properly closed when the with block finishes, even if
an exception is raised at some point.
11. create an object in memory called data, call the read() method on the 
file object 'f' with f.read()
This reads the entire file object.
12. Blank 
13. Call the print function to print it to the screen.
