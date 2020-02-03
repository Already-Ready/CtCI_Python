

class Stack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def pop(self):
        if not self.stack:
            return None
        else:
            # 지우는 값이 지금 최소값 스텍의 헤드랑 같다면 최소값 스텍에서도 지워줘야한다.
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
                return self.stack.pop()
            # 지우는 스텍의 헤드값이 최소값이 아니라면? --> min_stack은 변하지 않는다
            else:
                return self.stack.pop()

    def push(self, num):
        self.stack.append(num)
        if not self.min_stack:
            self.min_stack.append(num)
        else:
            if num <= self.min_stack[-1]:
                self.min_stack.append(num)
            else:
                pass

    def size(self):
        return len(self.stack)


    def min(self):
        return self.min_stack[-1]

def minstack():
    stack = Stack()
    stack.push(4)
    print("log1:", stack.min())
    stack.push(4)
    print("log2:", stack.min())
    stack.push(50)
    print("log3:", stack.min())
    stack.push(50)
    print("log4:", stack.min())
    stack.push(50)
    print("log5:", stack.min())
    stack.push(3)
    print("log6:", stack.min())
    stack.push(3)
    print("log7:", stack.min())
    stack.push(50)
    print("log8:", stack.min())
    stack.push(50)
    print("---------")
    stack.pop() #50 삭제
    print("log9:", stack.min())
    stack.pop() # 50 삭제
    print("log10:", stack.min())
    stack.pop() # 3 삭제 --> 아직 3이 남아있으므로 최소값은 여전히 3
    print("log11:", stack.min())
    stack.pop() # 3삭제 --> 최소값은 4가됨
    print("log12:", stack.min())
    print(stack.stack)


minstack()