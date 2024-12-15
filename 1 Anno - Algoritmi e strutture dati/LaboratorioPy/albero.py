class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    
class BinaryTree:
    def __init__(self,root=None):
        self.root = root

def print_tree(node,prefix=""):
    if not node:
        return
    print(prefix+str(node.value))
    prefix +="| "
    print_tree (node.left,prefix)
    print_tree (node.right,prefix)

root = Node(1)
root.left = Node(2)
root.righ = Node(3)
root.left.left = Node(4)
root.left.right = Node (5)

