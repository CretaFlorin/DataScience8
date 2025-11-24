class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def delete_node(self, node):
        if node is None:
            return

        # dacă este head
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return

        # dacă este tail
        if node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return

        # nod în mijloc
        node.prev.next = node.next
        node.next.prev = node.prev

    def find_nod_to_delete(self, val):
        current = self.head
        while current:
            if current.val == val:
                return current     # **** returnăm NODE, nu valoarea ****
            current = current.next
        return None

    def delete_by_value(self, val):
        node = self.find_nod_to_delete(val)
        if node:
            self.delete_node(node)
            return True
        return False

    def __str__(self):
        result = "DLL: "
        current = self.head
        while current:
            result += str(current.val) + " "
            current = current.next
        return result


# ----------------- test simplu -----------------
dll = DLL()
print("empty?", dll.is_empty())   # True

dll.insert_first(10)
print(dll)                        # DLL: 10

dll.insert_first(20)
dll.insert_first(30)
dll.insert_first(40)
dll.insert_first(50)
print(dll)                        # DLL: 50 40 30 20 10

dll.insert_last(20)
print(dll)                        # DLL: 50 40 30 20 10 20

# delete head
dll.delete_node(dll.head)
print(dll)                        # DLL: 40 30 20 10 20

# delete tail
dll.delete_node(dll.tail)
print(dll)                        # DLL: 40 30 20 10

# find non-existent
node = dll.find_nod_to_delete(60)
print(node)                       # None

# find existent (returnează node)
node = dll.find_nod_to_delete(30)
print(node)                       # <__main__.Node object ...>

# ștergere corectă: dă nodul la delete_node sau folosește delete_by_value
dll.delete_node(node)             # șterge nodul găsit
print(dll)                        # DLL: 40 20 10

# sau echivalent:
dll.delete_by_value(20)
print(dll)                        # DLL: 40 10
