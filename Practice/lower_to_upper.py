# Write a program in Python to convert lowercase characters to uppercase and vice versa in a string.

# Program to swap case of characters in a string

input_string = input("Enter a string: ")
result = ""

for char in input_string:
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char   # for spaces, numbers, symbols

print("Converted string:", result)


# Program using built-in function

#input_string = input("Enter a string: ")
# result = input_string.swapcase()

# print("Converted string:", result)