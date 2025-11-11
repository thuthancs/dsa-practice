# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    # post-order: left -> right -> root
    output = []

    def dfs(node):
        if not node:
            return
        else:
            dfs(node.left)
            dfs(node.right)
            output.append(node.val)

    dfs(root)
    return output
