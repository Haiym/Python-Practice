# The cryptography function crypto() takes as input a string (i.e., the name of a file in
# the current directory). The function should print the file on the screen with this modification:
# Every occurrence of string 'secret' in the file should be replaced with string 'xxxxxx'.

import os

def crypto(filename):
    with open(filename, 'r') as file:
        content = file.read()

    content = content.replace('secret', 'xxxxxx')

    print(content)


crypto('myfile.txt')