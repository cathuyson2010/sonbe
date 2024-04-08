class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def search(head, key):
    current = head
    while current:
        if current.value == key:
            return True
        current = current.next
    return False

def insert_after_nth_node(head, n ,value):
    current = head
    position = 1
    while current and position < n:
        current = current.next
        position += 1
    if current is None:
        print('Out of bounds.')
        return
    new_node = ListNode(value)
    new_node.next = current.next
    current.next = new_node

def print_list(head):
    while head is not None:
        print(head.value)
        head = head.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print_list(head)

print(search(head, 3))
print(search(head, 5))

insert_after_nth_node(head, 2, 5)
print_list(head)