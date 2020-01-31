class MultiStack:
    # push, pop peek isempty isfull indexoftop 구현해야함
    def __init__(self,stacksize):
        self.numstack = 3
        # 실제 데이터가 들어갈 스텍 3개
        self.stack = [0] * (stacksize * self.numstack)
        # 리스트안에 있는 각각의 스텍의 사이즈를 저장하기 위한 리스트
        self.sizes = [0] * self.numstack
        self.stacksize = stacksize

    def IndexOfTop(self,stacknum):
        tail_position = stacknum * self.stacksize
        top_position = tail_position + self.sizes[stacknum] - 1
        return top_position

    def isFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def isEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            raise Exception("stack is full")
        self.sizes[stacknum] += 1
        self.stack[self.IndexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception("stack is empty")
        pop_num = self.stack[self.IndexOfTop(stacknum)]
        self.stack[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return pop_num

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            raise Exception("stack is empty")
        return self.stack[self.IndexOfTop(stacknum)]

def ThreeInOne():
    newstack = MultiStack(2)
    print(newstack.isEmpty(1))
    newstack.push(3, 1)
    print(newstack.stack)
    print(newstack.peek(1))
    print(newstack.isEmpty(1))
    newstack.push(2, 1)
    print(newstack.stack)
    print(newstack.peek(1))
    print(newstack.pop(1))
    print(newstack.peek(1))
    newstack.push(3, 1)
    print(newstack.stack)

ThreeInOne()