class Stack:
    def __init__(self):
        self.items = []
        self.combo = 0

    def push(self, value):
        if self.size() > 1:
            if self.items[-1] == value and self.items[-2] == value:
                self.pop()
                self.pop()
                self.combo += 1
                return
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size == 0
    
inp = input('Enter Input : ').split()

S = Stack()

for i in inp:
    S.push(i)

print(S.size())
if S.size() == 0:
    print("Empty")
else:
    print("".join(reversed(S.items)))

if S.combo > 1:
    print(f"Combo : {S.combo} ! ! !")