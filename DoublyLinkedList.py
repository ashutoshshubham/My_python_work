#creation of Doubly Linked List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def createDLL(self,nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return ("DLL Created")

#insertion
    
    def insertNode(self,nodeValue,location):
        if self.head == None:
            print("DLL DNE")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                # newNode.next = None
                # self.tail.next = newNode
                # newNode.prev = self.tail
                # self.tail = newNode

                          #above OR below........both are correct

                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                # newNode.next = tempNode.next
                # tempNode.next = newNode
                # newNode.prev = tempNode
                # newNode.next.prev = newNode

                          #above OR below........both are correct

                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
                
#traversal

    def traverseDLL(self):
        if self.head == None:
            print("DLL DNE")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

#reverse Traversal

    def reverseTraverseDLL(self):
        if self.head == None:
            print("DLL DNE")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

#searching

    def searchDLL(self,nodeValue):
        if self.head is None:
            print("DLL DNE")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return ("Value Found")
                tempNode = tempNode.next
            return ("Value DNE")

#deletion

    def deleteNode(self,location):
        if self.head is None:
            print("DLL DNE")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode

#delete entire DLL

    def deleteDLL(self):
        if self.head == self.tail:
            print("DLL DNE")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None 
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("DLL Deleted")




doublyLL = DoublyLinkedList()

print(doublyLL.createDLL(2))
print([node.value for node in doublyLL])

doublyLL.insertNode(1,0)
doublyLL.insertNode(5,1)
doublyLL.insertNode(3,2)
doublyLL.insertNode(4,2)
print([node.value for node in doublyLL])

doublyLL.traverseDLL()

doublyLL.reverseTraverseDLL()

print(doublyLL.searchDLL(7))

doublyLL.deleteNode(1)
print([node.value for node in doublyLL])

doublyLL.deleteDLL()



