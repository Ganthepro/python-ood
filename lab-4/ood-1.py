class Queue:
    def __init__(self) -> None:
        self.items = []

    def get_items(self):
        return [str(e) for e in self.items]

    def push(self, data):
        self.items.append(data)
        print(f"Add {data} index is {self.items.index(data)}")

    def pop(self):
        try:
            print(f"Pop {self.items[0]} size in queue is {self.size() - 1}")
            self.items.pop(0)
        except:
            print(-1)

    def size(self):
        return len(self.items)

Q = Queue()

inp = input("Enter Input : ").split(',')

for e in inp:
    if e[0] == "E":
        Q.push(int(e[2:]))
    elif e[0] == "D":
        Q.pop()

if Q.size() == 0:
    print("Empty")
else:
    print(f"Number in Queue is :  {Q.get_items()}")