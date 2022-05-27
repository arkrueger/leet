### GRIND 75 SECOND PASS ###

"""
approach:
    
    stack:
        loop through the string
        add open parentheses to a stack
        when we encounter a closing parenthesis, pop the stack and check for compatibility (this "sinks" compatible bracket pairs)
            return False if:
                the stack is empty (nothing to pop, i.e. an orphan closing bracket)
                an incompatible bracket is popped
        return True if the loop runs to completion and the stack is empty
    
    alternative stack:
        loop through the string
        for each opening bracket, push the corresponding closing bracket onto a stack
        when we encounter a closing bracket, pop the stack and compare
        if they are unequal, return False
        return True if the loop runs to completion and the stack is empty
    
"""
# alternative stack and sink approach
# T: O(n)
# S: O(n) (at most 0.5*n if the result is true, at worst n if the result is False)
class Solution:
    def isValid(self, s: str) -> bool:
        openers     = ["(", "[", "{"] # opening brackets
        closers     = [")", "]", "}"] # closing brackets
        stack       = [] # stack to hold our closing brackets
        for i in s:
            if i in openers: # opening bracket, add its complement closing bracket to the stack
                complement = closers[openers.index(i)]
                stack.append(complement)
            else: # closing bracket, check if it matches the expected closing bracket from the stack
                # return false if the stack is empty (if we are on a closer, it should not be empty - if it is, game over)
                if stack == [] or i != stack.pop():
                    return False
        return True if stack == [] else False
                

# stack and sink approach
# T: O(n)
# S: O(n) (at most 0.5*n if the result is true, at worst n if the result is False)
class __Solution:
    def isValid(self, s: str) -> bool:
        openers     = ["(", "[", "{"] # opening brackets
        closers     = [")", "]", "}"] # closing brackets
        # compatible  = ["()", "[]", "{}"]
        stack       = [] # stack to hold our opening brackets
        for i in s:
            if i in openers:
                stack.append(i)
                print("appending ", i)
            # exit early if the stack is empty (it will not be if we just added an opener)
            elif stack == []: # if current is a closer and the stack is empty, game over
                return False
            else: # if current is a closer and stack is not empty, check for compatibility
                # checking if our current closer and latest opener are of the same type by comparing their indices in the openers/closers lists
                if closers.index(i) != openers.index(stack.pop()):
                    return False
        return True if stack == [] else False # hedging against the case where there are remaining openers without complements
        