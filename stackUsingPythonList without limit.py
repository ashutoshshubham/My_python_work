#creation

class Stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join (values)

#isEmpty Method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

#push Method

    def push(self, value):
        self.list.append(value)
        return ("Element Insered")

#pop Method
   
    def pop(self):
        if self.isEmpty():
            return("No Element in the Stack")
        else:
            return self.list.pop()

#peek Method                           it returns last element of stack

    def peek(self):
        if self.isEmpty():
            return ('No Element in Stack')
        else:
            return(self.list[len(self.list) - 1])

#delete Stack

    def delete(self):
        self.list = None
        return ("Stack Deleted")




customStack = Stack()
print(customStack.isEmpty())

customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)

#print(customStack)   #------->       calls __str__, so list will be reversed and when we use pop method, it will return the element which was inserted first but we want to pop last inserted element.
 
print(customStack.pop())

print(customStack.peek())

print(customStack.delete())
