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

class Queue():

    def __init__(self):
        self.stack_for_queue = Stack()
        self.queue = Stack()

    def push(self, num):
        self.stack_for_queue.push(num)

    # 스텍에서 저장된값을 큐로 옮겨줄 함수 구현 --> 1,2,3을 스텍에 넣었다면 큐에 3,2,1 을 집어넣어야 pop함수를 통해 1부터 꺼내올 수 있으므로
    def stack_to_queue(self):
        if self.stack_for_queue:
            while self.stack_for_queue:
                self.queue.push(self.stack_for_queue.pop())
        else:
            raise Exception("Nothing in stack and queue")

    def pop(self):
        if self.queue:
            return self.queue.pop()
        else:
            raise Exception("Queue is empty")

def test_queue():

    newqueue = Queue()
    newqueue.push(1)
    newqueue.push(2)
    newqueue.push(3)
    print(newqueue.stack_for_queue.stack)
    print(newqueue.queue.stack)
    newqueue.stack_to_queue()
    print(newqueue.stack_for_queue.stack)
    print(newqueue.queue.stack)
    print(newqueue.pop())
    print(newqueue.pop())
    print(newqueue.pop())
    print(newqueue.stack_for_queue.stack)
    print(newqueue.queue.stack)

test_queue()
