"""

thinking:
    
    are we only parsing integers? yes
    we can see whitespace before the number. can we see letters? yes, but they are not whitespace and preempt parsing -> see non-whitespace before number, don't parse
    what do we return if we aren't able to parse anything? -> doesn't specify, maybe 0?
    conditionals while searching for the start of the integer:
        + -> number is positive, increment index
        "#" without a sign -> number is positive, do not increment index ("#" indicates a digit)
        - -> number is negative, increment index
    conditionals wihle searching for the end of the integer:
        non-digit -> terminate parsing
    
    is adding sequentially larger numbers an inefficient operation? not sure
        maybe, because we're starting from the leftmost side and multiplying by 10 each iteration and adding the next digit rather than multiplying by its final power a single time
        
    

approach:
    
    iterative:
        T: O(n) worst case when the int substring is at the end of the string 
        S: O(1)
        vars:
            i = 0 for index
            sign = 1 for positive/negative
            ans = 0 for the parsed integer
        iterate over the string with index i
            if we see a digit, break
            if we see a + sign, increment i and break
            if we see a - sign, set sign to -1, increment i, and break
        iterate over the string starting with index i
            if the next number is not a digit, break
            otherwise
                multiply ans by 10 and add sign times the current character (digit)
                increment i
        return ans
            
    reverse iterative:
        this method prevents multiplying ans by itself so many times (maybe more efficient? should implement to test the idea)
        scan the string
            record the start of the int string
            record the end of the int string
        start with the final character in the int string and move backwards
            multiply the current character (digit) by 10^pw and add it to ans
        
        
    
"""

# iterative
# T: O(n) worst case, traverse whole string
# S: O(1) no additional data structures created
class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT = -2147483648
        MAX_INT = 2147483647
        MAX_INT_PRE = MAX_INT//10
        MIN_INT_PRE = MIN_INT//10
        i = 0 # string index
        sign = 1 # negative or positive
        ans = 0 # store the result here
        oneToNine = list("123456789")
        mapping = {c:v for c,v in zip(["0"]+oneToNine,range(0,10))}
        validBeforeInt = [" ", "-", "+"]
        # find the start of the int and set the sign
        while i < len(s):
            c = s[i]
            if c not in validBeforeInt+oneToNine:
                if c == "0":
                    break
                return ans # will be 0 at this stage
            elif c in oneToNine:
                break
            elif c in ["-","+"]:
                sign = -1 if c == "-" else 1
                i += 1
                break
            i += 1
        # remove any leading zeros
        while i < len(s):
            c = s[i]
            if c != "0":
                break
            i += 1
        # parse the int
        while i < len(s):
            c = s[i]
            if c not in ["0"]+oneToNine:
                break
            if ans < MIN_INT_PRE: return MIN_INT
            if ans > MAX_INT_PRE: return MAX_INT
            ans *= 10
            ans += mapping[c]*sign
            i += 1
        if ans < MIN_INT: return MIN_INT
        if ans > MAX_INT: return MAX_INT; print("ran")

        return ans
