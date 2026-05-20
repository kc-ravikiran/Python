# # Write a program in Python to reverse a string using slicing.

def reverse_string(text):
    reversed_str = ""
    for char in text:
        reversed_str = char + reversed_str
    return reversed_str

string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))