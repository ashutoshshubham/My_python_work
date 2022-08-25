#create circular singly linked list

class Node:
    def __init__(self,value):
        self.value = value
        self.tail = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return ("CSLL  Created")

#insertion

    def insertCSLL(self,value,location):
        if self.head is None:
            return ("CSLL DNE")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

#traversal

    def traversalCSLL(self):
        if self.head == None:
            print("CSLL DNE")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode =tempNode.next
                if tempNode == self.tail.next:
                    break

#searching

    def searchCSLL(self,nodeValue):
        if self.head == None:
            print("CSLL DNE")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return (tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return ("Value DNE")
                    break

#deletion

    def deleteNode(self,location):
        if self.head == None:
            print("CSLL DNE")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

#delete entire CSLL
    def deleteCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail =None
        print("CSLL Deleted")






circularSLL = CircularSLL()

print(circularSLL.createCSLL(1))
print([node.value for node in circularSLL])

circularSLL.insertCSLL(2,0)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(6,2)
circularSLL.insertCSLL(5,3)
print([node.value for node in circularSLL])

circularSLL.traversalCSLL()

print(circularSLL.searchCSLL(8))

circularSLL.deleteNode(-7)         #to delete value at index 1, give any negative value
print([node.value for node in circularSLL])

circularSLL.deleteCSLL()
