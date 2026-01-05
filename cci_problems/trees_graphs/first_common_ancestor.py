class BT:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def first_common_ancestor(root, node1, node2):
    """Design an algorithm and write code to find the first common ancestor
       of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
       necessarily a binary search tree.
    
    Example:
                1
            2       3
                4       5
                    6       7
    
    The first common ancestor of 4 and 6 is 3 because 3 is the parent of 4 while 6 is the direct child of 5 whose parent is 3
    
    Algorithm: Recursive depth first search
    - We first need to find the two nodes: node1 and node2
    - Keep track of the node that leads to node1 or node2 in the variable called ancestor
        - if ancestor.left == node1 and ancestor.right == node2: return ancestor
        - if ancestor.left == node1 or ancestor.right == node1:
            - ancestor 
    """
    def find_ancestor(node):
        if node is None:
            return
        
        if node == node1 or node == node2:
            return node
        
        left_result = find_ancestor(node.left)
        right_result = find_ancestor(node.right)
        
        if left_result is not None and right_result is not None:
            return node
        if left_result is not None:
            return left_result
        if right_result is not None:
            return right_result
        
        return None
    return find_ancestor(root)


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

print(first_common_ancestor(rootA, rootD, rootB).val)