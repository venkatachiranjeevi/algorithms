from lists.linkedList import FormList

__author__ = 'venkat'


def swap_nodes(mylist, x, y):
    curr_x  = curr_y = mylist.head
    prev_y= prev_x = None
    while curr_x != None and curr_x.data != x:
        prev_x = curr_x
        curr_x = curr_x.next
    while curr_y != None and curr_y.data != y:
        prev_y = curr_y
        curr_y = curr_y.next

    if prev_x != None:
        prev_x.next = curr_y
    else:
        mylist.head = curr_y
    if prev_y != None:
        prev_y.next = curr_x
    else:
        mylist.head = curr_x
    temp = curr_x.next
    curr_x.next = curr_y.next
    curr_y.next = temp
    mylist.print_list()


def create_list():
    elements = [1,2,3,4,5]
    mylist = FormList()
    [mylist.add_at_end(item) for item in elements]
    swap_nodes(mylist, 1,5)

create_list()