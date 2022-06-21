"""
clarifications:
    
    is ".*" possible to see in the pattern?
        -> yes, see example input 3
    
mapping example input:
    
    s = abccd, p = a.c*d
    for DFS:
        stack = [[0,0]] ; eval s: a with p: a, visited = stack[-1]
            -> this is a match and p does not offer continuation, so append only [sI+1,pI+1]
        stack = [[1,1]] ; eval s: b with p: . , visited etc
            -> this is a match and p does not offer continuation, so append only [sI+1, pI+1]
        stack = [[2, 2]] ; eval s: c with p: c* , visited etc
            -> match, p offers continuation, so extend with [[sI+1:sI_not_c,pI], [sI+1:sI_not_c+1,pI+2]]
        stack = [[3,2],[3,4],[4,4]] ; eval s: c with p: c*
            -> match, p offers continuation but sI+1=sI_not_c so skip that, extend with [4,4]
        stack = [[3,4],[4,4],[4,4]] ; eval s: c with p: d
            -> no match, append nothing
        stack = [[4,4],[4,4]] ; eval s: d with p: d
            -> match but no continuation, extend with [sI+1,pI+1] or [5,5]
        stack = [[4,4],[5,5]]
            -> [4,4] already in visited, continue
        stack = [[5,5]]
            -> return True because we reached the end perfectly, 5 == len(s) and 5 == len(p)
            
    
    for BFS:   
        same strategy, but popleft instead of pop
    
    
approach:
    
    BFS:
        T: O()
        S: O()
        start a deque of lists, where the list contains [s index, p index]
        store visited index pairs in a set to avoid infinite loops
        *** below is out of date and contains errors, see actual code below this comment section for the working algorithm
        while the deque is not empty:
            popleft onto sI and pI (indices for s and p)
            if [sI,pI] in visited then skip
            vars:
                currS = s[sI]
                currP = p[pI] if p[pI:pI+2][-1] != "*" else p[pI:pI+2]
            conditionals:
                # exit/continue cases, we exceed either list length
                if sI >= len(s) or pI >= len(p):
                    if sI == len(s) and pI == len(p): # then we successfully matched the whole string
                        return True
                    else: # then we ran out of one list but haven't finished the other, dead end
                        continue # this branch hit a dead end, move on to other leads
                if len(currP) > 1: # we have a wildcard
                    if currP[0] == currS or currP[0] == ".": # we have a match
                        q.append([sI+1,pI+2]) # simple case where only one matched and we move the pattern forward
                        for i in range(sI+1,len(s)-1): # want to try all possible repeats
                            if currP != "." and s[sI+1] != currP: # but only for the same character or all characters if pattern is ".*"
                                break (to outer while)
                                q.append([i, pI+2])
                else: # no wildcard, just a dot or a letter
                    if currP == ".": # then match anything
                        q.append([sI+1, pI+1])
                    elif currP == currS: # character match
                        q.append([sI+1, pI+1])
                    else: # no match, abandon this branch
                        continue
    
    DFS:
        same as bfs but with stack and pop
            
"""


            
# BFS
# T: O(not sure) faster than standard recursive, as fast as DP but uses less space than DP
# S: O(m*n + F(num of "*" in p)) for the visited matrix where m=len(s), n=len(p), and F(*) for the deque -- length is dependent upon the number of BFS branches, which are created by wildcard patterns
class __Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from collections import deque
        q = deque([[0,0]])
        visited = [[False] * len(s) for _ in range(len(p))] # len(s) columns, len(p) rows
        while q:
            print(q)
            sI, pI = q.popleft();
            # exit/continue cases, we exceed either list length
            if sI >= len(s) or pI >= len(p):
                if sI == len(s) and pI == len(p): # successfully matched the whole string
                    return True
                elif pI < len(p) and p[pI:pI+2][-1] == "*": # there's still a chance to zero-match on "x*"
                    q.append([sI,pI+2])
                    continue
                else: # then we ran out of one list but haven't finished the other, dead end
                    continue # don't append any child branches to the tree
            # the current char in s and the current pattern in p (p could be 1 or 2 chars)
            currS = s[sI]
            currP = p[pI] if p[pI:pI+2][-1] != "*" else p[pI:pI+2]
            # if it's not an exit case but we already saw it, then ignore and continue
            if visited[pI][sI]:
                continue
            visited[pI][sI] = True
            # the meat of the pattern matching is below
            if len(currP) > 1: # we have a wildcard, e.g. "x*" or ".*"
                q.append([sI,pI+2]) # "zero-match" case, do this always
                if currP[0] == currS or currP[0] == ".": # only append these if we match the current character (or have ".*")
                    q.append([sI+1,pI+2]) # "exactly 1 match" case, consider next pattern in p on next char in s
                    q.append([sI+1,pI]) # "1+ match" case, i.e. consider "x*" on next char in s
                    # for i in range(sI,len(s)-1): # want to try all possible repeats
            else: # no wildcard, just a dot or a letter
                if currP == ".": # then match anything
                    q.append([sI+1, pI+1])
                elif currP == currS: # character match
                    q.append([sI+1, pI+1])
                else: # no match, abandon this branch
                    continue
        # if we didn't reach the end of the list inside the BFS, then there is no match
        return False
            
            
# official leetcode solution for recursion
# runs much slower than the BFS with deque solution
class __Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text
        # does the first character match? -> first_match True or False
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        # if we have a wildcard...
        if len(pattern) >= 2 and pattern[1] == '*':
            # check for both the zero-match and the 1+ match
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else: # otherwise check for a single character match
            return first_match and self.isMatch(text[1:], pattern[1:])
            

# official leetcode solution for dynamic programming
# functions basically the same as the standard recursive solution, except:
#       store answer in memo[i,j]
#       only recurse if memo[i,j] doesn't exist yet
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text) # if we passed the end of both s and p, ans is True
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
