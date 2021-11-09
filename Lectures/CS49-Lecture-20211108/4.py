# Stack class using a linked list as a backing data structure
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
