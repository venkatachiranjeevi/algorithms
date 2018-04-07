from lists.linkedList import FormList

__author__ = 'venkat'


def del_nth_from_list(mylist, n):
    temp = curr = mylist.head
    while n != 0:
        temp = temp.next
        n -= 1
    while temp.next != None:
        temp = temp.next
        curr = curr.next
    if(curr.next != None):
        curr.next = curr.next.next

def create_list():
    elements = [1,2,3,4,5,6,7,8,9]
    mylist = FormList()
    [mylist.add_at_end(item) for item in elements]
    mylist.print_list()
    del_nth_from_list(mylist, 0)
    mylist.print_list()


create_list()