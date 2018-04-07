from lists.linkedList import FormList

__author__ = 'venkat'

def reverse_in_pairs(mylist):
    curr = mylist.head
    temp1 = temp2 = None
    while curr != None and curr.next != None:
        if(temp1 != None):
            temp1.next.next = curr.next
        temp1 = curr.next
        curr.next = curr.next.next
        temp1.next = curr
        if temp2 == None:
            temp2 = temp1
        curr = curr.next
    mylist.head = temp2

def create_list():
    elements = [1,2,3,4,5]
    mylist = FormList()
    [mylist.add_at_end(item) for item in elements]
    reverse_in_pairs(mylist)
    mylist.print_list()

create_list()