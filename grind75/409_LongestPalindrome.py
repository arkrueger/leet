"""
read the question first. it's not the other palindrome question, it's this palindrome question. no, really.

approach:
    
    frequency dict:
        loop through the string and store character frequencies in a dict
        start a running sum
        loop through the frequency dict
            if the frequency is even, add it to the running sum
            if the frequency is odd
                if the running sum is odd:
                    subtract 1 from the frequency and add it to the running sum
                if the running sum is even:
                    add it to the running sum
        return the running sum
   
"""


# frequency dict
# T: O(n) where n is input string length
# S: O(1) scales with small n, but the frequency dict is limited to 54 keys (upper and lower case alphabet)
class __Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c,0) + 1
        
        # start a running sum and collect frequencies, accounting for only one center character if available to us
        longest = 0
        for k in d:
            if d[k] % 2 == 0: # if the current char is of even frequency, we can add it without worry
                longest += d[k]
            else: # if the current char is of odd frequency, we have to check if we already added an odd number
                longest += d[k] if longest % 2 == 0 else d[k] - 1 # only add the even portion if we already have a center char (palindrome length has already been made odd)
        return longest

    
    
    
    
    
    
