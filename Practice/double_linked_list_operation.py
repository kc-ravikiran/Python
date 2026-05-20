# Write a program in Python to implement a Doubly Linked List with insertion and deletion operations.

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # If list is empty
        if temp is None:
            print("List is empty.")
            return

        # If head node is to be deleted
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        # Search for the node
        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Value not found.")
            return

        # If node is in between or last
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    # Traverse forward
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Traverse backward
    def traverse_backward(self):
        temp = self.head
        if temp is None:
            return

        # Go to last node
        while temp.next:
            temp = temp.next

        # Traverse backwards
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# Example usage
dll = DoublyLinkedList()

dll.insert_beginning(10)
dll.insert_beginning(5)
dll.insert_end(20)
dll.insert_end(30)

print("Forward Traversal:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()

dll.delete(20)
print("After Deletion:")
dll.traverse_forward()
