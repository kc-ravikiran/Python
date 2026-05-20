def main():
    print("Welcome to the Python Program!")
    print("This program demonstrates formatted output.")
    print()
    print("Here are some examples:")
    print("-" * 40)
    print("1. Simple text output")
    print("2. Numbers and calculations:")
    print(f"   5 + 3 = {5 + 3}")
    print(f"   12 / 4 = {12 / 4}")
    print("3. Loop output:")
    for i in range(1, 6):
        print(f"   Line {i}")
    print("4. Special characters:")
    print("   Tab\tSeparated\tValues")
    print("   New\nLine\nExample")
    print("-" * 40)
    print("End of program. Have a great day!")

if __name__ == "__main__":
    main()
