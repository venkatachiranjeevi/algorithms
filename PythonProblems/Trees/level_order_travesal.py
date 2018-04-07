from Queue import Queue
from PythonProblems.Trees.TreeForm import create_binary_tree

__author__ = 'venkat'


def lot(root):
    li = Queue()
    li._put(root)
    while li.empty() != True:
        root = li._get()
        print root.data
        if root.left:
            li._put(root.left)
        if root.right:
            li._put(root.right)


def problem2():
    root = create_binary_tree()
    lot(root)

if __name__ == "__main__":
    problem2()