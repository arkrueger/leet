"""
approach:
    
    depth first search does not work when trying to find minimum path
    I first attempted this with depth first search
        using a visited set to avoid infinite loops throws a wrench in this though, because you may visit a node via a longer path first, then are unable to visit that node from a shorter path because it is already recorded in visited
        
    
    adjacency graph with BFS:
        init a dict to store neighbors as values to word keys
        iterate over words
            add each word as a key to the dict, empty array as value
                iterate over words and check if it differs by 1 letter, append to the value array
        also do this for the source word
        
        now perform BFS to find the path from source to target
        return the minimum path
        
"""
      
# from the forum
# T: O(m*n^2) where m is word length, n is wordList length (worst case we traverse the entire wordList's worth of neighbors (T: n), and for each word we check all of its generic transormations e.g. dog = *og, d*g, do* (T: m) plus for each generic transformation we search wordList for a match (T: n) -> T: O(m*n*n) )
# S: O(n) for visited set and queue
class __Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        q = deque([beginWord])
        visited = set([beginWord])
        wordList = set(wordList) # remove any potential duplicates from wordList
        # steps in the transformation sequence and alphabet to help us look for transformations
        steps = 1
        bet = "abcdefghikjlmnopqrstuvwxyz" # alphabet
        # edge case
        if endWord not in wordList:
            return 0
        # perform BFS
        while q:
            for _ in range(len(q)): # only traverse over the existing q items because we want to increment steps before continuing to elements appended during this iteration
                current = q.popleft()
                if current == endWord: # we made it to endWord
                    return steps
                # add all valid (exist in wordList and not visited) neighbors to the queue to be visited at the next step
                for i in range(len(current)):
                    # construct neighbor words, i.e. dog has the neighbor *og, d*g, do*, where * is any letter
                    pre, suf = current[:i], current[i+1:]
                    for a in bet:
                        w = pre + a + suf
                        if w in wordList and w not in visited:
                            q.append(w)
                            visited.add(w)
            # increment steps after traversing each level of the tree
            steps += 1
        # if we didn't return from the BFS, there is no path so return 0
        return 0
                
# also from the forum, but uses preprocessing
class __Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        # construct the adjacency graph
        d = {}
        for w in wordList:
            for i in range(len(w)):
                proto = w[:i] + "_" + w[i+1:] # represents a word prototype, e.g. dog -> d*g -> dig, dug
                if proto in d: d[proto].add(w)
                else: d[proto] = set([w])
        # create a deque for BFS
        q = deque([beginWord])
        visited = set([beginWord])
        wordList = set(wordList) # remove any potential duplicates from wordList
        # steps in the transformation sequence and alphabet to help us look for transformations
        steps = 1
        bet = "abcdefghikjlmnopqrstuvwxyz" # alphabet
        # edge case
        if endWord not in wordList:
            return 0
        # perform BFS
        while q:
            for _ in range(len(q)): # only traverse over the existing q items because we want to increment steps before continuing to elements appended during this iteration
                current = q.popleft()
                if current == endWord: # we made it to endWord
                    return steps
                # add all valid (exist in wordList and not visited) neighbors to the queue to be visited at the next step
                for i in range(len(current)):
                    # construct neighbor words, i.e. dog has the neighbor *og, d*g, do*, where * is any letter
                    proto = current[:i] + "_" + current[i+1:]
                    for n in d.get(proto, set()):
                        if n in wordList and n not in visited:
                            q.append(n)
                            visited.add(n)
            # increment steps after traversing each level of the tree
            steps += 1
        # if we didn't return from the BFS, there is no path so return 0
        return 0
    

# gets TLE, but passes up to test case 34/50
"""
why does this TLE when the prototype (transformation) dict version doesn't?  
    like this:
        the prototype dict has m*n keys (for each word, there are len(word) keys, i.e. dog -> *og, d*g, do*)
            each neighbor word to dog will appear only len(dog) times, once under each of the keys
        on the other hand, the full neighbors dict below is far larger, because each word in words is a key
        so the prototype dict has n keys
            and each word shows up under every single neighbor it has in the list, rather than being grouped by prototype
        I tested this with a print statement and found that when it TLE's, it doesn't even finish creating the adjacency graph
"""
class __Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # helper function to check if words differ by only one letter
        def isAdjacent(word1: str, word2: str) -> bool:
            diff = 0
            for a, b in zip(word1, word2):
                diff += 1 if a != b else 0
            return diff == 1 # will be true if the w
        if endWord not in wordList: return 0
                
        # build the adjacency graph with a dict
        d = {}
        # add beginWord to the list if it doesn't already exist in it
        # if beginWord not in wordList: wordList.append(beginWord)
        for w in wordList+[beginWord]: # include the beginWord because we need its adjacency
            d[w] = []
        for k in d:
            for b in wordList:
                if isAdjacent(k, b):
                    d[k].append(b)
        print("finished building adjacency list")
        # breadth first search
        from collections import deque
        q = deque([d[beginWord]])
        visited = set()
        path = 0
        while q:
            path += 1
            neighbors = [] 
            for n in q.popleft():
                if n == endWord:
                    return path + 1
                if n not in visited: # only add a neighbor if we have not yet visited it
                    neighbors.extend(d[n])
                    visited.add(n)
            if neighbors:
                q.append(neighbors)
        # if we didn't find a path to endWord, there is no path so return 0
        return 0
