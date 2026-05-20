# Write a program in Python to evaluate a postfix expression using a stack.

def evaluate_postfix(expression):
    stack = []

    for char in expression:
        # If operand, push to stack
        if char.isdigit():
            stack.append(int(char))
        else:
            # Pop two operands
            b = stack.pop()
            a = stack.pop()

            # Apply operator
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)

    # Final result
    return stack.pop()


# Example usage
expr = "23*54*+9-"   # ((2*3) + (5*4)) - 9
result = evaluate_postfix(expr)
print("Result:", result)