# Write a recursive function to compute the product of two integers using only addition.

def multiply(a, b):
   
    if b == 0:
        return 0
    
    if b < 0:
        return -multiply(a, -b)
   
    return a + multiply(a, b - 1)

print(multiply(3, 0))   
print(multiply(4, -2))  