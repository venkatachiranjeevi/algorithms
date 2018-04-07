from lists.linkedList import FormList

__author__ = 'venkat'


def del_n_nodes_after_m_nodes(mylist, m, n):
    curr = temp = mylist.head
    while curr != None:
        i =m
        while i!=1:
            curr = curr.next
            temp = temp.next
            i -= 1
        if curr == None:
            break
        i = n
        while i !=0 and temp != None:
            curr.next = temp.next
            temp = temp.next
            i -= 1
        curr = curr.next
        temp = curr

    mylist.print_list()
def create_list():
    elements = [1,2,3]
    mylist = FormList()
    [mylist.add_at_end(item) for item in elements]
    del_n_nodes_after_m_nodes(mylist, 2, 2)

create_list()