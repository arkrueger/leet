"""
thinking:
    can we use tries? 
        could, but why not use dict keys instead? (that's a trie in the background anyway)

approach:
    
    brute force with sets:
        try every possible substring
        store results in a set (prohibits duplicates)
        cast the set to array and return
    
    trie:
        effectively the same thing as brute force with sets, except that you have to put the work in to build the trie
        I'm not going to code it out, but there are examples in the forum
    
    suffix array:
        if returning to this problem, check out the suffix / prefix array solutions in the forum
        but I can't learn a new algorithm or data structure today, so I'm skipping for now
        https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/discuss/1556081/Python-O(N)-solution(where-N-is-number-of-distinct-substrings)
        https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/discuss/1010936/Python-Suffix-Array-%2B-LCP-O(N-logN)
        
"""

# brute force
# T: O(n^2) n windows, with avg window traversal being 0.5*n -> 0.5*n^2 simplifies to n^2
# O: O(1) we don't create any additional data structures
class Solution:
    def countDistinct(self, s: str) -> int:
        distinct = set()
        for w in range(1,len(s)+1): # w is window size
            for start in range(len(s)-w+1):
                distinct.add(s[start:start+w])
        return len(distinct)
