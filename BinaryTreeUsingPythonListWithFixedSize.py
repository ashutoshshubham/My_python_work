#creation

class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
#insertion
    
    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return("BT is full")
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return("Value Added")
    
#searching

    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return("Found")
        return("Not Found")
        
#preOrder Traversal

    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)                       #for Left Child, cell[2 * index]
        self.preOrderTraversal(index * 2 + 1)                   #for Right Child, cell[2 * index + 1]

#inOrderTraversal

    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.preOrderTraversal(index * 2)                       #for Left Child, cell[2 * index]
        print(self.customList[index])
        self.preOrderTraversal(index * 2 + 1)                   #for Right Child, cell[2 * index + 1]

#postOrderTraversal
    
    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.preOrderTraversal(index * 2)                       #for Left Child, cell[2 * index]
        self.preOrderTraversal(index * 2 + 1)                   #for Right Child, cell[2 * index + 1]
        print(self.customList[index])
    
#levelOrderTraversal

    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex + 1):
            print(self.customList[i])

#delete a Node

    def deleteNode(self,value):
        #using LevelOrderTraversal
        if self.lastUsedIndex == 0:
            return ("No Node to Delete")
        for i in range (1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return(f"{value} Deleted")

#delete Entire BT

    def deleteBT(self):
        self.customList = None
        return ("BT Deleted")





newBT = BinaryTree(8)

print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))

# print(newBT.searchNode("Hot"))

# newBT.preOrderTraversal(1)

# newBT.inOrderTraversal(1)

# newBT.postOrderTraversal(1)

# newBT.levelOrderTraversal(1)

# print(newBT.deleteNode("Tea"))
# newBT.levelOrderTraversal(1)

print(newBT.deleteBT())





