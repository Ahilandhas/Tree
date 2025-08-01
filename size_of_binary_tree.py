
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def size_of_binary_tree(root):
    if root is None:
        return 0
    return 1 + size_of_binary_tree(root.left) + size_of_binary_tree(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print(size_of_binary_tree(root))
