from networkx import is_empty


class Queue:
    def __init__(self) -> None:
        self.items = []

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        self.items.pop(0)
    
    def get_head(self):
        try:
            return self.items[0]
        except: 
            return None    

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def __str__(self) -> str:
        return ", ".join(self.items)
    
def find_max_base(inp):
    max_base = 0
    for i in inp:
        if len(i) > max_base:
            max_base = len(i)
    return max_base

def radix_sort(inp):
    max_number = [Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue()]
    temp = [Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue()]
    for i in range(find_max_base(inp)):
        if i == 0:
            for j in inp:
                value = j[-1]
                max_number[int(value)].enQueue(j)
        else:
            for j in enumerate(max_number):
                t = j.items.copy()
                for k in t:
                    j.deQueue()
                    try:
                        value = k[-(i + 1)]
                        max_number[int(value)].enQueue(k)
                    except:
                        max_number[0].enQueue(k)
        for i in max_number:
            print(i)
        print("------")

    
inp = input().split()
radix_sort(inp)