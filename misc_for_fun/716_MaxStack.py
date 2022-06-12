"""
official solutions:

    two-value stack with temporary stack:
        stacks elements are lists containing two values [val, max]
        when pushing, current max is max(pushed val, previous element's recorded max)
        when peeking max, trivial, just return top's max
        when popping max,
            record the max listed at the top (self[-1][1]) b/c that's the actual max
            pop elements off the stack onto a second temporary stack
            discard the max when we find it
            now we need to update all of the recorded maxes in the temporary stack when we push them back onto the main stack
            to do this, just call the member push function while the temp stack is not empty, it will re-build the max values
    
    
    doubly linked list with treemap:
        DLL lets us remove internal elements in O(1) time
    
"""

class __MaxStack(list):
    def push(self, x: int) -> None:
        m = max(x, self[-1][1]) if self else x
        self.append((x,m))
        
    def pop(self) -> int:
        return list.pop(self)[0]

    def top(self) -> int:
        return self[-1][0]

    def peekMax(self) -> int:
        return self[-1][1]

    def popMax(self) -> int:
        m = self[-1][1]
        b = [] # this is our temporary stack to hold popped elements while we look for max
        while self[-1][0] != m:
            b.append(self.pop())
        self.pop()
        map(self.push, reversed(b))
        return m
