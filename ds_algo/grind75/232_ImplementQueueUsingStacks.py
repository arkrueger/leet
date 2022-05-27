### GRIND 75 SECOND PASS ###
"""
stack flushing approach:
            this is the description from when I did it in C++, copying the approach and trying to implement in python without looking at my C++ code
    have two stacks
    one "input" and one "output"
    all pushing is done on the input stack
    but what happens when we need to pop or peek the queue?
        the output queue has the opposite order of the input stack 
            (therefore popping the output stack obeys FIFO)
        -> if the output stack has elements, pop or peek the output stack
        -> if the output stack is empty, then transfer the whole input stack into the output stack
                this will put that part of the queue in FIFO order in the output stack
                nothing will be pushed onto the output stack until it is empty (this prevents
                    it from going out of order)
"""

# two stacks method
# T: O(1) overall, but intermittently operations will take O(n) where n is current queue size
# S: O(n) where n is the size of the queue
class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    # all pushing is done on the input stack
    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.peek() # checks if outStack is empty and if it is, dumps inStack into outStack
        # pop the output queue if it has elements
        return self.outStack.pop()
        
    def peek(self) -> int:
        if self.outStack:
            return self.outStack[-1]
        # if the output queue is empty, transfer the entire input queue into the output queue
        else:
            self.outStack.extend(self.inStack[-1::-1]) # transfer everything in reverse order from inStack to outStack
            self.inStack = []
            return self.peek() # first conditional will be true now that outStack has elements

    def empty(self) -> bool:
        return (self.outStack == [] and self.inStack == [])


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()