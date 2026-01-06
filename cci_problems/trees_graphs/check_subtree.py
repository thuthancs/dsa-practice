def check_subtree(root1, root2):
    """T1 and T2 are two very large binary trees, with T1 much bigger than T2. 
    Create an algorithm to determine if T2 is a subtree of T1.
    A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
    That is, if you cut off the tree at node n, the two trees would be identical.
    
    Algorithm:
    1. Search in tree 1 until reaches the node that is identical to root2
    """
    def matches(node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        elif node1.val != node2.val:
            return False
        return matches(node1.left, node2.left) and matches(node1.right, node2.right)
    
    if root2 is None:
        return True
    if root1 is None:
        return False
    
    if matches(root1, root2):
        return True
    
    return check_subtree(root1.left, root2) or check_subtree(root1.right, root2)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Test Case: T2 is a subtree of T1
# 
# T1 (larger tree):
#          10
#         /  \
#        4    6
#       / \    \
#      1   2    3
#         / \
#        7   8
#
# T2 (subtree):
#        4
#       / \
#      1   2
#         / \
#        7   8

# Build T1
t1 = TreeNode(10)
t1.left = TreeNode(4)
t1.right = TreeNode(6)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(2)
t1.left.right.left = TreeNode(7)
t1.left.right.right = TreeNode(8)
t1.right.right = TreeNode(3)

# Build T2 (should match the left subtree of T1)
t2 = TreeNode(4)
t2.left = TreeNode(1)
t2.right = TreeNode(2)
t2.right.left = TreeNode(7)
t2.right.right = TreeNode(8)

print("Test 1 - T2 is a subtree:", check_subtree(t1, t2))  # Expected: True

# Test Case 2: Same root value but different structure
t3 = TreeNode(4)
t3.left = TreeNode(1)
t3.right = TreeNode(2)
t3.right.left = TreeNode(9)  # Different value here

print("Test 2 - Different structure:", check_subtree(t1, t3))  # Expected: False

# Test Case 3: Empty subtree
print("Test 3 - Empty subtree:", check_subtree(t1, None))  # Expected: True

# Test Case 4: Subtree larger than tree
print("Test 4 - T2 larger than T1:", check_subtree(t2, t1))  # Expected: False

# Test Case 5: Single node match
t4 = TreeNode(3)
print("Test 5 - Single node:", check_subtree(t1, t4))  # Expected: True