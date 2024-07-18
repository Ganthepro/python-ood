class Node:
    def __init__(self, value = [], next = None) -> None:
        self.__value = value
        self.__next = next

    @property
    def value(self):
        return self.__value
    
    @property
    def next(self):
        return self.__next
    
    def set_next(self, next):
        self.__next = next

    def set_value(self, value = []):
        if value == []:
            self.__value = []
        else:
            self.__value.insert(0, value)
    
    def __str__(self) -> str:
        return str(" ".join(self.__value))
    
class LinkedList:
    def __init__(self, head, init_node = 0) -> None:
        self.__head: Node = head
        self.__tail: Node = None
        self.__max_base = 1
        self.__size = 0

        if init_node != 0:
            for i in range(init_node - 1):
                self.create_node()

    def find_tail(self):
        t = self.__head
        self.__size = 0
        while t.next != None:
            t = t.next  
            self.__size += 1
        self.__tail = t

    def create_node(self):
        if self.__tail == None:
            self.__head.set_next(Node([]))
        else:
            self.__tail.set_next(Node([]))
        self.find_tail()

    def append(self, value):
        if self.__tail == None:
            n = Node([value])
            self.__head.set_next(n)
        else:
            self.__tail.set_next(Node([value]))
        if len(value) > self.__max_base:
            if value[0] == "-":
                value = value[1:]
            self.__max_base = len(value)
        self.find_tail()

    def __str__(self) -> str:
        t = self.__head
        string = ""
        while t.next != None:
            string += f"{t.value} "
            t = t.next
        string += str(t.value)
        return string
    
    def set_head(self, node):
        self.__head = node

    def reset_value(self, index):
        t = self.__head
        for i in range(index):
            t = t.next
        t.set_value()

    def append_value(self, value, index):
        t = self.__head
        for i in range(index):
            t = t.next
        t.set_value(value)

    def set_value(self, value, index):
        t = self.__head
        for i in range(index):
            t = t.next
        if len(t.value) == 0:
            t.set_value([value])
        t.set_value(value)
    
    @property
    def max_base(self):
        return self.__max_base

    @property
    def head(self):
        return self.__head
    
    @property
    def tail(self):
        return self.__tail
    
    @property
    def size(self):
        return self.__size

inp = "456 -789 0 -50384 15615 -1 72".split()
linked_list = LinkedList(Node([inp[0]], None))
for i in range(1, len(inp)):
    linked_list.append(inp[i])

before = linked_list

def radix_sort():
    temp = linked_list
    for i in range(1, linked_list.max_base + 1):
        print("------------------------------------------------------------")
        print(f"Round : {i}")
        next_linked_list = LinkedList(Node([], None), 10)
        t = temp.head
        while t.next != None:
            for j in reversed(t.value):
                try:
                    next_linked_list.append_value(j, int(j[0 - i]))
                except:
                    next_linked_list.append_value(j, 0)
            t = t.next
        for j in t.value:
            try:
                next_linked_list.append_value(j, int(j[0 - i]))
            except:
                next_linked_list.append_value(j, 0)
        temp = next_linked_list
        index = 0
        t_temp = temp.head
        while t_temp.next != None:
            print(f"{index}: {t_temp}")
            index += 1
            t_temp = t_temp.next
        print(f"{index}: {t_temp}")
    return temp

after = radix_sort()

print("------------------------------------------------------------")
print(f"{linked_list.max_base} Time(s)")

temp = before.head
print("Before Radix Sort ", end=": ")
while temp.next != None:
    if len(temp.value) != 0:
        for i in range(len(temp.value)):
            print(f"{temp.value[i]} -> ", end="")
    temp = temp.next
for i in range(len(temp.value)):
    if i == len(temp.value) - 1:
        print(f"{temp.value[i]}", end="")
    else:
        print(f"{temp.value[i]} -> ", end="")
print()

temp = after.head
print("After  Radix Sort ", end=": ")
while temp.next != None:
    if len(temp.value) != 0:
        for i in range(len(temp.value)):
            if "-" not in temp.value[i]:
                print(f"{temp.value[i]} -> ", end="")
    temp = temp.next

