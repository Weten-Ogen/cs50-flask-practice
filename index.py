class Empty(Exception):
  pass


class ArrayStack:
  def __init__(self):
    self._data = []
  
  def is_empty(self):
    return len(self._data) == 0
  
  def __len__(self):
    return len(self._data)
  
  def top(self):
    if self.is_empty():
      raise Empty("The Stack is empty")
    else:
      return self._data[-1]
  
  def pop(self):
    if self.is_empty():
      raise Empty('No element to return')
    else:
      return self._data.pop()
  
  def push(self,e):
     return self._data.append(e)

item = ArrayStack()
item.push(4)
item.push(5)
print(item._data)