# Write a program in Python to implement a Singly Linked List with insertion, deletion, and traversal operations.

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
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

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found in list.")
            return

        prev.next = temp.next

    # Traverse (display list)
    def traverse(self):
        temp = self.head
        if temp is None:
            print("List is empty.")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
ll = SinglyLinkedList()

ll.insert_beginning(10)
ll.insert_beginning(5)
ll.insert_end(20)
ll.insert_end(30)

print("Linked List:")
ll.traverse()

ll.delete(20)
print("After deletion:")
ll.traverse()