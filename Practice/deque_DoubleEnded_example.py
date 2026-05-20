# Write a program in Python to implement a Deque (double-ended queue).

class Deque:
    def __init__(self):
        self.deque = []

    # Insert at front
    def insert_front(self, item):
        self.deque.insert(0, item)
        print(f"Inserted at front: {item}")

    # Insert at rear
    def insert_rear(self, item):
        self.deque.append(item)
        print(f"Inserted at rear: {item}")

    # Delete from front
    def delete_front(self):
        if self.is_empty():
            print("Deque is empty. Cannot delete.")
            return None
        return self.deque.pop(0)

    # Delete from rear
    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty. Cannot delete.")
            return None
        return self.deque.pop()

    # Check if empty
    def is_empty(self):
        return len(self.deque) == 0

    # Display deque
    def display(self):
        print("Deque:", self.deque)


# Example usage
d = Deque()

d.insert_front(10)
d.insert_rear(20)
d.insert_front(5)
d.insert_rear(30)

d.display()

print("Deleted from front:", d.delete_front())
print("Deleted from rear:", d.delete_rear())

d.display()
