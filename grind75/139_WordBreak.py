
"""
approach:
    
    brute force:
        try all combinations whose combined length equals length of s
        bad idea
    
    recursive:
        sliding window
        begin at start
            end at end
            recurse on same function with end as new start
        try all possible values of start and end
        see code below
    
    BFS:
        consider that in order to form a string, we must find a word in the dictionary that matches at least the first character of the input string
        for example
            s: leetcode, wordDict: [lee, tc, code, leet]
            do BFS
            level 1 gives us:
                    lee -> remains: tcode
                    leet -> remains: code
            level 2 gives us:
                    tc -> remains: ode
                    code -> nothing remains -> return True
            if we hadn't found "code" and were to continue with the BFS,
            level 3 would give us, trying to match "ode" in the dict:
                    no match -> deque runs empty, loop exits
            return False if the loop exits without finding a match
"""

# DP leetcode official
# T: O(n^3) two nested loops plus wordDict search
# S: O(n) for the dp array
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
                    

# BFS
# T: O(n^3) but likely a bit more efficient than the official leetcode BFS solution
# the actual number of iterations depends on the number of wordDict matches found in s, and the range of word lengths found in wordDict
# the official solution checks each end in range(start+1, len(s)+1) which is unnecessary, because we know the only valid "end" indices are those that fall between start and start+(all lengths found in word dict) so this is more efficient for cases where word dict has only a few different word lengths
# S: O(n) queue length
class __Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from collections import deque
        q = deque([0])
        visited = set()
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for w in wordDict:
                end = start+len(w)
                if s[start:end] == w:
                    if end == len(s): # we built the whole string, return True
                        return True
                    else:
                        q.append(end)
            visited.add(start)
        return False
                    


# brute force, TLE
# T: O(2^n) because we split the array n times for each call
# S: O(n) recursive stack space
class __Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # helper function
        def wordBreakRecursive(s: str, words: Set[str], start: int) -> bool:
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in words and wordBreakRecursive(s, words, end):
                    return True
            return False
        # main function
        return wordBreakRecursive(s, wordDict, 0)
    

# recursive memoization
# I don't see how this is any different... the only change is the use of a frozenset
# T: O(n^3)
# S: O(1)
class __Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # helper function
        def wordBreakMemo(s: str, words: FrozenSet[str], start: int):
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in words and wordBreakMemo(s, words, end):
                    return True
            return False
        # main function
        return wordBreakMemo(s, frozenset(wordDict), 0)
