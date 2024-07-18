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
        temp = t
        while t.next != None:
            temp = t
            t = t.next
        print(temp.name)
        t.next = Node(name, None, temp)
        # print(t.next.back)

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
        self.find_tail()
        if direction == "F":
            t = self.head
            while t.name != start:
                t = t.next
            while t.name != end:
                print(f"{t.name}->",end="")
                how_much += 1
                t = t.next
            print(f"{t.name}", end="")
        elif direction == "B":
            t = self.head
            while t.name != start:
                t = t.next
            while t.name != end:
                # print(f"{t.name}->",end="")
                print(t.name)
                how_much += 1
                if t.back == None:
                    t = self.tail
                else:
                    t = t.back
            print(f"{t.name}", end="")
        print(f",{how_much}")

    def __str__(self) -> str:
        t = self.head
        output = ""
        while t.next != None:
            output += f"{t.name} -> "
            t = t.next
        output += f"{t.name}"
        return output

inp = input("Enter Input : ").split("/")
stations = inp[0].split(",")
option = inp[1].split(",")
railway = LinkedList()

def move_forward():
    for station in stations:
        railway.appendLast(station)
    railway.move(option[0], option[1])

def move_backward():
    for station in stations:
        railway.appendLast(station)
    print(railway)
    railway.move(option[0], option[1], "B")

if option[2] == "F":
    move_forward()
elif option[2] == "B":
    move_backward()