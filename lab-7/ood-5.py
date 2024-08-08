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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, data):
        temp = self.root
        if temp.data == data:
            return "Root"
        while temp:
            if temp.data == data:
                return temp
            if data < temp.data:
                if temp.left == None:
                    temp = temp.left
                elif temp.left.data == data:
                    if temp.left.left != None or temp.left.right != None:
                        return "Inner"
                    if temp.right.left == None or temp.right.right == None:
                        return "Leaf"
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp = temp.right
                elif temp.right.data == data:
                    if temp.right.left != None or temp.right.right != None:
                        return "Inner"
                    if temp.right.left == None or temp.right.right == None:
                        return "Leaf"
                else:
                    temp = temp.right
        return "Not exist"
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
print(T.checkpos(inp[0]))