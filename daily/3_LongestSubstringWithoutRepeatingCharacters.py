"""
approach:
    brute force sliding window:
        start with the largest window size (26) and decrease by 1 each outer loop tick
        outer loop: iterate until window size is < 2
            inner loop:
                slide the window along the string
                check if the window has only unique characters 
                    exit early if true
        once the window size is less than 2, we know the longest unique substring is 1, so return 1
    
    running tally method:
        iterate through the list only once
        keep track of two pointers, one as the start of a string and one as the leading cursor
        also keep track of a max non-repeating substring length
            increment a counter as we go along
            fill a frequency dict as we go along
                if the char at the cursor already exists in the dict,
                    then record the length of the substring (likely minus 1 from the cursor b/c the cursor is at a repeat)
                    clear the dict
                    reset the counter
        return the max length
                    
"""

# even further improvement on the running tally method (essentially the same as the first improvement but more compact)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1730/Shortest-O(n)-DP-solution-with-explanations
# originally in C++, implementing it here in python
# TC: O(n)
# SC: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = {} # track most recent index of chars
        maxLen = 0
        start = 0
        for i, c in enumerate(s):
            # move the start forward to the position after the most recent incidence of the current char, if that index is greater than start (i.e. if we have a dupe within the current substring) (but if the char hasn't ever appeared yet, just set start to start)
            start = max(indexes[c] + 1, start) if c in indexes else start 
            indexes[c] = i # store the current char's index so that we can check for dupes like we did in the previous line
            maxLen = max(maxLen, 1 + i - start) # 1 + i - start : i - start is the delta but doesn't include start, so add 1
        return maxLen

# improvement on running tally method, comes from the forum
# TC: O(n)
# SC: O(1) 
class __Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start   = 0 # keep track of the start of a growing unique substring
        maxLen  = 0 # to store the max
        freq    = {} # to indicate the most recent index where a character was used
        for i, c in enumerate(s):
            # check if current char is in freq, and if it is, check if its most recent incidence is within the current substring (i.e. check if occurs after start)
            if (c in freq) and (freq[c] >= start):
                start = freq[c] + 1 # move start to the position after the first incidence of the duplicate character
            else:
                maxLen = max(1 + i - start, maxLen) # collect overall max
            freq[c] = i
        return maxLen
        

# running tally method
# TC: O(n)
# SC: O(1)
class __Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count   = 0
        maxLen  = 0
        freq    = {} # character frequency dict
        i       = 0 # string index
        while i < len(s):
            if s[i] in freq: # if it's a repeat, check for overall max, clear the frequency dict, and reset count
                maxLen = max(maxLen, count)
                i = freq[s[i]] # restart from the position after the first incidence of the repeated character
                freq.clear()
                count = 0
            freq[s[i]] = i+1 # set the frequency dict to the string index +1 so that we can reset to there while counting
            count       += 1
            i           += 1
        maxLen = max(maxLen, count) # catches the case where the entire string was unique
        return maxLen
                

# brute force with sliding window
# TC: O(n^2)
# SC: O(1)
class __Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        length = len(s) # string length
        window = min(100, len(s)) # 100 is the rough estimate of lower/uppercase alphanumeric + symbols and spaces
        # offset = window - 1 # used in string splicing to make the math easier (can't add + window directly when substringing because the starting index is part of window)
        freq = {} # dictionary to store character frequencies and check for uniqueness
        for w in reversed(range(window+1)):
            for x in range(1+length-w): # consider length: 3, w: 1, index 0 1 2 -> stop before index 3 -> 1 + 3 - 1 = 3
                # take the window substring
                sub = s[x:x+w]
                # print(" analyzing ", sub)
                noRepeats = True
                for i in sub:
                    if i in freq:
                        noRepeats = False # if the current char was already in freq, it's a repeat, this ain't the string
                    freq[i] = 1
                # if noRepeats was not set to false, that means all characters were unique
                if noRepeats:
                    return w
                # refresh the dict for the next substring
                freq.clear()
