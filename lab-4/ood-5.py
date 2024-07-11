class Queue:
    def __init__(self) -> None:
        self.__items = []

    def pop(self):
        temp = self.__items[0]
        self.__items.remove(self.__items[0])
        return temp

    def push(self, data):
        self.__items.append(data)

    @property
    def items(self):
        return self.__items
    
    def size(self):
        return len(self.__items)
    
class Stack:
    def __init__(self, type) -> None:
        self.__items = []
        self.__bomb = []
        self.__type = type
        self.__bomb_queue: Queue = Queue()
        self.__counter = 0
        self.__failed_counter = 0

    @property
    def bomb_queue(self):
        return self.__bomb_queue
    
    @property
    def items(self):
        if len(self.__items) == 0:
            return "Empty"
        return reversed(self.__items)
    
    @property
    def counter(self):
        return self.__counter
    
    @property
    def failed_counter(self):
        return self.__failed_counter

    def push(self, data):
        if self.size() > 1 and self.__items[-1] == data and self.__items[-2] == data:
            if self.__type == "normal" and self.__bomb_queue.size() > 0:
                bomb = self.__bomb_queue.pop()
                if bomb == self.__items[-1]:
                    self.pop()
                    self.pop()
                    self.__failed_counter += 1
                else:
                    self.push(bomb)
            else:
                self.pop()
                self.pop()
                self.__counter += 1
                if self.__type == "mirror":
                    self.__bomb.append(data)
                print(data)
                return
        self.__items.append(data)

    def pop(self):
        self.__items.pop()

    @property
    def bomb(self):
        return self.__bomb

    def size(self):
        return len(self.__items)
    

inp = input("Enter Input (Normal, Mirror) : ")
S_m = Stack("mirror")
S_n = Stack("normal")

normal, mirror = inp.split()
for m in mirror:
    S_m.push(m)

for b in reversed(S_m.bomb):
    S_n.bomb_queue.push(b)

for n in normal:
    S_n.push(n)

def reversed_word(word):
    return "".join(reversed(list(word)))

print("NORMAL :")
print(S_n.size())
print("".join(S_n.items))
print(f"{S_n.counter} Explosive(s) ! ! ! (NORMAL)")
if S_n.failed_counter > 0:
    print(f"Failed Interrupted {S_n.failed_counter} Bomb(s)")
print("------------MIRROR------------")
print(reversed_word("MIRROR :"))
print(S_m.size())
print(reversed_word("".join(S_m.items)))
print(f"(RORRIM) ! ! ! (s)evisolpxE {S_m.counter}")