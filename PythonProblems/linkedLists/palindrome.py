from lists.linkedList import FormList

__author__ = 'venkat'


def check_palindrome(mylist):
    curr = temp = mylist.head
    while temp  !=None and temp.next != None:
        curr = curr.next
        temp = temp.next.next
    curr = mylist.reverse_list(curr)
    temp = mylist.head
    while curr != None:
        if curr.data != temp.data:
            return False
        curr = curr.next
        temp = temp.next

    return True


def create_list():
    elements = [1,2,3,5,6,4,3,2,1]
    mylist = FormList()
    [mylist.add_at_end(item) for item in elements]
    if check_palindrome(mylist):
        print "list is Palindrome"
    else:
        print "list is not a palindrome list"
    mylist.print_list()


if __name__ == "__main__":
    create_list()