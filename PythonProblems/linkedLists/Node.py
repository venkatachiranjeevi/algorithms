__author__ = 'venkat'

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class FormList():
    def __init__(self):
        self.head = None

    def _add_to_start(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def _add_at_end(self, item):
        node = Node(item)
        if(self.head == None):
            self.head = node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node

    @staticmethod
    def reverse_list(head):
        curr = temp = head
        curr1 = None
        while curr!= None:
            temp = temp.next
            curr.next = curr1
            curr1 = curr
            curr = temp
        return curr1

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def print_list(self):
        current = self.head
        while current != None:
            print current.get_data()
            current = current.get_next()

def add_list(l1, l2):
    while l1 != None and l2 != None:
        pass

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry =0
        res = []
        while l1 != None and l2 != None:
            res, carry = self.get_sum_carry(l1.val, l2.val, carry, res)
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            res, carry = self.get_sum_carry(l1.val, 0 , carry, res)
            l1 = l1.next

        while l2 != None:
            res, carry = self.get_sum_carry(l2.val, 0, carry, res)
            l2 = l2.next

        return res

    def get_sum_carry(self, val1, val2, carry, res):
            sum = val1+val2+carry
            res.append(sum % 10)
            carry = sum /10
            return res, carry


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def show_list():
    a = [1,2,3,4]

    list1 = FormList()
    list2 = FormList()
    [list1._add_at_end(item) for item in [2,4,3]]
    [list2._add_at_end(item) for item in [5,4,6]]
    add_list(list1, list2)

show_list()