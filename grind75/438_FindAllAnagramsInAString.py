"""
thinking:

    we could construct a trie of p's anagrams
        remember we don't care which anagram is at each index, we just care that an anagram is at the index
    

approach:

    p-trie search on s:
        construct a trie of p's anagrams
            we can do this by converting p to a list of chars
            do DFS w/visited array of size len(p)
            
    dang! a trie wasn't the way to go on this one. major league TLEs
    but hey, good practice for constructing and implementing a trie
    
    sliding window hashmap:
        hashmap size of the alphabet
        store character frequencies
        window size is p
        initialize the hash map to the frequencies of p
        then subtract the frequencies of the first len(p) characters in s
        remove keys when they reach the value of 0
        slide the window along, 
            do not recalculate the entire hash map for each starting array
            just undo (add) the trailing character and add (subtract) the leading edge character
                why reversed add/subtract? because if we do this, our map stays small and it's easy for us to check when the dict is empty
                when the dict is empty, it means the current window contains all of the characters from p (we don't care about the order) so we can add the trailing edge index to the answer list
        stop when the leading edge reaches the end of string s
    


"""





# sliding window with character frequencies (hash map)
# T: O(s) because s > p (not in all test cases, but we return [] in that case)
# S: O(1) because hash map size is limited by alphabet size
class __Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if m > n: return [] # leetcode... I have a moral disagreement with this test case
        freq = {}
        # initialize hashmap to the inverse of character frequencies in p
        for c in p:
            freq[c] = -1 + freq.get(c, 0)
        # adjust it with the frequencies in the first len(p) chars of s
        for i in range(m):
            c = s[i]
            freq[c] = 1 + freq.get(c, 0)
            if freq[c] == 0:
                freq.pop(c)
        # now slide the window
        res = []
        if freq == {}:
            res.append(0)
        for i in range(n-m):
            trailing = s[i]
            leading = s[i+m]
            # subtract the one we're leaving behind, addd the one we're taking on
            freq[trailing] = -1 + freq.get(trailing, 0)
            freq[leading] = 1 + freq.get(leading, 0)
            # prune 0-keys
            if freq.get(trailing, 0) == 0: freq.pop(trailing, None)
            if freq.get(leading, 0) == 0: freq.pop(leading, None)
            # check if we balanced out frequencies (found a match)
            if freq == {}:
                res.append(i+1)
        return res

# same as sliding window above, but without my stubborn "let's remove keys when they're zero and spend the entire time debugging dict function calls" nonsense
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if m > n: return [] # leetcode... I have a moral disagreement with this test case
        freq = {}
        # initialize hashmap to the inverse of character frequencies in p
        for c in p:
            freq[c] = -1 + freq.get(c, 0)
        # adjust it with the frequencies in the first len(p) chars of s
        for i in range(m):
            c = s[i]
            freq[c] = 1 + freq.get(c, 0)
        # now slide the window
        def isBalanced(f):
            return not any([f[i] for i in f])
        res = []
        if isBalanced(freq):
            res.append(0)
        for i in range(n-m):
            trailing = s[i]
            leading = s[i+m]
            # subtract the one we're leaving behind, addd the one we're taking on
            freq[trailing] = -1 + freq.get(trailing, 0)
            freq[leading] = 1 + freq.get(leading, 0)
            # check if we balanced out frequencies (found a match)
            if isBalanced(freq):
                res.append(i+1)
        return res          
        
        
        
        

# works but TLEs on larger test cases
# T: O(p! * s) p! for the dfs, s for checking each starting index
# S: O(p!)
class __Solution:
    def makeTrie(self, p: str) -> Dict:
        visited = [False] * len(p)
        trie = {}
        def helper(node):
            for k, v in enumerate(p):
                if visited[k] == False:
                    visited[k] = True # mark so we don't visit again on this DFS branch
                    node[v] = node.setdefault(v, {}) # add char node to trie if it's new
                    helper(node[v])
                    visited[k] = False # reset visited as we unwind
            return
        ###
        for i, c in enumerate(p):
            trie[c] = {}
            visited[i] = True
            helper(trie[c])
            visited[i] = False
        return trie
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        trie = self.makeTrie(p)
        res = []
        # search the array for starting elements
        for i in range(len(s)):
            # print("trying ", i)
            start = i
            if s[i] not in trie: # don't /search if c isn't in p
                continue
            # if trie[s[i]] == {}: # if p is a single character
            #     res.append(start)
            #     continue
            stack = [ trie ]
            while stack and i < len(s):
                # print("i ", i, " stack ", stack)
                node = stack.pop()
                c = s[i]
                if c not in node: # if no match, don't pursue further
                    break
                if node[c] == {}: # if node is empty, then we reached the base of the trie (match)
                    res.append(start)
                    break
                # if we didn't already return, let's try the next one
                i += 1
                stack.append(node[c])
        ##
        return res
