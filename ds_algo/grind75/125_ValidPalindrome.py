### GRIND 75 SECOND PASS ###
"""
approach:
    iterative / brute force / two pointer:
        trim any non-alphanumeric characters
        start from the middle elements (left and right middle if even, middle-1 and middle+1 if odd)
        two pointers, one to the left middle and one to the right middle
        loop while within bounds of string
            check if left and right are equal
            return False if they are not
        return True if we completed the loop
    
    stack:
        pop characters onto stack until we get to the middle (skip the true middle if size is odd)
        then compare 
    
    easy money:
        worth noting that it's possible to reverse the string using a convenience function, then comparing the strings
        if it's a palindrome, it should read the same forward and backward
"""
# easy money (reverse string and check equality)
# T: O(n) or similar, depends on convenience functions
# S: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        s = re.sub(r"[^A-Za-z0-9]+","", s)
        t = s[::-1]
        return t == s

# stack
# T: O(n)
# S: O(n)
class __Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        s = re.sub(r"[^A-Za-z0-9]+","", s)
        size = len(s)
        s = list(s)
        right = [] # stack will receive second half of the string (i.e. all popped characters until string is halved)
        i = 0
        stop = size//2
        for i in s[:stop]:
            right.append(s.pop())
        if size % 2 == 1:
            s.pop() # get rid of middle character if string is of odd length (this will not affect palindrom....icity?)
        while right != []:
            if right.pop() != s.pop():
                return False
        return True
        
# brute force (you could call this "two pointer")
# T: O(n)
# S: O(1)
class __Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        s = re.sub(r"[^A-Za-z0-9]+","", s)
        size = len(s)
        left, right = size//2-1, size//2
        print(left, " ", right)
        right += 1 if size%2 == 1 else 0 # go to the right of middle if length is odd (i.e. we have a single unique middle)
        while left >= 0 and right <= size-1:
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
        return True