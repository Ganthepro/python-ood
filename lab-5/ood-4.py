class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        t = self.head
        while t.next != None:
            t = t.next
        t.next = Node(value)
        self.tail = t.next

    def find_item_by_index(self, index):
        t = self.head
        i = 0
        while t != None:
            if i == index:
                return t
            t = t.next
            i += 1
        return None
    
    def size(self):
        t = self.head
        s = 0
        while t != None:
            t = t.next
            s += 1
        return s
    
    def __str__(self) -> str:
        t = self.head
        if t == None:
            return 'Empty'
        output = ''
        while t.next != None:
            output += str(t.value) + '->'
            t = t.next
        output += str(t.value)
        if output == '':
            return 'Empty'
        return output

inp = input("Enter input : ").split(",")
LL = LinkedList()

tail = None
head = None
temp_next = None
for i in inp:
    i = i.split()
    if i[0] == 'A':
        LL.append(i[1])
        print(LL)
    elif i[0] == 'S':
        j = i[1].split(":")
        if LL.head == None:
            print("Error! {list is empty}")
        else:
            node_1 = LL.find_item_by_index(int(j[0]))
            if node_1 == None:
                print("Error! {index not in length}:", j[0])
                break
            node_2 = LL.find_item_by_index(int(j[1]))
            if node_2 == None:
                LL.append(j[1])
                print("index not in length, append :", j[1])
                node_2 = LL.find_item_by_index(int(j[1]))
                continue
            try:
                print(f"Set node.next complete!, index:value = {j[0]}:{node_1.value} -> {j[1]}:{node_2.value}")
                temp_next = node_1.next
                node_1.next = node_2
                tail = node_1
                head = node_2
            except:
                pass
try:
    if int(j[0]) < int(j[1]):
        print("No Loop")
        print(LL)
    elif tail.next == head:
        print("Found Loop")
    else:
        print("No Loop")
        tail.next = temp_next
        print(LL)
except:
    print("No Loop")
    print(LL)