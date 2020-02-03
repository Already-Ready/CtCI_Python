class SetofStacks():

    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.stacks = []
        self.sizes = []
        self.mini_stack = []

    def IndexofTop(self):
        if self.stacks:
            top_stack = self.stacks[-1]
            top_position = top_stack[-1]
            return top_position
        else:
            raise Exception("Stacks is empty")

    def TopStack(self):
        if self.stacks:
            top_stack = self.stacks[-1]
            return top_stack
        else:
            raise Exception("Stacks is empty")

    def IndexofTopStack(self):
        if self.stacks:
            return len(self.stacks) - 1
        else:
            raise Exception("Stacks is empty")

    def isfull(self,stacknum):
        if self.stacks:
            return len(self.stacks[stacknum]) == self.sizes[stacknum]
        else:
            raise Exception("Stacks is empty")

    def isempty(self, stacknum):
        if self.stacks:
            return self.sizes[stacknum] == 0
        else:
            raise Exception("Stacks is empty")

    def push(self, item):
        # 초기 stacks가 비어있을 때 삽입해주는 경우 처리해주고,
        if not self.stacks:
            self.mini_stack.append(item)
            self.stacks.append(self.mini_stack)
            self.sizes.append(1)
            self.mini_stack = []

        else:
            # stacks는 비어있지 않지만--> 특정 stack이 stacksize만큼 다 차있는 경우 처리해주고,
            if len(self.TopStack()) == self.stacksize:
                self.mini_stack.append(item)
                self.stacks.append(self.mini_stack)
                self.mini_stack = []
                self.sizes.append(1)
            # stack에 여유공간이 있는 경우를 처리해준다.
            else:
                self.TopStack().append(item)
                self.sizes[self.IndexofTopStack()] += 1

    def pop(self):
        if not self.stacks:
            raise Exception("Stacks is empty")
        else:
            pop_num = self.TopStack().pop()
            # top stack에서 top 인 값을 pop한 후 해당 stack이 빈 스텍이 된다면? --> 해당 스텍도 stacks에서 지워줘야한다.
            if not self.TopStack():
                self.stacks.pop()
                return pop_num
            else:
                return pop_num

    def peek(self):
        if not self.stacks:
            raise Exception("Stacks is empty")
        else:
            return self.TopStack()[-1]


def stacks():
    newstack = SetofStacks(3)
    newstack.push(1)
    print(newstack.stacks)
    newstack.push(2)
    print(newstack.stacks)
    newstack.push(3)
    print(newstack.stacks)
    newstack.push(4)
    print(newstack.stacks)
    newstack.push(5)
    print(newstack.stacks)
    print(newstack.peek())
    newstack.pop()
    print(newstack.stacks)
    newstack.pop()
    print(newstack.stacks)
    print(newstack.peek())
    newstack.pop()
    print(newstack.stacks)
    print(newstack.peek())


stacks()
