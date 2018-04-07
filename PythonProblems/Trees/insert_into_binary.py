from Queue import Queue
from PythonProblems.Trees.level_order_travesal import lot

__author__ = 'venkat'

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lot_insert(root, node):
    li = Queue()
    li._put(root)
    while li.empty() != True:
        root = li._get()
        if root.left == None:
            root.left = node
            break
        if root.right == None:
            root.right = node
            break
        li._put(root.left)
        li._put(root.right)
    return root

def crt_bt():
    li = [1,2,3,4,5,6,7]
    root = None
    for item in li:
        if root == None:
            root = Node(item)
        else:
            lot_insert(root, Node(item))
    lot(root)
    return root

if __name__ == "__main__":
    crt_bt()