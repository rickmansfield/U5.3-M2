"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.
You already have a `Stack` class that you've implemented using a dynamic array.
Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.
*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""
class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack:
    def __init__(self):
        self.storage_stack = Stack()
        self.maxes_stack = Stack()


    def push(self, item):
        """Add a new item onto the top of our stack."""
        pass


    def pop(self):
        """Remove and return the top item from our stack."""
        pass


    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        pass




print("Maxes")
s = MaxStack()
s.push(4)
s.push(5)
s.push(3)
print(s.get_max())
s.push(7)
print(s.get_max())
s.pop()
print(s.get_max())