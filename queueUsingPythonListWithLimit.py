#creation

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x 
        in self.items]
        return ' '.join(values)

#isFull Method

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

#isEmpty Method

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

#enqueue Method
    
    def enqueue(self,value):
        if self.isFull():
            return ("The Queue is Full")
        else:
            if self.top + 1 == self.maxSize:              #if top pointing towards last element
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:                      #if Queue is empty
                    self.start = 0
            self.items[self.top] = value
            return ("The element is inserted at the end")

#dequeue Method

    def dequeue(self):
        if self.isEmpty():
            return("No element in Queue")
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

#peek Method

    def peek(self):
        if self.isEmpty():
            return("No element in Queue")
        else:
            return self.items[self.start]

#delete Method

    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1
        return ("Queue deleted")

        
     



customQueue = Queue(3)

print(customQueue.isFull())

print(customQueue.isEmpty())

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)                #not printed because size given is 3
print(customQueue)

print(customQueue.dequeue())
print(customQueue)

print(customQueue.peek())

print(customQueue.delete())



