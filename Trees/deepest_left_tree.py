from treeTravesal import Tree

__author__ = 'venkat'


def find_node(root, mxl,lvl, isLeft):
    if root is None:
        return
    if isLeft:
        if root.left is None and root.right is None:
            if(lvl> mxl[0]):
                mxl[0] = lvl
                find_depest_left.rest = root
    find_node(root.left, mxl, lvl+1, False)
    find_node(root.right, mxl, lvl+1, True)

def find_depest_left(root):
    find_depest_left.rest = None
    mxl = [0]
    find_node(root, mxl, 0, False)
    return find_depest_left.rest

def deepest_left():
    li = [1, 2,3,4,5,6,7,8,9]
    tree = Tree()
    [tree.insert_node(item) for item in li]
    node= find_depest_left(tree.root)
    print node.data1


def find_leaves(root, li):
    if root is None:
        return
    li.append(root.data)
    if root.left is None and root.right is None:
        print_array(li)
        li.pop()
    else:
        find_leaves(root.left, li)
        find_leaves(root.right, li)

def print_array(li):
    for item in li:
        print item
    print "asddsa"

def print_all_root_to_leaf():
    li = [1,2 ,3,4,5, 6,7]
    tree = Tree()
    [tree.insert_node(item) for item in li]

    find_leaves(tree.root, [])

print print_all_root_to_leaf()
