"""
a classic

approach:
    
    stack of value pairs:
        each push has two elements, [the value being pushed, the current min]
        when pushing, how to decide what the current min value is:
            current min = min(top of stack's min, current value being pushed)
        the rest is trivial
"""

class MinStack:

    def __init__(self):
        self.stack = []
        # in some member functions, I set stack = self.stack to avoid writing self so much

    def push(self, val: int) -> None:
        stack = self.stack 
        if stack:
            stack.append([val, min(stack[-1][1], val)])
        else: # the stack was empty, no need to check existing min
            stack.append([val, val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
