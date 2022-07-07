"""
thinking:
    
    this is is similar to a problem that asks how much energy a drone needs to start with if it has perfect conservation of potential energy, and expends no energy to remain at the same height
    but it's a little different
    
    we have to select the gas station that, over the course of the burn/fill cycles, gives us enough gas to cross the largest gap
    
    can we treat this similar to the "largest subarray sum" problem where the subarray start index is reset when cumulative sum dips below zero?
        in this case it would be when we are unable to reach a gas station
    
    basic truths:
        we can't start at a gas station whose gas[i] < cost[i] 
        
    hmm another thought, can we normalize the costs? in other words, can we make it trivial to traverse a known section by saying "from station 0 to 1 to 2 to 3 we know we are able to make it based on 0, and the amount of gas left over from 0 to 3 is x"
    we could precompute this for n*n where n is the length of the array
    but then what's the point, that's inefficient
    
    
    hold on, is this just a "daily temperatures https://leetcode.com/problems/daily-temperatures/" problem in disguise?
    in daily temperatures, we started at the end and moved backwards, building the output list (and each element we needed to fill in could be informed by the elements we already filled in at the later indices)
    
    can we make an array of deficits (negative means the gas station didn't provide enough gas, positive means we had gas left over) and 
    gas = [1,2,3,4,5], cost = [3,4,5,1,2] leftovers = [2,-3,-3,2,2] where leftovers[i] is the gas leftover after reaching i, before filling up, in other words whether it was possible to get to i on gas[i-1] alone
    gas = [2,3,4], cost = [3,4,3] leftovers = [1,-2,0]
    -> looks to me like our starting index should be the beginning index of the highest-summing string of positives, no?
    -> if the leftovers array sum < 0, return -1
    
approach:
    
    brute force: 
        simply try all starting stations, backtrack early if we hit 0
        
    running total with dp?
        it might be possible to try the "max subarray sum" method
        the only catch is that we want to try all starting n's and this would skip some?
        also, how do we catch that there is no solution?
    
    leftovers array:
        build array where leftovers[i] is the gas left over upon reaching station i, before filling up, provided that the gas tank contained only what gas was available at station i-1
        if the sum of leftovers elements is < 0, return -1
        iterate through the leftovers array to find the starting index of the highest-summming region of positive numbers
        


"""

# dang, my intuition with the "max subarray sum" approach was spot on
# it's no more complicated than that
# coulda saved a lot of time by trying that out
# "cumulative lack of fuel" method
# T: O(n)
# S: O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        currTank = 0
        totalTank = 0 # we'll use this to keep track of the overall cost - gas
        start = 0
        for i in range(n):
            totalTank += gas[i] - cost[i]
            currTank += gas[i] - cost[i]
            if currTank < 0: # then this can't be the starting station
                start = i + 1
                currTank = 0
        
        return start if totalTank >= 0 else -1 # if totalTank < 0, then we can't complete the circuit from any station



# leftovers array
# this works up until test case 25, but is flawed
# T: O(n)
# S: O(n)
class __Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        leftovers = [0] * n
        # generate leftovers array
        indices = [-1] + [i for i in range(0, n-1)]
        for i in indices:
            currCost = cost[i]
            currGas = gas[i] # gas comes from the previous station and we treat it as a circuit
            leftovers[i+1] = currGas - currCost
        # check if a solution is possible
        if sum(leftovers) < 0: return -1
        # find the highest-summing region of positive leftovers
        station = 0
        maxPositiveSum = 0
        currPositiveSum = 0
        leftovers = leftovers+leftovers
        print(leftovers)
        i = 0
        while i < 2*n:
            j = i
            # print(j)
            while j < 2*n and leftovers[j] >= 0:
                currPositiveSum += leftovers[j]
                print("curr ", currPositiveSum)
                if currPositiveSum > maxPositiveSum:
                    maxPositiveSum = currPositiveSum
                    station = i # we want i because i is the starting index of this region
                j += 1
                # print(j)
            currPositiveSum = 0 # reset the current var
            i = j + 1 # move i forward to our current position
            # print("i ", i, " j ", j)
        # outdent
        print(station)
        station = station if station < n else station - n
        return station-1 if station > 0 else n-1
