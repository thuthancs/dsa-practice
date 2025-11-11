# Definition for a Node.
class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


def preorder(root: "Node") -> List[int]:
    # root -> left -> right
    output = []

    def dfs(node):
        if not node:
            return
        else:
            output.append(node.val)
            if node.children:
                for child in node.children:
                    dfs(child)

    dfs(root)
    return output
