"""
approach:
    
    dict of 2d lists:
        dict keys are the key in get(key, timestamp)
            dict value is the 2d list
                first list element: value
                second list element: timestamp
        for O(logn) time, use binary search to find the requested timestamp
    
    dict of dicts:
        outer dict keys are the keys given in the test cases
            outer dict values are the inner dicts
        inner dict keys are the timestamps
            inner dict values are the values at those timestamps
        still need binary search to locate nonexact timestamp matches
        
        
"""

# dict of 2d lists
# T: O(logn) retrieval where n is the number of timestamped values for a given key
# S: O(n) where n is the total number of values across all keys
class __TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        d = self.d # to avoid tying self so much
        if key in d:
            d[key].append([value, timestamp])
        else:
            d[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        d = self.d # to avoid typing self so much
        # edge cases
        if key not in d or d[key][0][1] > timestamp: # if it's not there at all or the requested timestamp is earlier than the earliest existing timestamp
            return ""
        # binary search
        high = len(d[key]) - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if d[key][mid][1] == timestamp:
                return d[key][mid][0]
            elif d[key][mid][1] > timestamp:
                high = mid - 1
            elif d[key][mid][1] < timestamp:
                low = mid + 1
        # if we didn't find an exact match, adjust mid to just before the requested timestamp
        mid = mid if d[key][mid][1] < timestamp else mid - 1
        # return timestamp <= mid
        return d[key][mid][0]
            

# more concise version of a dict implementation that I saw in the forum
"""
here's how it works
    create two dicts, one for timestampse and another for values
    remember we can assume element addition occurs in increasing time order
    __init__ and set() are trivial
    get() works like:
        use the bisect function (tells you the index at which element x should be inserted in a sorted list) to get the index following the desired timestamp
        subtract 1 from this index to get the desired timestamp
        return "" if the bisect function did not have an answer for us
"""
class TimeMap:
    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
