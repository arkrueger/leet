"""
thinking:
    everything always evaluates down to a left | right | operand phrase
    can we represent this as a tree?
        ["2","1","+","3","*"]
            *
        3       +
            1       2                -> 3*(1+2) 
    
approach:
    two stacks, iterative
        left as empty list
        set right as the reverse of tokens (it's just easier)
        looping while we still have elements in right and left:
            pop right and push onto left (do until left is big enough to look for a math phrase)
            check if we have num-num-operator
                pop the top three from left, perform the computation, and push the result onto left
            exit case:
                if left has only one element and right is empty, our answer is in left so return it
    
    what if we want to avoid reversing tokens into right?
        set 
        
"""

# two stacks, iterative
# T: O(n)
# S: O(n)
class __Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return tokens[0]
        ops = ["+", "-", "*", "/"] # operators
        # two stacks
        left = []
        right = tokens[::-1]
        while left or right:
            if len(left) < 2 and not right: # base case, we have exhausted tokens and our result is in left
                return left[0] 
            if right: # pop right and push onto left if right has tokens to give
                left.append(right.pop())
            if len(left) < 3: # if left is too small, pop right and push in the next iteration
                continue
            # check if we have a math phrase
            if left[-3] not in ops and left[-2] not in ops and left[-1] in ops: # we have num-num-operator
                o, b, a = left.pop(), left.pop(), left.pop()
                left.append(self.compute(a,b,o))
    
    # helper function to do the math
    def compute(self, a: str, b: str, op: str) -> int:
        a, b = int(a), int(b)
        if op == "+": return a+b
        if op == "-": return a-b
        if op == "*": return a*b
        if op == "/": return trunc(a/b)

# two stacks, iterative but we don't reverse tokens
# T: O(n)
# S: O(1) note that this is less than the original because we don't copy tokens
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        print("running two stacks iterative but we don't reverse tokens")
        if len(tokens) < 2:
            return tokens[0]
        ops = ["+", "-", "*", "/"] # operators
        # two stacks
        left = []
        right = tokens
        while left or right:
            if len(left) < 2 and not right: # base case, we have exhausted tokens
                return left[0] 
            if len(left) < 3: 
                left.append(right.pop())
                continue
            # check if we have a math phrase
            if left[-3] in ops and left[-2] not in ops and left[-1] not in ops: # we have num-num-operator
                print("i ran")
                a, b, o = left.pop(), left.pop(), left.pop()
                left.append(self.compute(a,b,o))
            else:
                left.append(right.pop())
    
    # helper function to do the math
    def compute(self, a: str, b: str, op: str) -> int:
        a, b = int(a), int(b)
        if op == "+": return a+b
        if op == "-": return a-b
        if op == "*": return a*b
        if op == "/": return trunc(a/b)

"""

# iterative solution (I don't think this is a good strategy, fails test cases)
# T: O()
# S: O()
class __Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return tokens[0]
        ops = ["+", "-", "*", "/"] # operators
        stack = []
        l = r = 0
        # find the first number-number-operator pattern in the tokens list
        for i, a in enumerate(tokens):
            b, c = tokens[i+1], tokens[i+2]
            if (a not in ops) and (b not in ops) and (c in ops):
                res = self.compute(a,b,c)
                l = i-1
                r = i+3
                break
        while l >= 0 or r < len(tokens)-1:
            if tokens[r] in ops: # then our terms are result and tokens[l]
                a, b, o = tokens[l], res, tokens[r]
                l -= 1; r += 1
            else: # then our terms are result and tokens[r], and our operator is to the right of that
                a, b, o = res, tokens[r], tokens[r+1]
                r += 2 # only move r forward, don't move l backward
            # perform the operation
            res = self.compute(a, b, o)
            print(res)
            
        return res
        
    # helper function to do the math
    def compute(self, a: str, b: str, op: str) -> int:
        a, b = int(a), int(b)
        if op == "+": return a+b
        if op == "-": return a-b
        if op == "*": return a*b
        if op == "/": return trunc(a/b)        
"""