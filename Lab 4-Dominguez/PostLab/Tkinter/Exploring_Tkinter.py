
"""
  LAB 04
  PROGRAMMING PROBLEM 02

  Explore the Tkinter.filedialog module to get the name of a text file
"""

import tkinter.filedialog as fd

target = fd.askopenfilename()

if target:                            # Check if a file was selected
    with open(target, 'r') as file:   # Open the selected file in read mode
        for line in file:             # Read and print each line from the file
            print(line, end='')       # Print lines as they are without extra new lines

