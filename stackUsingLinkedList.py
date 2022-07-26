#creation

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return("\n".join(values))

#isEmpty Method

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

#push Method

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

#pop Method

    def pop(self):
        if self.isEmpty():
            return ("Stack is Empty")
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

#peek Method

    def peek(self):
        if self.isEmpty():
            return ("Stack is Empty")
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

#delete Stack

    def delete(self):
        self.LinkedList.head = None
        print("Stack Deleted")




customStack = Stack()

print(customStack.isEmpty())

customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)

# print(customStack)

print(customStack.pop())

print(customStack.peek())

customStack.delete()


            
