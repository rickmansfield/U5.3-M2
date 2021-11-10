"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.
You already have a `Stack` class that you've implemented using a dynamic array.
Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.
*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*

PLAN
-----
# push?
- push the item on to the storage stack.
- if the maxes stack is empty, or if the item we are pushing is greater than a peek at the top of the maxes stack
  - also push the item on to the top of the maxes stack

# pop?
- store the item to be popped off
- check if the item is on the maxes stack
  - pop the item off the maxes stack

- return the popped item to the caller

# get max
  return a peek at the top of the maxes stack
"""


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is not None:
            popped_node = self.top
            self.top = popped_node.next
            return popped_node

    def peek(self):
        if self.top:
            return self.top.data

# class Stack:
#     def __init__(self):
#         """Initialize an empty stack"""
#         self.items = []

#     def push(self, item):
#         """Push a new item onto the stack"""
#         self.items.append(item)

#     def pop(self):
#         """Remove and return the last item"""
#         # If the stack is empty, return None
#         # (it would also be reasonable to throw an exception)
#         if not self.items:
#             return None

#         return self.items.pop()

#     def peek(self):
#         """Return the last item without removing it"""
#         if not self.items:
#             return None
#         return self.items[-1]


class MaxStack:
    def __init__(self):
        self.storage_stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        """Add a new item onto the top of our stack."""
        self.storage_stack.push(item)

        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
        """Remove and return the top item from our stack."""
        popped_item = self.storage_stack.pop()

        if popped_item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return popped_item

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.maxes_stack.peek()


print("Maxes")
s = MaxStack()
s.push(4)
s.push(5)
s.push(3)
print(s.get_max())
s.push(7)
print(s.get_max())
s.push(7)
s.pop()
print(s.get_max())
