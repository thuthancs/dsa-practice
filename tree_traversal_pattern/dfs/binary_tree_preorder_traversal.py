# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """preorder traversal: root -> left -> right"""
    output = []

    def dfs(node):
        if not node:
            return
        else:
            output.append(node.val)
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return output
