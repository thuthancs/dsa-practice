from collections import deque


class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None


def list_of_depths(root):
    """Given a binary tree, design an algorithm which creates a linked list of all the nodes
       at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

    Input: root (object) - the root node of a binary tree (eg, a tree where each parent node has at most 2 children nodes)
    Output: an array of linked lists
            each linked list has the first node as the farthest left node of that level
    Root: 3
    L--- 1
        L--- None
        R--- 2
    R--- 4
        L--- None
        R--- 5
    Output: [3 -> None, 1 -> 4 -> None, 2 -> 5 -> None]

    Algorithm: BFS (traverse level by level) using a queue
    - Create a helper function to build the linked list (level_nodes):
        - root = Node(level_nodes[0])
        - for node in range(1, len(level_nodes)):
            - root.next = node
            - root = node
    - Create a queue and intially add the root node: q = deque([root])
    - Create a list of level nodes: level_nodes = []
    - Create the output array: output = []
    - While the queue is not empty, we process the node in the order of left to right using popleft():
        - node = q.popleft()
        - level_nodes.append(node)
        - Create the root node for the linked list:
        - If node has left child:
            - Add to queue
        - If node has right child:
            - Add to queue
        output.append(build_list(level_nodes))
    - Return output
    """

    def build_list(level_nodes):
        head = Node(level_nodes[0].val)
        current = head
        for i in range(1, len(level_nodes)):
            current.nxt = Node(level_nodes[i].val)
            current = current.nxt
        return head

    q = deque([root])
    output = []
    
    while q:
        n = len(q)
        level_nodes = []
        
        for i in range(n):
            node = q.popleft()
            level_nodes.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        output.append(build_list(level_nodes))

    return output


rootA = BST(3)
rootB = BST(1)
rootC = BST(4)
rootD = BST(0)
rootE = BST(2)
rootF = BST(5)
rootA.left = rootB
rootA.right = rootC
rootB.left = rootD
rootB.right = rootE
rootC.right = rootF

# Expected output: [3 -> None, 1 -> 4 -> None]
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.nxt
    result.append("None")
    return "->".join(result)

result = list_of_depths(rootA)
for i, linked_list in enumerate(result):
    print(f"Level {i}: {print_linked_list(linked_list)}")
