class BT:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_balanced(root):
    """Implement a function to check if a binary tree is balanced. For the purposes of
       this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
       node never differ by more than one.

    Input: root (root node object of a binary tree)
    Output: boolean (T/F)
    abs(height(left subtree) - height(right subtree)) <= 1: balanced
    The height of each subtree is calculated as the number of edges from root node to leaf node

    Algorithm: DFS to compute the height
    1. Start with the root node
    2. Recursively compute the left subtree and right subtree height:
        - Base case: when the node is the leaf node (node.left and node.right are None) -> height = 0
        - Else: add 1 to the subtree's height
    3. If diff > 1: return False else return True
    """
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))
    
    if root is None:
        return True

    l_height = height(root.left)
    r_height = height(root.right)
    
    if abs(l_height - r_height) > 1:
        return False
    
    return check_balanced(root.left) and check_balanced(root.right)

rootA = BT(3)
rootB = BT(1)
rootC = BT(4)
rootD = BT(0)
rootE = BT(2)
rootF = BT(5)
rootA.left = rootB
rootA.right = rootC
rootC.right = rootF
rootF.left = rootD
rootF.right = rootE

print(check_balanced(rootA))