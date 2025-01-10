""" 
 PROBLEM 03:
 Modify the sentence-generator program of Case Study 5.3:
•	METIS book: 9781337671019, page 150. 
•	Python source code: generator.py

so that it inputs its vocabulary from a set of text files at startup. The filenames are nouns.txt, verbs. txt, articles.txt, and prepositions.txt. (Hint: Define a single new function, getWords.
This function should expect a filename as an argument. The function should open an input file with this name, define a temporary list, read words from the file, and add them to the list. 
The function should then convert the list to a tuple and return this tuple. Call the function with an actual filename to initialize each of the four variables for the vocabulary
""" 

import random

def getWords(filename):
    try:
        with open(filename, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return tuple(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return tuple()

def sentence():
    articles = getWords("articles.txt")
    nouns = getWords("nouns.txt")
    verbs = getWords("verbs.txt")
    prepositions = getWords("prepositions.txt")
    if not (articles and nouns and verbs and prepositions):
        return "Error: Missing or empty vocabulary files."
    noun_phrase = f"{random.choice(articles)} {random.choice(nouns)}"
    verb_phrase = f"{random.choice(verbs)} {random.choice(prepositions)} {random.choice(articles)} {random.choice(nouns)}"
    return f"{noun_phrase.capitalize()} {verb_phrase}."

def main():
    try:
        number = int(input("Enter the number of sentences to generate: "))
        for _ in range(number):
            print(sentence())
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
