#creation

class Queue:
    def __init__(self):
        self.items = []
    def __str__(self):
        values = [str(x) for x in self.items]
        return (" ".join(values))

#isEmpty Method

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
#Enqueue Method

    def enqueue(self, value):
        self.items.append(value)
        return("Element Inserted")

#Dequeue Method

    def dequque(self):
        if self.isEmpty():
            return("Empty Queue")
        else:
            return(self.items.pop(0))

#Peek Method 

    def peek(self):
        if self.isEmpty():
            return("Empty Queue")
        else:
            return(self.items[0])

#Delete Queue

    def delete(self):
        self.items = None
        return("Queue Deleted")


customQueue = Queue()

print(customQueue.isEmpty())

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)

print(customQueue.dequque())

print(customQueue.peek())

print(customQueue.delete())

