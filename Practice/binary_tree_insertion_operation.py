# Write a program in Python to implement a Binary Tree. The program should also provide for insertion operation.

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert using level-order (BFS)
    def insert(self, data):
        new_node = Node(data)

        # If tree is empty
        if self.root is None:
            self.root = new_node
            return

        queue = []
        queue.append(self.root)

        while queue:
            temp = queue.pop(0)

            # Insert as left child
            if temp.left is None:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            # Insert as right child
            if temp.right is None:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # Inorder Traversal (Left → Root → Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# Example usage
bt = BinaryTree()

bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

print("Inorder Traversal:")
bt.inorder(bt.root)
