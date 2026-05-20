# Write a program in Python to implement a Queue using two stacks.

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue

    # Enqueue operation
    def enqueue(self, item):
        self.stack1.append(item)
        print(f"Enqueued: {item}")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        # Move elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    # Check if queue is empty
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    # Display queue
    def display(self):
        # Front elements are in stack2 (reversed), then stack1
        print("Queue:", self.stack2[::-1] + self.stack1)


# Example usage
q = QueueUsingStacks()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued:", q.dequeue())
q.display()
