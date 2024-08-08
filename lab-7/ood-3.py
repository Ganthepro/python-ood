import re


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root: Node = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            temp = self.root
            while temp:
                if data < temp.data:
                    if temp.left == None:
                        temp.left = Node(data)
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = Node(data)
                        break
                    else:
                        temp = temp.right
        return self.root
    
    def findChild(self, data):
        temp = self.root
        while temp:
            if temp.data == data:
                return temp
            if data < temp.data:
                if temp.left == None:
                    temp = temp.left
                elif temp.left.data == data:
                    return temp.left
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp = temp.right
                elif temp.right.data == data:
                    return temp.right
                else:
                    temp = temp.right
        return []
    
    def dfs(self, node):


T = BST()
inp, val = input('Enter the BST values and search value: ').split(', ')
inp = list(map(int, inp.split()))
for i in inp:
    root = T.insert(i)
child = T.findChild(int(val))
print(f"Input: root = {inp}, val = {val}")
if child == []:
    print(f"Output: {[]}")
else:
    # print(f"Output: {list(map(int, [str(child), str(child.left), str(child.right)]))}")
    T.printTree(child)