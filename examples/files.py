"""
Reading and writing from files.
"""

# We `open` a file to work with it. We use a `with` to do it so that
# the file is properly close after we are done with it.

# We can read a file whole, or we can read it line by line.

# What we can do with a file depends out how its open, we can open a file as read only or we can open

# Modes we can open a file in:
# r   (default) Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
# rb  Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.
# r+  Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
# rb+ Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
# w   Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# wb  Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# w+  Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
# wb+ Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
# a   Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# ab  Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# a+  Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# ab+ Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

# First let me show a working example, and then I can dive into the details about the different parts.

# By default a file is open with `r` which means read only mode.

# This import is just need for the try except, and try
# excepts are optional
from io import UnsupportedOperation

try:
    with open('local_importing/data/example_data.csv') as file_obj:
        # Now we have a file object we can work with:
        all_text = file_obj.read()
        print(all_text)
        file_obj.write("a,b,c,e") # This will raise an exception
except FileNotFoundError:
    print("File at the given path could not be found.")
except UnsupportedOperation:
    print("Tried to write to a file that is read-only.")
    

file_obj = None
try:
    file_obj = open('local_importing/data/example_data.csv')
    # Now we have a file object we can work with:
    all_text = file_obj.read()
    print(all_text)
    file_obj.write("a,b,c,e") # This will raise an exception
except FileNotFoundError:
    print("File at the given path could not be found.")
except UnsupportedOperation:
    print("Tried to write to a file that is read-only.")
finally:
    if file_obj:
        file_obj.close()

# Is the same as

with open("<<Path to file relative to entrypoint") as file_obj:
    
    
    with open('local_importing/data/example_data.csv', 'w+'):pass

    with open('local_importing/data/example_data.csv', 'rb+'): pass

    with open('local_importing/data/example_data.csv', 'r'): pass


# Writing text to a file.
text_to_write = "Line One\nLine Two\nLine Three"
with open('files_example.txt', 'w+') as file_obj:
    file_obj.write(text_to_write)
print("File contents written (file created).")

print("----------------------------------------")

# Read text as a whole
with open('files_example.txt') as file_obj:
    read_text = file_obj.read()
    print("Does the read text match the text written:",
          read_text == text_to_write)

print("----------------------------------------")

# Read a text file line by line. (Best for reading massive files)
with open('files_example.txt') as file_obj:
    for line_no, line in enumerate(file_obj):
        print(f"Line {line_no + 1}: {line}")

print("----------------------------------------")
