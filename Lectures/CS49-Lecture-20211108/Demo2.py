"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.
As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.
The Stack class that you will use has been provided to you.

init-
create 2 stacks; in stack and out stack

enqueue
push a item to the in stack

dequeue
check if the out stack is empty

  while the in stack is not empty
    push the items from the in stack on to the out stack
  
  ?? check for no items and deal with it ??

return the item from the top of the out stack to the caller
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

    def __len__(self):
        return len(self.data)


class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                stack_item = self.in_stack.pop()
                self.out_stack.push(stack_item)

            # if len(self.out_stack) == 0:
            #   raise IndexError("The Queue is Empty, you can not dequeue at this time")

        return self.out_stack.pop()


q = QueueTwoStacks()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
a = q.dequeue()  # 1
b = q.dequeue()  # 2
c = q.dequeue()  # 3
print(a, b, c, d)
