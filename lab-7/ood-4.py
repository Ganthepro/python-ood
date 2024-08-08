from re import T


class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
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
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = Node(val)
                        break
                    else:
                        temp = temp.right
        return self.root
    
    def delete(self,temp, data):
        while temp:
            if temp.data == data:
                return temp
            if data < temp.data:
                if temp.left == None:
                    temp = temp.left
                elif temp.left.data == data:
                    temp = None
                    # return temp.left
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp = temp.right
                elif temp.right.data == data:
                    temp = None
                    # return temp.right
                else:
                    temp = temp.right
        return self.root
        
                
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
        tree.delete(tree.root,int(val))
        print(f"delete {val}")
    elif opt == 'i':
        tree.insert(int(val))
        print(f"insert {val}")
    printTree90(tree.root)