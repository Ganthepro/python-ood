class ManageStack:
    def __init__(self) -> None:
        self.items = []

    def add(self, data):
        self.items.append(data)
        print(f"Add = {data}")

    def pop(self):
        if len(self.items) == 0:
            print(-1)
            return
        print(f"Pop = {self.items[-1]}")
        self.items.pop()

    def delete(self, data):
        if len(self.items) == 0:
            print(-1)
            return
        for e in self.items:
            if e == data:
                print(f"Delete = {e}")
        self.items = [e for e in self.items if e != data]

    def lessthan_remove(self, data):
        if len(self.items) == 0:
            print(-1)
            return
        for e in reversed(self.items):
            if e < data:
                print(f"Delete = {e} Because {e} is less than {data}")
        self.items = [e for e in self.items if e >= data]

    def morethan_remove(self, data):
        if len(self.items) == 0:
            print(-1)
            return
        for e in reversed(self.items):
            if e > data:
                print(f"Delete = {e} Because {e} is more than {data}")
        self.items = [e for e in self.items if e <= data]

inp = input("Enter Input : ").split(',')
ms = ManageStack()

for e in inp:
    if e[0] == 'A':
        ms.add(int(e[2:]))
    elif e[0] == 'P':
        ms.pop()
    elif e[0] == 'D':
        ms.delete(int(e[2:]))
    elif e[0] == 'L':
        ms.lessthan_remove(int(e[3:]))
    elif e[0] == 'M':
        ms.morethan_remove(int(e[3:]))

print(f"Value in Stack = {ms.items}")