class Stack():

    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def isempty(self):
        if self.stack:
            return False
        else:
            return True

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise Exception("stack is empty")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise Exception("stack is empty")

# 가장 작은 값이 위로 오도록
# -- == 다른 하나의 스택의 입장에서는 가장 큰 값이 위로 오도록
def sortstack(stack):

    temp_stack = Stack()

    while stack:
        top = stack.pop()
        trigger = True
        if not temp_stack:
            temp_stack.push(top)
        else:
            while trigger:
                if temp_stack:
                    if top >= temp_stack.peek():
                        temp_stack.push(top)
                        trigger = False
                    else:
                        temp_top = temp_stack.pop()
                        stack.push(temp_top)
                else:
                    temp_stack.push(top)
                    trigger = False

    for _ in range(len(temp_stack)):
        num = temp_stack.pop()
        stack.push(num)

    return stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)
stack.push(3)
print(stack.stack)
print(sortstack(stack).stack)

