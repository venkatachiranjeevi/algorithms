from sys import maxint
from PythonProblems.Trees.TreeForm import create_binary_tree

__author__ = 'venkat'


def find_max_recursion(root):
    max = -maxint
    if root:
        max = root.data
        left = find_max_recursion(root.left)
        right = find_max_recursion(root.right)
        if left > max:
            max = left
        if right > max:
            max = right
    return max

def find_max_non(root):
    pass

def problem1():
   root = create_binary_tree()
   max = find_max_recursion(root)
   print max

if __name__ == "__main__":
    problem1()