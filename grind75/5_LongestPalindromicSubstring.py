# doing this a second time for Grind 75

"""
approach:
    
    brute force sliding window:
        iterate over all possible window sizes
            slide the window along the string
                check if substring is a palindrome
                    record max substring length seen
        
        just diagramming out the windows
        0 1 2 3 4 -> len(string) = 5
        a b c d e
        w = 3 -> last possible substring starts at index 2 
        -> starting index goes range(0,3) -> range(0,len(string)-w+1)
    
    dynamic programming:
        one letter palindromes are trivial to find
        search for and consider all two letter palindromes
            now that we have the 2 letter palindromes, we can expand these to find all 3 letter palindromes
            once we find the 3 letter palindromes (the set size is <= the number of 2 letter palindromes)
                (because some 2 letter palindromes when extended will not become 3 letter palindromes)
    
    expand around center:
        similar to the dynamic programming method, but does not allocate any extra data structures
        iterate through the array, stopping at each possible center 
            (a center is a single character, or the space between two characters)
            at each center:
                expand around the center until either the start/end of the string is reached, or the substring is no longer a palindrome
                record the current palindrome if it is longer than the current longest palindrome
        how to identify centers?
            given   0   1   2   3   4   5 -> len = 6 -> 11 centers
                    t   h   e   c   a   t
                    0 1 2 3 4 5 6 7 8 9 10
"""

# even more compact expand around center, based on my favorite from the discussion forum
# T: O(n^2)
# S: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        def expand(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right] # left+1 b/c we took 1 after the last valid pal, leave right as is because exclusive end string slicing
        
        longest = ""
        offset = [i%2 for i in range(2*len(s)-1)] # will alternate 0 and 1 to account for even and odd palindromes
        index = [i//2 for i in range(2*len(s)-1)]
        for (i, o) in zip(index, offset):
            candidate = expand(s, i, i+o) # palindrome centered on index i,i+0 (odd length) or i,i+1 (even length)
            longest = candidate if len(candidate) > len(longest) else longest
        return longest


# expand around center
# is slow, maybe because we allocate so many strings?
# T: O(n^2)
# S: O(1)
class __Solution:
    def longestPalindrome(self, s: str) -> int:
        # helper function to find longest palindrome given starting indices
        def expand(s: str, left: int, right: int) -> int:
            pal = ""
            while left >= 0 and right < len(s):
                if s[left:right+1] != s[right:(left-1 if left > 0 else None):-1]:
                    return pal
                else:
                    pal = s[left:right+1]
                    left -= 1
                    right += 1
            return pal
        
        longest = s[0]
        k = 2 * len(s) - 1 # this is the number of palindromic centers we can have
        for i in range(k):
            left = right = i // 2 # keep it this way if char is center
            if i % 2 == 1: # if center is between two chars, move the right cursor forward
                right += 1
            candidate = expand(s, left, right)
            longest = candidate if len(candidate) > len(longest) else longest
        return longest


# Brute force, more compact, gets TLE
# O(n^3)
class __Solution:
    def longestPalindrome(self, s: str) -> int:
        r = s[::-1]
        longest = s[0:1] # (start index, window size)
        # sliding window
        for w in range(1,len(s)+1):
            for i in range(len(s)-w+1): # start window at 0, don't go out of string bounds with w
                sub = s[i:i+w]
                if w > len(longest) and sub == sub[::-1]:
                    longest = sub       
        return longest

# Brute force, gets TLE
# O(n^3)
class __Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initial strategy, brute force:
        #   reverse the string and store it
        #   traverse the string with all window sizes and search for window in reversed string
        #   record length and return the longest
        
        size = len(s)
        reversedS = s[-1::-1]  # reverse the string to search on palindromes
        
        # for a given window size, iterate over the string and find the largest palindrome
        #   from that window
        def traverse(windowSize) -> str:
            maxChunk = ""
            for i in range(0, 1+size-windowSize):
                chunk = s[i:windowSize+i:1]
                if chunk == chunk[-1::-1]:
                    if reversedS.find(chunk) >= 0:
                        if len(chunk) > len(maxChunk):
                            maxChunk = chunk
            return maxChunk
        
        # iterate over all window sizes and find the largest palindrome
        maxChunk = ""
        for i in range(0,size+1):
            res = traverse(i)
            if len(res) > len(maxChunk):
                maxChunk = res
        
        return maxChunk
        
            
            
