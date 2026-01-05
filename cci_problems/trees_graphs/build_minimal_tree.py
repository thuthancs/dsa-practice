class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def build_minimal_tree(arr: list):
    """Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
       to create a binary search tree with minimal height.

    Input: strictly increasing-sorted array of unique integers. E.g.: [1, 2, 3, 4, 5]
    Output: object (a BST with minimal height)

    Understand:
    - A BST is a binary tree (e.g., a tree where each parent has at most 2 children) where on all levels, the left child < parent and right child > parent
    - A BST with minimal height is a balanced BST where the ideal scenario is where each parent node has 2 children
    - We can take advantage of the strictly increasing order array to build out the tree -> use binary search algorithm

    Algorithm:
    - Initialize a tree object: root = Node()
    - Start with the mid_idx = (l + r) // 2
    - Set the mid index as the root node: root.val = arr[mid_idx]
    - Recursively build the left subtree and right subtree:
        - root.left = call the same function with the new left and right pointers to cut off the left half (r = mid - 1, l is the same)
        - root.right = call the same function with the new left and right pointers to cut off the right half (l = mid + 1, r is the same)
    - Return root
    """

    def build_tree(arr, l, r):
        if l > r:
            return None
        mid_idx = (l + r) // 2
        node = Node(arr[mid_idx])
        node.left = build_tree(arr, l, mid_idx - 1)
        node.right = build_tree(arr, mid_idx + 1, r)
        return node

    l, r = 0, len(arr) - 1
    return build_tree(arr, l, r)


def print_tree(node, level=0, prefix="Root: "):
    """Print tree structure"""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left or node.right:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


arr = [1, 2, 3, 4, 5]
root = build_minimal_tree(arr)
print_tree(root)
