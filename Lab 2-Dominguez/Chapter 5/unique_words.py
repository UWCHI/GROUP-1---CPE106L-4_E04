""" 
 PROBLEM 04:
 Write a program that inputs a text file. The program should print all of the unique words in the file in alphabetical order.
""" 

import string

def get_unique_words(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read().translate(str.maketrans('', '', string.punctuation)).lower()
            return sorted(set(content.split()))
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []

def main():
    file_name = input("Enter the file name: ")
    words = get_unique_words(file_name)
    if words:
        print("Sorted unique words:")
        print("\n".join(words))

if __name__ == "__main__":
    main()

