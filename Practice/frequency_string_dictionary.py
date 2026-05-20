# Write a program in Python to compute the frequency of each word in a given text using a dictionary.

text = input("Enter a sentence: ")
words = text.lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)