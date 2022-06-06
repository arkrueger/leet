"""
approach:
    dict / hash map:
        ransom note is shorter than magazine -> create a frequency from this
        iterate through magazine and decrement the frequency map
        once a character is zero remove the key from the dict
        once the dict size is 0 return true
        if we exit the loop without dict size being zero return false
"""

# frequency map / hash
# T: O(r + m) where r is ransom note length and m is magazine length
# S: O(1) because this is maximum the size of the alphabet so it doesn't scale with r and m
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in ransomNote:
            d[c] = 1 + d.get(c, 0) # get d[c] or 0 if it's not there yet

        for c in magazine:
            if d.get(c, 0) > 0:
                d[c] = d.get(c, 0) - 1
                if d.get(c, 0) <= 0:
                    d.pop(c,0)
            if len(d) == 0: # if we found all the characters we need
                return True
        return False # if we did not find the ransom note in the magazine
        
