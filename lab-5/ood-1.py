class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def appendHead(self,value):
        node = Node(value,self.head)
        self.head = node

    def appendLast(self,value):
        self.find_tail()
        if self.head is None:
            self.appendHead(value)
            return
        self.tail.next = Node(value)

    def find_tail(self):
        try:
            t = self.head
            while t.next != None:
                t = t.next
            self.tail = t
        except:
            pass

    def removeLast(self):
        try:
            self.find_tail()
            t = self.head
            if t == None:
                print("Error!!!")
                return
            if t == self.tail or t.next is None:
                self.head = None
                self.tail = None
                return
            while t.next != None:
                temp = t
                t = t.next
            temp.next = None
        except:
            print("Error!!!")

    def rename(self, newName):
        try:
            self.find_tail()
            self.tail.value = newName
        except:
            print("Error!!!")

    def printList(self):
        try:
            t = self.head
            while t.next != None:
                print(f"{t.value} -> ",end="")
                t = t.next
            print(f"{t.value}")
        except:
            print("Linklist is empty!")

    def printListWithNoDuplicate(self):
        temp = ""   
        t = self.head
        output = ""
        while t != None:
            if t.value not in temp.split():
                output += t.value + " -> "
                temp += t.value + " "
            t = t.next
        if "->" in output[-3:]:
            output = output[:-3]
        if output == "":
            print("Linklist is empty!")
        else:
            print(output)

def convertToLinkList(ls):
    for i in range(len(ls)):
        if i == 0:
            myLinkList = LinkedList()
            myLinkList.appendHead(ls[i])
        else:
            myLinkList.appendLast(ls[i])
    return myLinkList

print("*** My Favourite Keynote ***")
listSong = input("Enter Input / List of operation : ").split(' / ')
song = listSong[0].split(" ")
oparations = listSong[1].split(", ")
myLinkList = convertToLinkList(song)
myLinkList.printList()

for o in oparations:
    [op, *value] = o.split()
    if op == "A":
        myLinkList.appendLast(value[0])
    elif op == "D":
        myLinkList.removeLast()
    elif op == "R":
        myLinkList.rename(value[0])

myLinkList.printList()
myLinkList.printListWithNoDuplicate()

