"""
A stack is a type of data structure that stores items sequentially and allows access to the top only.

A stack is a LIFO data structure (Last in First Out)
"""

class Stack(object):
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        return self.data.pop(-1)
    
    def __repr__(self) -> str:
        return str(self.data)


stack = Stack()

print(stack)

stack.push(8)
stack.push(9)

stack.pop()

print(stack)

stack.push(199)

print(stack)