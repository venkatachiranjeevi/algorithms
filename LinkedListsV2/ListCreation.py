class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_end(self, value):
        node = Node(value)
        temp = self.head
        if self.head is None:
            self.head = node
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def add_at_start(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def add_after_value(self, insert_value, search_value):
        is_inserted = False
        node = Node(insert_value)
        temp = self.head
        if temp.value == search_value:
            node.next = temp.next
            temp.next = node
            is_inserted = True
        else:
            while temp.next is not None:
                if temp.next.value == search_value:
                    node.next = temp.next
                    temp.next = node
                    is_inserted = True
                    break
                temp = temp.next
        if not is_inserted:
            temp.next = node

    def delete_start_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_end_node(self):
        if self.head is None:
            return
        temp = self.head
        if self.head.next is None:
            self.head = None
            return
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_value(self, value):
        if self.head.value == value:
            self.head = self.head.next
        temp = self.head
        while temp.next is not None:
            pass

    def revers_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

def reverse_sam(node):
    if node is None or node.next is None:
        return node
    node1 = reverse_sam(node)
    node.next.next = node
    node.next = None
    return node1

def reverse(node):
    if node is None:
        return node

    if node.next is None:
        return node

    node1 = reverse(node.next)
    node.next.next = node
    node.next = None
    return node1


linked_list_operations = LinkedList()
linked_list_operations.delete_start_node()
linked_list_operations.delete_end_node()
linked_list_operations.add_at_start(2)
linked_list_operations.delete_end_node()
linked_list_operations.add_at_start(1)
linked_list_operations.add_at_end(3)
linked_list_operations.add_at_end(4)
linked_list_operations.add_at_end(5)
linked_list_operations.add_at_end(6)
linked_list_operations.add_at_end(7)
linked_list_operations.add_after_value(-2, 1)
linked_list_operations.add_after_value(-3, 4)
linked_list_operations.delete_start_node()
linked_list_operations.delete_end_node()
# linked_list_operations.delete_value(-3)
# linked_list_operations.delete_value(1)
linked_list_operations.display()
print('Done')

two = LinkedList()
two.add_at_end(1)
two.add_at_end(2)
two.add_at_end(3)
two.add_at_end(4)
x = reverse(two.head)
print('reversed')
