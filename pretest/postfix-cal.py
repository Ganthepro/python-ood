class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return " ".join(self.items)
    
S = Stack()
inp = input().split()
for i in inp:
    if i not in "+-*/":
        S.push(int(i))
    elif S.size() > 1:
        if i == "+":
            temp = S.items[-2] + S.items[-1]
        elif i == "-":
            temp = S.items[-2] - S.items[-1]
        elif i == "*":
            temp = S.items[-2] * S.items[-1]
        elif i == "/":
            temp = S.items[-2] / S.items[-1]
        S.pop()
        S.pop()
        S.push(temp)
print(temp)