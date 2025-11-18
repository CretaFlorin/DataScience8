class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            self.items.pop()

    def is_empty (self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def __str__(self):
        return f"Stack: {self.items}"    


s = Stack()
s.push(1)   
s.push(2) 
s.push(3) 
s.push(4)  

print(s)

s.pop()

print(s)

s.push(5)

print(s)
