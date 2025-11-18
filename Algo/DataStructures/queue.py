class Queue:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)   

    def pop(self):
        if not self.is_empty():
            self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]     

    def __str__(self):
        return f"Queue: {self.items}"          


q = Queue()
q.push(1)   
q.push(2) 
q.push(3) 
q.push(4)  

print(q)

q.pop()

print(q)

q.push(5)

print(q)

