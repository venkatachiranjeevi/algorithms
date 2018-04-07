from Queue import Queue
import gc
from Arrays.next_greater import Stack

__author__ = 'venkat'


class Node():
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


class Tree():
    def __init__(self):
        self.root = None

    def insert_node(self, x):
        node = Node(x)
        if self.root is None:
            self.root = node
            return
        q = Queue()
        q._put(self.root)
        while(True):
            curr = q._get()
            if curr.left is None:
                curr.left = node
                return
            elif curr.right is None:
                curr.right = node
                return
            else:
                q._put(curr.left)
                q._put(curr.right)

    def inorder_rec(self, root):
        if(root is not None):
            self.inorder_rec(root.left)
            print root.data
            self.inorder_rec(root.right)

    def inorder_nonrec(self, root):
        s = Stack()
        while(True):
            while(root):
                s.push(root)
                root = root.left
            if s.isEmpty():
                return
            root = s.pop()
            print root.data
            root = root.right

    def preorder_rec(self, root):
         if(root is not None):
            print root.data
            self.preorder_rec(root.left)
            self.preorder_rec(root.right)

    def preorder_nonrec(self, root):
        s = Stack()
        while(True):
            while(root):
                print root.data
                s.push(root)
                root = root.left

            if s.isEmpty():
                return
            root = s.pop()
            root = root.right

    def postorder_rec(self, root):
        if(root is not None):
            self.postorder_rec(root.left)
            self.postorder_rec(root.right)
            print root.data

    def postorder_nonrec(self, root):
        s = []
        while(1):
            while(root):
                s.append(root)
                root = root.left
            if len(s) == 0:
                return
            root = s[len(s)-1]
            if root.right is None:
                s.pop()
                print root.data
                if root == s[len(s)-1].right:
                    print s[len(s)-1].data
                    s.pop()
            if len(s) is not 0:
                root = s[len(s)-1].right
            else:
                root = None

    def level_order_traversal(self, root):
        s = Queue()
        s._put(root)
        while(True):
            root = s._get()
            print root.data
            if root.left is not None:
                s._put(root.left)
            if root.right is not None:
                s._put(root.right)
            if s.empty():
                break
    def level_order_reverse_traveral(self, root):
        q = []
        q.append(root)
        s = Stack()
        while(len(q) is not 0):
            root = q.pop(0)
            s.push(root)
            if root.right:
                q.append(root.right)
            if root.left:
                q.append(root.left)
        for item in s.items:
            print item.data



def form_tree():
    a = [1,2,3,4,5, 6,7]
    tree = Tree()
    [tree.insert_node(item) for item in a]
    # tree.inorder_rec(tree.root)
    # tree.inorder_rec(tree.root)
    # tree.postorder_rec(tree.root)
    # tree.preorder_rec(tree.root)
    # tree.preorder_nonrec(tree.root)
    # tree.postorder_nonrec(tree.root)
    # tree.level_order_reverse_traveral(tree.root)
  
form_tree()