# Write a function fcopy() that takes as input two file names (as strings) and copies
# the content of the first file into the second

import os

def fcopy(src, dest):
    if not os.path.isfile(src):
        print(f'Source file {src} does not exist.')
        return

    with open(src, 'r') as src_file:
        content = src_file.read()

    with open(dest, 'w') as dest_file:
        dest_file.write(content)

    print(f'Content of {src} has been copied to {dest}.')

open('firstfile.txt').read()
open('secondfile.txt').read()
fcopy('firstfile.txt', 'secondfile.txt')
open('secondfile.txt').read()