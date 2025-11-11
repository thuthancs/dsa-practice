# Definition for a Node.
class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


def postorder(root: "Node") -> List[int]:
    output = []

    def dfs(node):
        if not node:
            return
        else:
            if node.children:
                for child in node.children:
                    dfs(child)
            output.append(node.val)

    dfs(root)
    return output
