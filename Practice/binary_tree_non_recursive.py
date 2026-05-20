# Write a program in Python that includes non-recursive preorder, inorder and postorder traversals of a Binary Tree.

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder Traversal (Root -> Left -> Right)
def preorder_iterative(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data, end=" ")

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Inorder Traversal (Left -> Root -> Right)
def inorder_iterative(root):
    stack = []
    current = root

    while stack or current:
        # Reach the leftmost node
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")

        current = current.right


# Postorder Traversal (Left -> Right -> Root)
def postorder_iterative(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        # Push left and right children
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # Print postorder
    while stack2:
        print(stack2.pop().data, end=" ")


# Example usage
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print("Preorder (Iterative):")
preorder_iterative(root)

print("\nInorder (Iterative):")
inorder_iterative(root)

print("\nPostorder (Iterative):")
postorder_iterative(root)
