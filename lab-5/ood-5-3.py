class Node:
    def __init__(self, values=None, next_node=None, prev_node=None) -> None:
        if values is None:
            values = []
        self.values = values
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def sort_values(self):
        for i in range(len(self.values)):
            for j in range(i + 1, len(self.values)):
                if int(self.values[i]) < int(self.values[j]):
                    self.values[i], self.values[j] = self.values[j], self.values[i]

    def set_values(self, values=None, index=0):
        if values is None:
            self.values = []
        else:
            if index == 0:
                self.values.insert(index, values)
            else:
                self.values.append(values)

    def append_value(self, value):
        self.values.append(value)

    def __str__(self) -> str:
        return str(" ".join(self.values))

class LinkedList:
    def __init__(self, head, initial_nodes=0) -> None:
        self.head: Node = head
        self.tail: Node = None
        self.max_base_length = 1
        self.size = 0

        if initial_nodes != 0:
            for _ in range(initial_nodes - 1):
                self.create_node()

    def find_tail(self):
        current_node = self.head
        self.size = 0
        while current_node.next_node is not None:
            current_node = current_node.next_node
            self.size += 1
        self.tail = current_node

    def create_node(self):
        if self.tail is None:
            self.head.set_next_node(Node([], None, self.head))
        else:
            self.tail.set_next_node(Node([], None, self.tail))
        self.find_tail()

    def append(self, value):
        if self.tail is None:
            self.head.set_next_node(Node([value]))
        else:
            self.tail.set_next_node(Node([value], None, self.tail))
        self.find_tail()

    def set_max_base_length(self, value):
        self.max_base_length = value

    def __str__(self) -> str:
        current_node = self.head
        result = ""
        while current_node.next_node is not None:
            result += f"{current_node.values} "
            current_node = current_node.next_node
        result += str(current_node.values)
        return result

    def set_head(self, node):
        self.head = node

    def reset_values(self, index):
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node
        current_node.set_values()

    def append_value(self, value, index):
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node
        if int(value) < 0:
            current_node.set_values(value, len(current_node.values))
        else:
            current_node.set_values(value)

    def append_value_to_back(self, value, index):
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node
        current_node.append_value(value)

    def set_values_at_index(self, value, index):
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node
        if len(current_node.values) == 0:
            current_node.set_values([value])
        current_node.set_values(value)

def is_all_equal(input_list):
    for i in range(1, len(input_list)):
        if input_list[i] != input_list[i - 1]:
            return False
    return True

def is_base_equal(input_list: LinkedList, base=0):
    current_node = input_list.head
    temp_base_value = current_node.values[0][-1]
    while current_node is not None:
        if len(current_node.values) > 0 and temp_base_value != current_node.values[0][-1]:
            return False
        current_node = current_node.next_node
    return True

def radix_sort(linked_list: LinkedList, is_print=False):
    current_list = linked_list
    for i in range(1, linked_list.max_base_length + 1):
        if is_print:
            print("------------------------------------------------------------")
            print(f"Round : {i}")
        next_linked_list = LinkedList(Node([]), 10)
        current_node = current_list.head
        if i == 1 and is_base_equal(current_list):
            while current_node is not None:
                for value in current_node.values:
                    try:
                        next_linked_list.append_value_to_back(value, int(value[0 - i]))
                    except:
                        next_linked_list.append_value_to_back(value, 0)
                current_node = current_node.next_node
        else:
            while current_node is not None:
                for value in reversed(current_node.values):
                    if int(value) < 0:
                        continue
                    try:
                        next_linked_list.append_value(value, int(value[0 - i]))
                    except:
                        next_linked_list.append_value(value, 0)
                for value in current_node.values:
                    if int(value) < 0:
                        try:
                            next_linked_list.append_value(value, int(value[0 - i]))
                        except:
                            next_linked_list.append_value(value, 0)
                current_node = current_node.next_node
        current_list = next_linked_list
        index = 0
        temp_node = current_list.head
        if is_print:
            while temp_node.next_node is not None:
                print(f"{index} : {temp_node}")
                index += 1
                temp_node = temp_node.next_node
            print(f"{index} : {temp_node}")
    temp_node = current_list.head
    while temp_node is not None:
        temp_node.sort_values()
        temp_node = temp_node.next_node
    return current_list

inp = input("Enter Input : ").split()
linked_list = LinkedList(Node([inp[0]], None))
for i in range(len(inp)):
    value = inp[i]
    if i != 0:
        linked_list.append(value)
    if len(value) > linked_list.max_base_length:
        if value[0] == "-":
            value = value[1:]
        linked_list.set_max_base_length(len(value))

before = linked_list

if not is_all_equal(inp):
    after = radix_sort(linked_list, True)
    print("------------------------------------------------------------")
    print(f"{linked_list.max_base_length} Time(s)")
else:
    after = radix_sort(linked_list)
    print("------------------------------------------------------------")
    print(f"{0} Time(s)")

print("Before Radix Sort ", end=": ")
current_node = before.head
while current_node.next_node is not None:
    if len(current_node.values) != 0:
        for value in current_node.values:
            print(f"{value} -> ", end="")
    current_node = current_node.next_node
for value in current_node.values:
    if value == current_node.values[-1]:
        print(f"{value}", end="")
    else:
        print(f"{value} -> ", end="")
print()

print("After  Radix Sort ", end=": ")
current_node = after.tail
flag = False
while current_node is not None:
    if len(current_node.values) != 0:
        for value in current_node.values:
            if int(value) > 0:
                if flag:
                    print(f"-> {value} ", end="")
                else:
                    print(f"{value} ", end="")
                    flag = True
    current_node = current_node.prev_node
current_node = after.head
while current_node is not None:
    if len(current_node.values) != 0:
        for value in current_node.values:
            if int(value) <= 0:
                if flag:
                    print(f"-> {value} ", end="")
                else:
                    print(f"{value} ", end="")
                    flag = True
    current_node = current_node.next_node
