# Write a program in Python to count the number of words, blanks, characters in input string.

# Input string from user
text = input("Enter a string: ")

# Count characters (including spaces)
characters = len(text)

# Count words
words = len(text.split())

# Count blanks (spaces)
blanks = text.count(" ")

# Display results
print("Number of characters:", characters)
print("Number of words:", words)
print("Number of blanks:", blanks)