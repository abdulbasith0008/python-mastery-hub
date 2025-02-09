'''Write a python program to print the contents of a directory using the os module.
Search online for the function which does that. '''

import os


directory_path = '/'

try:
    
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except NotADirectoryError:
    print(f"The path '{directory_path}' is not a directory.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
