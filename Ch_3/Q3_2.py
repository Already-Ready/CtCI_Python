import math

class Stack:

    def __init__(self):
        self.stack = []
        self.min_stack = math.inf

    def pop(self):
        if not self.stack:
            return None
        else:
            return self.stack.pop()

    def push(self, num):
        self.stack.append(num)
        if num < self.min_stack:
            self.min_stack = num
        else:
            pass

    def size(self):
        return len(self.stack)


    def min(self):
        return self.min_stack

def minstack():
    stack = Stack()
    stack.push(50)
    print(stack.min())
    stack.push(100)
    print(stack.min())
    stack.push(30)
    print(stack.min())

minstack()