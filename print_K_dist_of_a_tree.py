

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def print_K_dist_of_a_tree(root,k):
    if root is None:
        return
    if k == 0:
        print(root.data,end=" ")
    else:
        print_K_dist_of_a_tree(root.left, k - 1)
        print_K_dist_of_a_tree(root.right, k - 1)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print_K_dist_of_a_tree(root,2)
