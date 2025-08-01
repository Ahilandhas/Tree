"""
First convention
"""

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def height_of_a_tree(root):
    if root is None:
        return 0
    else:
        lh = height_of_a_tree(root.left)
        rh = height_of_a_tree(root.right)

        return max(lh,rh)+1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print(height_of_a_tree(root))


"""
second convention
"""


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def height_of_a_tree(root):
    if root is None:
        return -1
    else:
        lh = height_of_a_tree(root.left)
        rh = height_of_a_tree(root.right)

        return max(lh,rh)+1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print(height_of_a_tree(root))
