#levelOrder Traversal in BT using Linked List use Queue using Linked List
import queueUsingLinkedList as queue

#creation of BT Using Linked List

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

#preOrder Traversal

def preOrderTraversal(rootNode):
    if not rootNode:
        # print ("Tree DNE")                  #this line is not working.....why????🤨🤨
        return                                #this is working....
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

#inOrder Traversal

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

#postOrder Traversal

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

#levelOrder Traversal

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

#searching Method

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "BT DNE"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not Found"

#insertion Method

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Success"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Success"

#delete Node

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value == dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild == dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild == dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode,node):
    if not rootNode:
        return "BT DNE"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "Node Deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild) 
        return "Failed to Delete"

#delet entire BT

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    print ("Deleted")





    
newBT = TreeNode("Drink")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

# preOrderTraversal(newBT)
# # print('\n')
# inOrderTraversal(newBT)
# # print('\n')
# postOrderTraversal(newBT)
# # print('\n')
# levelOrderTraversal(newBT)
# # print('\n')
# print(searchBT(newBT, "Tea"))
# print(searchBT(newBT, "MURGA"))

# newNode = TreeNode("cola")
# print(insertNodeBT(newBT, newNode))
# levelOrderTraversal(newBT)

# deepestNode = getDeepestNode(newBT)
# print(deepestNode.data)

# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, newNode)
# levelOrderTraversal(newBT)

# deleteNodeBT(newBT, 'Tea')
# levelOrderTraversal(newBT)

deleteBT(newBT)
levelOrderTraversal(newBT)