class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Singly Linked List
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    # O(1)
    def add_first(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node

    # O(1)
    def add_last(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # O(1)
    def delete_first(self):
        if not self.is_empty():
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    # O(n)
    def delete_last(self):
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.tail = current
        

    def __str__(self):
        result = "SLL: "

        current = self.head
        while current is not None:
            result += str(current.val) + ' ' 
            current = current.next

        return result

# l = SLL()

# l.add_first(1)
# l.add_first(2)
# l.add_first(3)
# l.add_first(4)
# print(l)

# l.add_last(5)
# l.add_last(6)
# print(l)

# l.delete_first()
# l.delete_first()
# l.delete_first()
# print(l)

# l.delete_last()
# print(l)
# l.delete_last()
# print(l)
# l.delete_last()
# print(l)
