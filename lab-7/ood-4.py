from fastapi.background import P


class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.root = None

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
        if node != None:
            if data == node.data:
                if node.root == None:
                    # node = Node
                    self.root = None
                    return
                # ตั้ง node.left - node.right แทน 
            self.findChild(data, node.left)
            self.findChild(data, node.right)
        # while temp:
        #     if temp.data == data:
        #         return temp
        #     if data < temp.data:
        #         if temp.left == None:
        #             temp = temp.left
        #         elif temp.left.data == data:
        #             return temp.left
        #         else:
        #             temp = temp.left
        #     else:
        #         if temp.right == None:
        #             temp = temp.right
        #         elif temp.right.data == data:
        #             return temp.right
        #         else:
        #             temp = temp.right
        # return temp
    
    def findInorderSuccessor(self, node: Node) -> Node:
        if node != None:
            if node.root == None:
                return None
            if node.right != None:
                temp = node.right
                while temp.left:
                    temp = temp.left
                temp.root.left = temp.right
                return node

    
    def delete(self, data):
        child = self.findChild(data, self.root)
        # print("child:", child)
        if child == None:
            print("Error! Not Found DATA")
            return
        if child.root == None:
            child = None
        # if child == None:
        #     print("Error! Not Found DATA")
        #     return 
        # child = self.findInorderSuccessor(child)
        # print(child)
        
        
                
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