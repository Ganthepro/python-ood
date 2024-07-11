print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

class Stack():
    def __init__(self) -> None:
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

s = Stack()

for e in ls:
    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():
    s.pop()

print(s.size(),"Data in stack : ",s.items)

