# A Queue implemented on Linked List
from linked_list import SLL

class Queue:
    def __init__(self):
        self.items = SLL()

    def push(self,item):
        self.items.add_last(item)   

    def pop(self):
        if not self.is_empty():
            self.items.delete_first()

    def is_empty(self):
        return self.items.is_empty()

    def peek(self):
        if self.is_empty():
            return None
        return self.items.head.val

    def __str__(self):
        return f"Queue: {self.items}"          

from time import time
q = Queue()

start = time()
for i in range(5000000):
    q.push(i)
for _ in range(5000000):
    q.pop()
end = time()
print("Duration", end - start)