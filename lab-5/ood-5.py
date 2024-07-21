class Node:
    def __init__(self, value = [], next = None, back = None) -> None:
        self.__value = value
        self.__next = next
        self.__back = back

    @property
    def value(self):
        return self.__value
    
    @property
    def next(self):
        return self.__next
    
    @property
    def back(self):
        return self.__back
    
    def set_next(self, next):
        self.__next = next

    def sort_value(self):
        for i in range(len(self.__value)):
            for j in range(i + 1, len(self.__value)):
                if int(self.__value[i]) < int(self.__value[j]):
                    self.__value[i], self.__value[j] = self.__value[j], self.__value[i]

    def set_value(self, value = [], index = 0):
        if value == []:
            self.__value = []
        else:
            if index == 0:
                self.__value.insert(index, value)
            else:
                self.__value.append(value)
    
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
            self.__head.set_next(Node([], None, self.__head))
        else:
            self.__tail.set_next(Node([], None, self.__tail))
        self.find_tail()

    def append(self, value):
        if self.__tail == None:
            self.__head.set_next(Node([value]))
        else:
            self.__tail.set_next(Node([value], None, self.__tail))
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
        if int(value) < 0:
            t.set_value(value, len(t.value))
        else:
            # print(t.value)
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

inp = input("Enter Input : ").split()
# inp = "64 8 216 512 27 729 0 1 343 125".split()
linked_list = LinkedList(Node([inp[0]], None))
for i in range(1, len(inp)):
    linked_list.append(inp[i])

before = linked_list

def radix_sort(is_print = False):
    temp = linked_list
    for i in range(1, linked_list.max_base + 1):
        if is_print:
            print("------------------------------------------------------------")
            print(f"Round : {i}")
        next_linked_list = LinkedList(Node([]), 10)
        t = temp.head
        while t != None:
            for j in reversed(t.value):
                if int(j) < 0:
                    continue
                try:
                    next_linked_list.append_value(j, int(j[0 - i]))
                except:
                    next_linked_list.append_value(j, 0)
            for j in t.value:
                if int(j) < 0:
                    try:
                        next_linked_list.append_value(j, int(j[0 - i]))
                    except:
                        next_linked_list.append_value(j, 0)
            t = t.next
        temp = next_linked_list
        index = 0
        t_temp = temp.head
        if is_print:
            while t_temp.next != None:
                print(f"{index} : {t_temp}")
                index += 1
                t_temp = t_temp.next
            print(f"{index} : {t_temp}")
    t_temp = temp.head
    while t_temp != None:
        t_temp.sort_value()
        t_temp = t_temp.next
    return temp

def is_all_equal(inp):
    for i in range(1, len(inp)):
        if inp[i] != inp[i - 1]:
            return False
    return True

if not is_all_equal(inp):
    after = radix_sort(True)
    print("------------------------------------------------------------")
    print(f"{linked_list.max_base} Time(s)")
else:
    after = radix_sort()
    print("------------------------------------------------------------")
    print(f"{0} Time(s)")

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

temp = after.tail
flag = False
print("After  Radix Sort ", end=": ")
while temp != None:
    if len(temp.value) != 0:
        for i in range(len(temp.value)):
            if int(temp.value[i]) > 0:
                if flag:
                    print(f"-> {temp.value[i]} ", end="")
                else:
                    print(f"{temp.value[i]} ", end="")
                    flag = True
    temp = temp.back
temp = after.head
while temp != None:
    if len(temp.value) != 0:
        for i in range(len(temp.value)):
            if int(temp.value[i]) <= 0:
                if flag:
                    print(f"-> {temp.value[i]} ", end="")
                else:
                    print(f"{temp.value[i]} ", end="")
                    flag = True
    temp = temp.next