# Label the program written in problem 4 with comments. 

#rewrite the 4th orgram with comments.

import os

# Replace 'your_directory_path' with the path of the directory you want to list
directory_path = '/'

try:
    # List all files and directories in the specified path
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
