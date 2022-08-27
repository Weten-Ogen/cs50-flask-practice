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


"""This is how to use Stack in checking for delimeter errors"""
def is_matched(expr):
  lefty="({["
  righty ="]})"
  S = ArrayStack()
  for c in expr:
    if c in lefty:
      S.push(c)
    elif c in righty:
      if  S.is_empty():
        return False
      if righty.index(c) != lefty.index(S.pop()):
        return False
    return S.is_empty()



cam = '[x + 2] - [3 + y]'
print(is_matched(cam))