age = int(input("Enter your age: "))

if age<=20:
    print("Below 20")
    print(age+10)
elif age<=40:
    print("21-40")
elif age<=60:
    print("41-60")
else:
    print("Above 60")