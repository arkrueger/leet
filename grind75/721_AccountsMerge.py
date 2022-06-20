"""
approach:
        
    note:
        why is this one trickier than other adjacency graph problems?
            because in most adjacency graphs we create, the values and the keys are of the same quality
            for example, let's say we have a graph of people who live in a neighborhood and their neighbors
                the keys would be people's names, and the values would be their neighbors
                in other words, while doing DFS, we simply look at a give person, look at their neighbors, 
                plug those keys into the dict to find their neighbors, and so on
                -> each value is also a key
            but in this problem, our values and keys are of different quality, i.e. keys = emails and values = indices
            this means that in order to do DFS, we don't just look at the values and append all non-visited values
            we actually have to visit the accounts list at the indices indicated by the dict values, and append those email addresses to the search path
            
    adjacency graph + DFS:
        build adjacency graph in a dict
            keys: email addresses
            values: list containing row indices where they appear
        iterate through the indices, on each iteration initialize a stack with the current index
            use a visited array to avoid double tracking
            on each iteration, perform dfs to find all email addresses associated with that contact
            append to the new merged list
"""


# adjacency graph + DFS
# T: O()
# S: O()
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # names are not unique, so we rely on email addresses
        # build a hash map of the email addresses
        emails = {}
        for i, c in enumerate(accounts):
            for e in c[1:]:
                if e in emails: emails[e].append(i)
                else: emails[e] = [i]
        merged = []
        visited = [False] * len(accounts)
        # merge the dupes
        for i in range(len(accounts)):
            stack = [i]
            temp = [] # holds each account (may be empty if "while stack" doesn't build a new list, i.e. already visited)
            while stack:
                idx = stack.pop()
                if not visited[idx]:
                    visited[idx] = True
                    newEmails = accounts[idx][1:]
                    temp.extend(newEmails)
                    stack.extend([k for e in newEmails for k in emails[e]]) # add connected indices to the stack
            if len(temp) > 0: # only add temp if contains elements (it would be empty if we already visited this email and its graph neighbors in a previous iteration)
                merged.append([accounts[idx][0]] + sorted(list(set(temp)))) # account name + sorted list w/o dupes
                
        return merged
