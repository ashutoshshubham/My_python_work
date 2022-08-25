#creation of Singly Linked List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

#insertion

    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:                # insert at beginning of SLL
                newNode.next = self.head
                self.head = newNode
            elif location == 1:              # insert at end of SLL
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:                            # insert at any other place
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

#traversal
    
    def traverseSLL(self):
        if self.head == None:
            print("SLL DNE")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

#searching

    def searchSLL(self,nodeValue):
        if self.head is None:
            return("LL DNE")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return (node.value)
                node = node.next
            return ("Value DNE")

#deletetion

    def deleteNode(self, location):
        if self.head == None:
            return ("LL DNE")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head 
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while  index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

#delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("LL DNE")
        else:
            self.head = None
            self.tail = None
            print("Deleted")


singlyLinkedList = SLinkedList()

# node1 = Node(1)
# singlyLinkedList.head = node1
# singlyLinkedList.head.next = None
# singlyLinkedList.tail = node1

singlyLinkedList.insertSLL(2,0)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,-1)
singlyLinkedList.insertSLL(5,-1)
singlyLinkedList.insertSLL(8,-1)
singlyLinkedList.insertSLL(7,-1)
print([node.value for node in singlyLinkedList])

# singlyLinkedList.traverseSLL()

# print(singlyLinkedList.searchSLL(5))

# singlyLinkedList.deleteNode(2)
# print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteEntireSLL()




