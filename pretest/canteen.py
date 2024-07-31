class Queue:
    def __init__(self) -> None:
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        temp = self.items[0]
        self.items.pop(0)
        return temp

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return ", ".join(self.items)

Q = Queue()
init, option = input().split("/")
for i in option.split(","):
    if i == "D":
        if Q.size() == 0:
            print("Empty")
        else:
            print(Q.pop())
    else:
        typ, id = i.split()
        if typ == "E":
            Q.push(id)