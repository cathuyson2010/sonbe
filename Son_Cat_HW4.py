# Task 1: One Potato Two Potato Game
class Node:
    # Represents a member in the game
    def __init__(self, data):
        self.data = data
        self.next = None

def one_potato_two_potato(n, k):
    # Creating a circular linked list with n members
    head = Node(0)
    current = head
    for i in range(1, n):
        current.next = Node(i)
        current = current.next
    current.next = head  # Making the list circular

    # Simulating the game
    while current.next != current:  # While more than one member remains
        for _ in range(k-1):  # Move k-1 steps each round (the kth is the eliminated one)
            current = current.next
        # Eliminate the kth member
        current.next = current.next.next

    # Return the last remaining member's index
    return current.data

# Task 2: Analyzing a Binary Tree
class TreeNode:
    # Represents a node in a binary tree
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_info(node):
    # Function to calculate the height of the tree
    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1

    # Function to count the leaf nodes
    def count_leaves(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return count_leaves(node.left) + count_leaves(node.right)

    # Function to check if the tree is full
    def is_full(node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left and node.right:
            return is_full(node.left) and is_full(node.right)
        return False

    # Function to check if the tree is balanced
    def is_balanced(node):
        if node is None:
            return True, 0
        left_balanced, left_height = is_balanced(node.left)
        right_balanced, right_height = is_balanced(node.right)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return balanced, max(left_height, right_height) + 1

    # Computing tree information
    tree_height = height(node)
    leaf_count = count_leaves(node)
    full = is_full(node)
    balanced, _ = is_balanced(node)

    # Printing the results
    print(f"Height of the tree: {tree_height}")
    print(f"Number of leaf nodes: {leaf_count}")
    print(f"Is Full: {'Yes' if full else 'No'}")
    print(f"Is Balanced: {'Yes' if balanced else 'No'}")

#        3
#       / \
#      9   8
#     / \
#    4   5

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calling tree_info on this tree should print the specified results
tree_info(root)
