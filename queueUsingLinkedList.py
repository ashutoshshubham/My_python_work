#creation

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return (' '.join(values))

#enqueue Method
   
    def enqueue(self,value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

#isEmpty Method
  
    def isEmpty(self):
        if self.linkedList.head == None:
            return True 
        else:
            return False

#dequeue Method

    def dequeue(self):
        if self.isEmpty():
            return("Empty Queue")
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

#peek Method

    def peek(self):
        if self.isEmpty():
           return("Empty Queue")
        else:
            return self.linkedList.head 

#delete Method

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
        return("Queue Deleted")


custQueue = Queue() 

custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
custQueue.enqueue(4)
print(custQueue)

print(custQueue.dequeue())
print(custQueue)

print(custQueue.peek())

print(custQueue.delete())

