class Queue:
    def __init__(self) -> None:
        self._items = []

    def pop(self):
        if self._items:
            return self._items.pop(0)
        return None

    def push(self, data):
        self._items.append(data)

    def size(self):
        return len(self._items)
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __repr__(self):
        return f"Queue({self._items})"


class Stack:
    def __init__(self, stack_type) -> None:
        self._items = []
        self._bombs = []
        self._type = stack_type
        self._bomb_queue = Queue()
        self._explosion_count = 0
        self._failed_explosion_count = 0

    @property
    def bomb_queue(self):
        return self._bomb_queue
    
    @property
    def items(self):
        if not self._items:
            return "ytpmE" if self._type == "mirror" else "Empty"
        return "".join(reversed(self._items))
    
    @property
    def explosion_count(self):
        return self._explosion_count
    
    @property
    def failed_explosion_count(self):
        return self._failed_explosion_count

    def push(self, data):
        if len(self._items) > 1 and self._items[-1] == data and self._items[-2] == data:
            if self._type == "normal" and not self._bomb_queue.is_empty():
                bomb = self._bomb_queue.pop()
                if bomb == self._items[-1]:
                    self._pop()
                    self._pop()
                    self._failed_explosion_count += 1
                else:
                    self.push(bomb)
            else:
                self._pop()
                self._pop()
                self._explosion_count += 1
                if self._type == "mirror":
                    self._bombs.append(data)
                return
        self._items.append(data)

    def _pop(self):
        if self._items:
            self._items.pop()

    @property
    def bombs(self):
        return self._bombs

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack(type={self._type}, items={self._items}, bombs={self._bombs})"
    
inp = input("Enter Input (Normal, Mirror) : ")
mirror_stack = Stack("mirror")
normal_stack = Stack("normal")
normal_sequence, mirror_sequence = inp.split()

for char in reversed(mirror_sequence):
    mirror_stack.push(char)

for bomb in mirror_stack.bombs:
    normal_stack.bomb_queue.push(bomb)

for char in normal_sequence:
    normal_stack.push(char)

def reversed_word(word):
    return word[::-1]

print("NORMAL :")
print(normal_stack.size())
print(normal_stack.items)
print(f"{normal_stack.explosion_count} Explosive(s) ! ! ! (NORMAL)")
if normal_stack.failed_explosion_count > 0:
    print(f"Failed Interrupted {normal_stack.failed_explosion_count} Bomb(s)")
print("------------MIRROR------------")
print(reversed_word("MIRROR :"))
print(mirror_stack.size())
print(mirror_stack.items)
print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_stack.explosion_count}")