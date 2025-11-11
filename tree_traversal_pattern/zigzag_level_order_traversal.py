# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    output = []
    if not root:
        return output

    q = deque()
    q.append(root)
    left_to_right = True

    while q:
        level = []
        for _ in range(len(q)):
            if left_to_right:
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                node = q.pop()
                level.append(node.val)
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)

        output.append(level)
        left_to_right = not left_to_right
    return output
