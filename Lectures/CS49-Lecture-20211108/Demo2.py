"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.
As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.
The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        pass
        
    def enqueue(self, item):
        pass

    def dequeue(self):
        pass


q = QueueTwoStacks()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
a = q.dequeue() # 1
b = q.dequeue() # 2
c = q.dequeue() # 3
print(a, b, c)