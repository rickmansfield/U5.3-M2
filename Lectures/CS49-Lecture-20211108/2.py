# lets write a Queue class using a python list as a backing data structure
class Queue:
  def __init__(self):
    self.storage = []

  def size(self):
    return self.__len__()

  def enqueue(self, item):
    self.storage.append(item)
  
  def dequeue(self):
    return self.storage.pop(0)
  
  def __len__(self):
    return len(self.storage)

l = []
l.append(1)
l.append(2)
l.append(3)
print("from list: ", l.pop(0))

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(len(q))
