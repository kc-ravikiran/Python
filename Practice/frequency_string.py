# Write a program in Python to compute the frequency of each word in a given text using a dictionary.

# Program to count frequency of words in a string using dictionary

text = input("Enter a sentence: ")

# Convert text to lowercase and split into words
words = text.lower().split()

# Create an empty dictionary
word_count = {}

# Count frequency
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display result
print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)
