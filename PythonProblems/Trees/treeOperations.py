from PythonProblems.Trees.TreeForm import create_binary_tree

__author__ = 'venkat'


def preOrder2(root):
    li = []
    while True:
        while root:
            print root.data
            li.append(root)
            root = root.left

        if len(li) == 0:
            break
        root = li.pop()
        root = root.right

def inOrder2(root):
    li = []
    while True:
        while root:
            li.append(root)
            root = root.left

        if len(li) == 0:
            break
        root = li.pop()
        print root.data
        root = root.right

def postOrder2(root):
    s1 = []
    s2 = []
    s1.append(root)
    while len(s1) != 0:
        root = s1.pop()
        s2.append(root)
        if root.left != None:
            s1.append(root.left)
        if root.right != None:
            s1.append(root.right)
    while len(s2)!= 0:
        print s2.pop().data


def main():
    root = create_binary_tree()
    postOrder2(root)


if __name__ == "__main__":
    main()