# lets write a Stack class using a python list as a backing data structure
class Stack:
  def __init__(self):
    self.storage = []

  def push(self, item):
    self.storage.append(item)
  
  def pop(self):
    return self.storage.pop()

  def __len__(self):
    return len(self.storage)

s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(len(s))