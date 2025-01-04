# Programming Problem 01: Count number of lines in a file
try:
    # Open the file in read mode ('r') to ensure no accidental changes are made
    file = open('myfile.txt', 'r')
    count = 0
    for line in file:  # Iterate over each line in the file to count the total number
        count += 1
    print("The number of lines in the file:", count)
    file.close()  # Close the file to release resources
except FileNotFoundError:
    print("Error: The file 'myfile.txt' does not exist.")

# --------------------

# Programming Problem 02: Count four-letter words in a file
try:
    # Open the file in read mode ('r') to read its content
    file = open('myfile.txt', 'r')
    words = file.read().split()  # Split the content into a list of words
    count = 0
    for word in words:  # Loop through each word
        if len(word) == 4:  # Check if the word has exactly four characters
            count += 1
    print("The number of four-letter words in the file:", count)
    file.close()  # Close the file to free resources
except FileNotFoundError:
    print("Error: The file 'myfile.txt' does not exist.")

# --------------------

# Programming Problem 03: Calculate the average of integers in a file
try:
    # Open the file in read mode ('r') for processing integers
    file = open('numbers.txt', 'r')
    total = 0
    count = 0
    for line in file:  # Loop through each line in the file
        if line.strip().isdigit():  # Check if the line contains a valid integer
            total += int(line.strip())  # Add the integer to the total
            count += 1
    if count > 0:  # Avoid division by zero
        average = total / count  # Calculate the average
        print("The average of the integers in the file:", average)
    else:
        print("No integers found in the file.")
    file.close()  # Close the file after processing
except FileNotFoundError:
    print("Error: The file 'numbers.txt' does not exist.")
except ValueError:
    print("Error: The file contains non-integer values.")

# --------------------

# Programming Problem 04: List names of items in the current directory
import os
# Use os.listdir to get all items (files and directories) in the current folder
items = os.listdir('.')
print("Items in the current directory:")
for item in items:  # Print each item one by one
    print(item)

# --------------------

# Programming Problem 05: Print contents of a file or show an error message
filename = input("Enter the filename: ")
try:
    # Open the specified file in read mode ('r')
    file = open(filename, 'r')
    content = file.read()  # Read and store the file's content
    print(content)  # Print the file's content
    file.close()  # Close the file to release system resources
except FileNotFoundError:
    print("Error: The file '", filename, "' does not exist.", sep='')
