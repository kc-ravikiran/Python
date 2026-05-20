# Write a program in Python to reverse a string using slicing.

# Function to reverse string
def reverse_string(text):
    return text[::-1]

# Input from user
string = input("Enter a string: ")

# Function call
result = reverse_string(string)

# Output
print("Reversed string:", result)