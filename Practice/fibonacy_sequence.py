# Write a program in Python to generate the Fibonacci sequence up to n terms (both iterative and recursive versions).

# Iterative Fibonacci

# n = int(input("Enter number of terms: "))

# a, b = 0, 1

# if n <= 0:
#     print("Please enter a positive number")
# else:
#     print("Fibonacci Sequence:")
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
        
   # Recursive Fibonacci function

def fibonacci(n):
    if n <= 1:   # Base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input
n = int(input("\nEnter number of terms: "))

if n <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci Sequence:")
    for i in range(n):
        print(fibonacci(i), end=" ")
     
        