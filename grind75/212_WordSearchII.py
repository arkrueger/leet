"""
thinking:
    
    brute force, we could reuse the solution from Word Search I and call it for each
    but that's inefficient and might TLE
    instead, we should modify the algorithm from Word Search I to search for multiple possible matches at once
    
    https://leetcode.com/problems/word-search/
    
    for keeping track of words that we no longer want to search, can we use a list like a stack?
    similar to how we use "wordSoFar" as a path and pop the top character as we backtrack
    to do this with a word blacklist we would need to
        append the word (or its index) to a list when we first encounter curr != need
            increment a counter for the number of times we added a char to the blacklist
        make the recursive calls
        pop the stack a number of times according to the aforementioned counter
        or is there a way we can change this to a whitelist? reduces search time
        remove items from list when found or not compatible
        add back the incompatible items after the recursive calls return
        do not add back the found items (we found them, no need to waste time checking)
    
approach:
    
    ### this one's a no-go
    recursive DFS:
        same strategy as word search 1 with the following modifications
        we will maintain a list of the words (or their indices) that remain to be checked
            this is meant both in the sense that a found word will be omitted from future searches
            and also that an invalidated word (i.e. "abcd" doesn't match "abce" but we may have reason to continue searching if it matches another string) will be removed from recursive calls deeper in the tree
            when a word is found, we remove it from the list (and never add it back)
                we do add it to the "found" list though
            when a word is incompatible as of the current letter, we remove it from the list before we recurse, then add it back after the recursive call returns
        at the end we will have a list of "found" words, return that list
        
    
    trie:
        "just use a trie bro, it's basically a leetcode easy"


"""

# works, but TLEs on the later test cases
class __Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # recursive helper
        # returns True if a match is found--but this is only so that we can use this to avoid popping the top off wordSoFar
        def search(i: int, j: int, wordSoFar: List[chr], visited: List[List[int]]) -> bool:
            nonlocal wordsToCheck
            if len(found) == len(words): return True
            wordSoFar.append(board[i][j])
            tempRemoved = set()
            # check if we have any compatible words
            for idx in frozenset(wordsToCheck):
                if wordSoFar[-1] == words[idx][len(wordSoFar)-1]:
                    if len(wordSoFar) == len(words[idx]):  # we matched a word
                        found.append(idx)
                        wordsToCheck.remove(idx) # we won't be adding this back in
                else:
                    tempRemoved.add(idx) # store word so we can add it back later
                    wordsToCheck.remove(idx)
            # if wordsToCheck is empty, terminate this branch of the search
            # if not wordsToCheck:
            #     print("done with branch")
            #     return
            visited[i][j] = True
            dirs = [[1,0],[0,1],[-1,0],[0,-1]] # down right up left
            for row, col in dirs:
                row += i; col += j
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and not visited[row][col]:
                    if search(row, col, wordSoFar, visited):
                        return True # forget about searching any more branches, we found all matches
                    wordSoFar.pop() # unwind wordSoFar
            wordsToCheck = wordsToCheck.union(tempRemoved) # add the words back in
            visited[i][j] = False
            return False
        # main
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        wordsToCheck = set([i for i in range(len(words))])
        found = []
        for i in range(m):
            if len(found) == len(words): break
            for j in range(n):
                search(i, j, [], visited)
                if len(found) == len(words): break
        found = [words[i] for i in found]
        return found

# remaking the official solution
# T: O(m*n*4*3^(w-1)) where m,n are matrix dimensions and w is maximum word length
# S: O(m*n)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie
        trie = {}
        WORD_MARKER = "$"
        for w in words:
            node = trie
            for c in w:
                node = node.setdefault(c, {}) 
            node[WORD_MARKER] = w # at this level of the trie, place a non-alphabetic character to flag that there is a word here, and store said word there
        m, n = len(board), len(board[0])
        # map of the cells we've visited (this could also be the board itself)
        visited = [[False] * n for _ in range(m)]
        found = [] # the words we find matches for
        def search(i: int, j: int, parent):
            c = board[i][j] # current char
            curr = parent[c]
            match = curr.pop(WORD_MARKER, False) # pop the word if it exists, otherwise return False
            if match:
                found.append(match)
            visited[i][j] = True
            dirs = [0, 1, 0, -1, 0]
            for row, col in zip(dirs[:-1], dirs[1:]):
                row += i; col += j
                if 0<=row<m and 0<=col<n and board[row][col] in curr and not visited[row][col]:
                    search(row, col, curr) # search on the neighbor coords, providing the current node as parent
            visited[i][j] = False
            if not curr:
                parent.pop(c)
            
        # main
        for roh in range(m):
            for coh in range(n):
                if board[roh][coh] in trie: # we need to do the first check outside the search function because it only validates the candidate(next) character given the parent node
                    search(roh, coh, trie)
        
        return found
