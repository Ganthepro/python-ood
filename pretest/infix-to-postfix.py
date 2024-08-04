class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        temp = self.top()
        self.items.pop()
        return temp
    
    def top(self):
        if len(self.items) == 0:
            return ''
        return self.items[-1]    
    
S = Stack()
inp = input()
output = ""
for i in inp:
    if i == "(":
        S.push(i)
    elif i == ")":
        while S.top() != "(":
            try:
                output += S.pop()
            except:
                break
        if S.top() == "(":
            S.pop()
    elif i in "*/":
        less_prio = "+-("
        more_prio = "/*"
        if S.top() not in less_prio:
            while S.top() in more_prio:
                try:
                    output += S.pop()
                except:
                    break
        S.push(i)
    elif i in "+-":
        less_prio = "("
        more_prio = "+-*/"
        if S.top() not in less_prio:
            while S.top() in more_prio:
                try:
                    output += S.pop()
                except:
                    break
        S.push(i)
    else:
        output += i

while len(S.items) > 0:
    output += S.pop()

print(output)
