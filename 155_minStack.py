class MinStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = [2 ** 31 - 1]
        self.minElement = 2 ** 31 - 1

    def push(self, val: int) -> None:
        if val < self.minElement:
            self.minElement = val
        self.stack1.append(val)
        self.stack2.append(self.minElement)
        

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()
        self.minElement = self.stack2[-1]
        

    def top(self) -> int:
        return self.stack1[-1]
        

    def getMin(self) -> int:
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Problem 155: https://leetcode.com/problems/min-stack/