"""
Add a peek method to the Stack class. The peek method should return the value of the top item in the stack without actually removing it from the stack.
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

    def peek(self):
        """Return the last item without removing it"""
        if not self.top:
            return None
        return self.top.data
