# Write a program in Python to replace multiple consecutive blanks in a string with a single blank.

# Input string from user
text = input("Enter a string: ")

# Replace multiple spaces with a single space
result = ' '.join(text.split())

# Display result
print("Updated string:")
print(result)