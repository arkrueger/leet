### GRIND 75 SECOND PASS ###

"""
approach:
    hash:
        loop through each string and collect their character frequencies
        loop through the character frequency dicts and compare
            return False if there is any mismatch
        return True if we completed the loop without returning False
        
    alternate hash: 
        loop through the first string to collect frequencies
        loop through the second string to decrement frequencies
            if any key isn't found, return False
            delete any key that reaches 0
        return true if the frequency dict is an empty dict
        
    sorted strings:
        sort the strings
        compare the strings
        of course be sure that your language of choice is comparing string contents and not object reference
"""

# sorted strings
# T: O(n)
# S: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# alternate hash 
# T: O(n)
# S: O(1) but slightly lower than the solution below because it only needs one frequency dict
class __Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in t:
            if i in freq:
                freq[i] -= 1
                if freq[i] == 0:
                    freq.pop(i)
            else:
                 return False   
        if freq == {}:
            return True
        else: 
            return False

# hash / frequency dict
# T: O(n) where n is the string length (they should be equal lengths if anagrams)
# S: O(1) this doesn't scale with n because there are a fixed number of numeric characters
class __Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case where the strings are of diff lengths
        if len(t) != len(s):
            return False
        # frequency dicts
        freqS = self.collectFrequencies(s)
        freqT = self.collectFrequencies(t)
        # if the frequency dicts are of different sizes, we know they can't desribe the same strings
        if len(freqS) != len(freqT):
            return False
        for i in freqS.keys():
            if i in freqT:
                if freqS[i] != freqT[i]:
                    return False # if they don't have the same count, game over
            else:
                return False # if any keys aren't in both, game over
        return True
    
    # helper, collect frequencies
    def collectFrequencies(self, s: str) -> dict:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        return freq