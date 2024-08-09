class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.root = None

    def __str__(self) -> str:
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            temp = self.root
            while temp:
                if val < temp.data:
                    if temp.left == None:
                        temp.left = Node(val)
                        temp.left.root = temp
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = Node(val)
                        temp.right.root = temp
                        break
                    else:
                        temp = temp.right
        return self.root
    
    def findChild(self, data, node: Node) -> Node:
        if node == None or node.data == data:
            return node
        if data < node.data:
            return self.findChild(data, node.left)
        return self.findChild(data, node.right)
    
    def findChildNum(self, data, node: Node) -> int:
        if node == None or node.data == data:
            return node.data
        if data < node.data:
            return self.findChild(data, node.left)
        return self.findChild(data, node.right)
    
    def changeChildValue(self, data, val, node: Node) -> Node:
        if node == None or node.data == data:
            node.data = val
            return node
        if data < node.data:
            return self.changeChildValue(data, val, node.left)
        return self.changeChildValue(data, val, node.right)
    
    def findInorderSuccessor(self, node: Node, flag = False) -> int:
        if not flag:
            if node.right == None:
                return None
            return self.findInorderSuccessor(node.right, True)
        else:
            if node.left == None:
                return node
            return self.findInorderSuccessor(node.left, flag)
        
    def deleteChild(self, successor, node: Node, tempNode: Node, flag = False):
        if node == None or node.data == successor.data:
            if node.root.left == node:
                node.root.left = None
            elif node.root.right == node:
                node.root.right = None
            if node.right:
                node.root.left = node.right
            elif node.left:
                node.root.left = node.left
            tempNode.data = node.data
            return node
        if successor.data < node.data:
            return self.deleteChild(successor, node.left, tempNode, True)
        return self.deleteChild(successor, node.right, tempNode)
        
    def deleteSelf(self, successor, node: Node):
        if node == self.root and successor == node:
            if node.left == node.right:
                self.root = None
                return
            if successor.left:
                self.root = successor.left
            elif successor.right:
                self.root = successor.right
            return
        else:
            if node != None:
                if node == successor:
                    if node.root.left == node:
                        node.root.left = None
                    elif node.root.right == node:
                        node.root.right = None
                self.deleteSelf(successor, node.left)
                self.deleteSelf(successor, node.right)

    
    def delete(self, data):
        child = self.findChild(data, self.root)
        if child == None:
            print("Error! Not Found DATA")
            return
        successor = self.findInorderSuccessor(child)
        if successor:
            self.deleteChild(successor, self.root, child)
        else:
            self.deleteSelf(child, self.root)
        
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    opt, val = i.split()
    if opt == "d":
        print(f"delete {val}")
        tree.delete(int(val))
    elif opt == 'i':
        print(f"insert {val}")
        tree.insert(int(val))
    printTree90(tree.root)