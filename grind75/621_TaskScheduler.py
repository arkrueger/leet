"""
thinking:
    
    edge case where n=0, just return length of task list
    
    A B idle A B
    A B B
    
    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
    A   A   A   A   A   B   B   B   B   C   C   C   C   G   G      n = 2
    ABCABCABCABCAG..G
    GABCABCABCABCAG
    GABCGABCABCABCA
    
    take the frequencies
    start with the largest frequency * n as a lower bound
        then grab the next highest frequency, if n > 1 then we can "fold" the next highest frequency task into the idle time 
        and so on and so forth
    
    
approach:

    greedy:
        official leetcode solution
        
        

"""



# T: O(len(tasks))
# S: O(1)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1
        
        freq.sort()
        print(freq)
        
        fmax = freq.pop()
        idle = (fmax-1) * n
        
        while freq and idle > 0:
            idle -= min(fmax-1, freq.pop())
        idle = max(0, idle)
        return idle + len(tasks)
