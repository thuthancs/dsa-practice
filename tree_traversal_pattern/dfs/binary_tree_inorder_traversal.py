# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """inorder: left -> root -> right"""
    output = []

    def dfs(node):
        if not node:
            return
        else:
            dfs(node.left)
            output.append(node.val)
            dfs(node.right)

    dfs(root)
    return output
