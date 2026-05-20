#### Example 1: Write a python code to check whether an user is eligible to vote or not 
##### (Note: People with age 18+ are allowed to vote and others are not)

age = int(input("Enter your age: "))

if age>=18:
    print("You are eligible to vote")
else:
    print("OOPS!! You are not allowed to vote")