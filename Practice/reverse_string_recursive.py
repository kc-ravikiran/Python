# Write a recursive Python function to reverse a string.

def reverse_string(s):
   
    if len(s) <= 1:
        return s
    
   
    return reverse_string(s[1:]) + s[0]



text = "hello"
print(reverse_string(text))  # Output: "olleh"