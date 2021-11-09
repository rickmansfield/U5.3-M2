# a Queue class using a linked list as a backing data structure
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = LinkedListNode(item)

        # check if queue is empty
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is not None:
            old_front = self.front
            self.front = old_front.next

        if self.front is None:
            self.rear = None

        return old_front
