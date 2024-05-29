class MyQueue:

    def __init__(self):
        self.inQueue = []
        self.outQueue = []

    def push(self, x: int) -> None:
        self.inQueue.append(x)
        
    def pop(self) -> int:
        if self.outQueue:
            return self.outQueue.pop()
        else:
            while self.inQueue != []:
                self.outQueue.append(self.inQueue.pop())
            return self.outQueue.pop()

    def peek(self) -> int:
        if self.outQueue:
            return self.outQueue[-1]
        else:
            while self.inQueue != []:
                self.outQueue.append(self.inQueue.pop())
            return self.outQueue[-1]

    def empty(self) -> bool:
        if self.inQueue == [] and self.outQueue == []:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Problem 232: https://leetcode.com/problems/implement-queue-using-stacks/description/