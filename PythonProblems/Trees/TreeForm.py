__author__ = 'venkat'


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def create_binary_tree():
    root  = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

def create_tree2():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.right = Node(7)
    root.right.right.right = Node(8)
    root.left.left.left = Node(11)
    root.right.left.right.left = Node(9)
    root.right.right.right.right= Node(10)
    return root

def print_inorder(root):
    if root == None:
        return
    print_inorder(root.left)
    print root.data
    print_inorder(root.right)


def print_preorder(root):
    if root == None:
        return
    print root.data
    print_preorder(root.left)
    print_preorder(root.right)

def print_postorder(root):
    if root == None:
        return
    print_postorder(root.left)
    print_postorder(root.right)
    print root.data


def basic_tree_operations():
    root = create_binary_tree()
    # print_inorder(root)
    # print_preorder(root)
    print_postorder(root)


if __name__ == "__main__":
    basic_tree_operations()