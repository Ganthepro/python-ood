class Node:
    def __init__(self,value, next = None):
        self.value = int(value)
        self.next = next

    def __str__(self):
        return str(self.value)

def createList(l=[]):
    head = None
    for num in l:
        t = head
        if t == None:
            head = Node(num)
            continue
        while t.next != None:
            t = t.next
        t.next = Node(num)
    return head

def printList(H):
    while H != None:
        print(H,end=' ')
        H = H.next
    print()

def size(H):
    s = 0
    while H != None:
        H = H.next
        s += 1
    return s

def mergeOrderesList(p,q):
    n = Node(0)
    dummy = n
    t = p
    t2 = q
    while t and t2:
        if t.value < t2.value:
            n.next = t
            t = t.next
        else:
            n.next = t2
            t2 = t2.next
        n = n.next
    if t:
        n.next = t
    elif t2:
        n.next = t2
    dummy = dummy.next
    return dummy

inp = input("Enter 2 Lists : ").split()
L1 = inp[0].split(",")
L2 = inp[1].split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)