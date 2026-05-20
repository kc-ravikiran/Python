# Write a program in Python to implement a Stack using Python lists and perform push, pop, and peek operations.

class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.stack.pop()

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Example usage
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Peek:", s.peek())   # Top element
print("Popped:", s.pop())  # Remove top

s.display()
