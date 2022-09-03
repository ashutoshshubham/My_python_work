#creation

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return ("\n".join(values))

#isEmpty Method
   
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
#isFull Method
   
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

#push Method

    def push(self, value):
        if self.isFull():
            return ("Stack is Full")
        else:
            self.list.append(value)
            return ("Element inserted")

#pop Method

    def pop(self):
        if self.isEmpty():
            return ("Stack is Empty")
        else:
            return self.list.pop()

#peek Method

    def peek(self):
        if self.isEmpty():
            return("Stack is Empty")
        else:
            return(self.list[len(self.list) - 1])

#delete Stack

    def delete(self):
        self.list = None
        return("Stack Deleted")





customStack = Stack(4)

print(customStack.isEmpty())

print(customStack.isFull())

customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.push(4))
# print(customStack.push(5))

# print(customStack)

print(customStack.pop())

print(customStack.peek())

print(customStack.delete())

