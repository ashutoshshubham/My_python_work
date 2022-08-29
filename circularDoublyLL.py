#create circular doubly Linked List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self,nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        print ("CDLL Created")
 
#insertion

    def insertCDLL(self,value,location):
        if self.head == None:
            print("CDLL DNE")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode
                newNode.prev = self.tail

                # newNode.next = self.head
                # newNode.prev = self.tail
                # self.head.prev = newNode
                # self.head = newNode
                # self.tail.next = newNode
            elif location == 1:
                self.tail.next = newNode
                newNode.next = self.head
                self.head.prev = newNode
                newNode.prev = self.tail
                self.tail = newNode

                # newNode.next = self.head
                # newNode.prev = self.tail
                # self.head.prev = newNode
                # self.tail.next = newNode
                # self.tail = newNode
            else:
                tempNode = self.head                #tempNode = Current Node
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                tempNode.next = newNode
                newNode.prev = tempNode
                newNode.next.prev = newNode

                # newNode.next = tempNode.next
                # newNode.prev = tempNode
                # newNode.next.prev = newNode
                # tempNode.next = newNode

#traversal

    def traverseCDLL(self):
        if self.head == None:
            print("CDLL DNE")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode.next == self.head:
                    break
                tempNode = tempNode.next

#reversal traversal
    def reverseTraversal(self):
        if self.head == None:
            print("CDLL DNE")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

#searching

    def searchCDLL(self,nodeValue):
        if self.head == None:
            return ("CDLL DNE")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return ("Node Value Found")
                if tempNode == self.tail:
                    return ("Node Value DNE")
                tempNode = tempNode.next

#deletion

    def deleteNode(self,location):
        if self.head == None:
            print("CDLL DNE")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    # self.tail.next = self.head.next
                    # self.head.prev = self.tail
                    # self.head = self.head.next
                                
                                #OR

                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print("Node Deleted")

#delete entire CDLL

    def deleteCDLL(self):
        if self.head == None:
            print("CDLL DNE")
        else:
            # tempNode = self.head
            # while tempNode:  #!= self.head:
            #     tempNode.next.prev = None
            #     tempNode = tempNode.next
            # self.tail.next = None
            # self.head.prev = None
            # self.head = None
            # self.tail = None

                   #OR

            tempNode = self.head
            while tempNode:   #!= self.tail:
                tempNode.next = None
                tempNode = tempNode.next
            self.tail.next = None
            self.head = None
            self.tail = None
            print("CDLL Deleted")





                


circularDLL = CircularDoublyLinkedList()

circularDLL.createCDLL(2)
print([node.value for node in circularDLL])

circularDLL.insertCDLL(1,0)
circularDLL.insertCDLL(5,1)
circularDLL.insertCDLL(3,2)
circularDLL.insertCDLL(4,3)
print([node.value for node in circularDLL])

circularDLL.traverseCDLL()

circularDLL.reverseTraversal()

print(circularDLL.searchCDLL(25))

circularDLL.deleteNode(2)
print([node.value for node in circularDLL])

print(circularDLL.deleteCDLL())
