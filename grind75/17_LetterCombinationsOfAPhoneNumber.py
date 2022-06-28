"""
thinking:

    what happens if we see a 1, is it ignored, is it a space?
        I think it's ignored
        nvm, it will not appear in the input
    
    can we treat this like a tree?
    keep in mind they're not asking for permutations. the letters must be in the same order as the numbers that produced them
    
    is this straightforward? let's map it out:
        digits = "23"
        2 gives us abc, 3 gives us def
        for each digit, we have to explore all options
        pivot on a:
        ad, ae, af
        on b:
        bd, be, bf
        on c:
        cd, ce, cf
        if we had a third digit we would continue with that
        say, 232 -> ada, adb, adc, bda, bdb, bdc, etc
        but how do we get variable levels of nesting based on the number of digits?


approach:

    DFS:
        res = result string
        numToChar = map of digits to character options
        stack = partial combos, initialized to contain the letters of the first digit
        while stack is not empty
            pop the stack
            if the current string length is equal to digits, append string to res
                continue
            if we haven't fully formed a combination string, then
            the current string length is the index in digits of the next digit
            append to stack all combinations of the current string and next digit
                i.e. digits="23", started with ["a","b","c"]
                     so pop "a", check digits[1] and append "ad","ae","af" to the stack
        return res

"""

# iterative DFS
# T: O(4^n) where 4 is the max chars per digit (i.e. 7 and 9) and n is the number of digits
# S: O(n) because the height of the n-ary tree is related to the length of digits
class __Solution:
    def mapNums(self):
        m = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        i = e = 0
        for num in range(2,10):
            e = i + 4 if num == 7 or num == 9 else i + 3
            m[str(num)] = alphabet[i:e]
            i = e
        return m
            
    def letterCombinations(self, digits: str) -> List[str]:
        numToChar = self.mapNums()
        res = []
        stack = list(numToChar[digits[0]]) if digits else [] # why? because leetcode thinks its clever with useless corner cases
        while stack:
            curr = stack.pop()
            # add and move on if we have a fully formed string
            if len(curr) == len(digits):
                res.append(curr)
                continue
            # the length of the current string is the index of the next digit in digits
            for n in numToChar[digits[len(curr)]]:
                stack.append(curr+n)
        return res
                
        
        
        
# coding out leetcode's "backtracking" (it's not really backtracking, but uses backtracking patterns) answer
# just for practice
class Solution:
    def mapNums(self):
        m = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        i = e = 0
        for num in range(2,10):
            e = i + 4 if num == 7 or num == 9 else i + 3
            m[str(num)] = alphabet[i:e]
            i = e
        return m
            
    def letterCombinations(self, digits: str) -> List[str]:
        numToChar = self.mapNums()
        res = []
        # recursive helper function to build the solution
        def backtrack(path): # path is the string being built
            nonlocal digits
            nonlocal res
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            # path, when full, is the same length as digits
            # so len(path) when partially formed gets us the index of the next digit in digits
            for c in numToChar[digits[len(path)]]:
                path.append(c)
                # recurse until the leaves (when path length == digits length)
                backtrack(path) # keep in mind path is longer now, so len(path) is 1 more than it was on this function call
                path.pop() # this prunes the path list after we visit all (if any) of a node's children, i.e. we get rid of the character appended just above (and any appended in the recursive backtrack calls)
        
        backtrack([])
        return res if digits else []
