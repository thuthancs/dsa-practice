class BT:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def validate_bst(root):
    """Implement a function to check if a binary tree is a binary search tree.

    Input: root (the root node of a binary tree)
    Output: boolean (T/F)

    Brainstorm: Every subtree has to be a BST (left < parent and parent < right) -> DFS

    Algorithm:
    - Start with the root node
    - If node.left and node.right:
        - Check if node.val > node.left.val and node.val < node.right.val:
            - If yes, return True
            - Else, return False
    """

    def is_valid(node, min_val, max_val):
        if node is None:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (is_valid(node.left, min_val, node.val)) and (
            is_valid(node.right, node.val, max_val)
        )

    return is_valid(root, float("-inf"), float("inf"))


rootA = BT(3)
rootB = BT(1)
rootC = BT(8)
rootD = BT(0)
rootE = BT(2)
rootF = BT(5)
rootA.left = rootB
rootA.right = rootC
rootB.left = rootD
rootB.right = rootE
rootC.right = rootF

print(validate_bst(rootA))
