""" 
 PROBLEM 05:
A file concordance tracks the unique words in a file and their frequencies. Write a program that displays a concordance for a file. 
The program should output the unique words and their frequencies in alphabetical order.
""" 

import string

def create_concordance(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        words = cleaned_text.split()
        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1
        sorted_words = sorted(word_frequency.items())
        print("Word Concordance:")
        for word, frequency in sorted_words:
            print(f"{word}: {frequency}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    create_concordance(filename)
