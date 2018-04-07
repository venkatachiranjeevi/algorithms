from Queue import Queue
from PythonProblems.Trees.TreeForm import create_tree2
from PythonProblems.Trees.insert_into_binary import crt_bt
from PythonProblems.Trees.level_order_travesal import lot

__author__ = 'venkat'



def find_max_sum_level(root):
    li = Queue()
    level = cl = 1
    sum = max_sum = 0
    li._put(root)
    li._put(None)
    while li.empty() != True:
        root = li._get()
        if root == None:
            cl += 1
            if sum > max_sum:
                max_sum = sum
                level = cl
            sum = 0
            if li.empty() != True:
                li._put(None)
        else:
            sum += root.data
            if root.left:
                li._put(root.left)
            if root.right:
                li._put(root.right)

    print max_sum
    print level

def print_deepest_left_node(root):
    node = root.data
    li = Queue()
    li._put(root)
    while li.empty() != True:
        root = li.get()
        if root.left:
            li._put(root.left)
            node = root.left
        if root.right:
            li._put(root.right)

    print node.data


def print_reverse_level_order(root):
    li =  Queue()
    li._put(root)
    sl = []
    height =0
    while li.empty() != True:
        root = li._get()
        sl.append(root.data)
        if root.right:
            li._put(root.right)
        if root.left:
            li._put(root.left)

    print "height is " + str(height)

    print sl

def print_all_paths_(root, li, x):
    if root == None:
        return
    li.append(root.data)
    if root.left == None and root.right == None:
        print li
    print_all_paths_(root.left, li, x)
    print_all_paths_(root.right, li, x)

def mirror_tree(root):
    if(root):
        mirror_tree(root.left)
        mirror_tree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
    return root

def mirror_tree_non_r(root, root2):
    s1 =  Queue()
    s1._put(root)
    s2 = Queue()
    s2._put(root2)
    while s1.empty() != True and s2.empty() != True:
        if s1.empty() or s2.empty():
            return False
        root = s1._get()
        root2 = s2._get()
        if root.data != root2.data:
            return False
        if root.left:
            s1._put(root.left)
        if root2.right:
            s2._put(root2.right)
        if root.right:
            s1._put(root.right)
        if root2.left:
            s2._put(root2.left)
    return True

def print_all_paths():
    root = create_tree2()
    li = []
    x = 0
    print_all_paths_(root, li, x)

def lca(root, n1, n2):
    if root ==None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)

    if left and right:
        return root
    return left if left != None else right

if __name__ == "__main__":
    root = create_tree2()
    node = lca(root, 2, 5)
    print node.data
    # lot(root)
    # print "started"
    # root2 = mirror_tree(root)
    # root = create_tree2()
    # lot(root)

    # x = mirror_tree_non_r(root, root2)
    # print x
    # if mirror_tree_non_r(root, root2):
    #     print "yes"


    # find_max_sum_level(root)
    # print_deepest_left_node(root)
    # print_reverse_level_order(root)