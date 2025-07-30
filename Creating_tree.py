

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

"""
Traversal
"""

"""
left root right
"""

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

inorder(root)

"""
root left right
"""
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

preorder(root)

"""
Left right root
"""

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

postorder(root)
