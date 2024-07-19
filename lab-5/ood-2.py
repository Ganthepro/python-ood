print("***Railway on route***")

class Node:
    def __init__(self, name, next = None, back = None) -> None:
        self.name = name
        self.next = next
        self.back = back

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def appendHead(self, name):
        self.head = Node(name)

    def appendLast(self, name):
        self.find_tail()
        if self.head == None:
            self.appendHead(name)
            return
        t = self.head
        while t.next != None:
            t = t.next
        t.next = Node(name, None, t)

    def find_tail(self):
        try:
            t = self.head
            while t.next != None:
                t = t.next
            self.tail = t
        except:
            pass

    def move(self, start, end, direction = "F"):
        how_much = 0
        output = ""
        self.find_tail()
        if direction == "F":
            output += "Forward Route: "
            t = self.head
            while t.name != start:
                t = t.next
            while t.name != end:
                output += f"{t.name}->"
                how_much += 1
                if t.next == None:
                    t = self.head
                else:   
                    t = t.next
            output += f"{t.name}"
        elif direction == "B":
            output += "Backward Route: "
            t = self.head
            while t.name != start:
                t = t.next
            while t.name != end:
                output += f"{t.name}->"
                how_much += 1
                if t.back == None:
                    t = self.tail
                else:
                    t = t.back
            output += f"{t.name}"
        output += f",{how_much}"
        return how_much, output

    def __str__(self) -> str:
        t = self.head
        output = ""
        while t.next != None:
            output += f"{t.name} -> "
            t = t.next
        output += f"{t.name}"
        return output

inp = input("Input Station name/Source, Destination, Direction(optional): ").split("/")
stations = inp[0].split(",")
option = inp[1].split(",")
railway = LinkedList()

def move_forward():
    for station in stations:
        railway.appendLast(station)
    temp, output = railway.move(option[0], option[1], "F")
    print(output)

def move_backward():
    for station in stations:
        railway.appendLast(station)
    temp, output = railway.move(option[0], option[1], "B")
    print(output)

try:
    if option[2] == "F":
        move_forward()
    elif option[2] == "B":
        move_backward()
except:
    for station in stations:
        railway.appendLast(station)
    temp, output = railway.move(option[0], option[1], "F")
    temp2, output2 = railway.move(option[0], option[1], "B")
    if temp < temp2:
        print(output)
    elif temp > temp2:
        print(output2)
    else:
        print(output)
        print(output2)