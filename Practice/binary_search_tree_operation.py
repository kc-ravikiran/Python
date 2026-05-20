# Write a program in Python to implement a Binary Search Tree (BST) with insertion, deletion, and search operations.

# Node class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# BST class
class BST:
    def __init__(self):
        self.root = None

    # Insert operation
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        return root

    # Search operation
    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Find minimum value node (used in deletion)
    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    # Delete operation
    def delete(self, root, key):
        if root is None:
            return root

        # Traverse the tree
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    # Inorder traversal (sorted output)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


# Example usage
bst = BST()

# Insert elements
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.root = bst.insert(bst.root, v)

print("Inorder traversal (sorted):")
bst.inorder(bst.root)

# Search element
key = 40
result = bst.search(bst.root, key)
print("\nSearch:", key, "found" if result else "not found")

# Delete element
bst.root = bst.delete(bst.root, 50)

print("After deletion of 50:")
bst.inorder(bst.root)