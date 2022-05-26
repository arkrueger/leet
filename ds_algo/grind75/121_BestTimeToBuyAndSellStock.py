### GRIND 75 SECOND PASS ###
"""
approach:
    brute force:
        calculate the sums of all subarrays
        record the max
        return the max
    
    running ledger:
        loop through the list starting from index 0
            add the current element to the running tally
                record as global max if it is
            if our running tally dips below 0, then we may as well have not bought/sold in that period at all
                so we can reset our running tally to zero
                (it might be tempting to wonder "but what if the stock goes way higher afterwards and our original starting price was actually ok? why would we throw that away?" -> but recall that the stock is currently going down, so while our cursor is currently at a price that's bad for *selling*, it's a great price for buying. So we don't need to worry about any period that results in a negative stock price, because we inherently landed on a better buying price in the process)
        -> return the global max when we finish the loop
"""



# running ledger:
# T: O(n)
# S: O(1)
class __Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: # if there's only one day to buy, then we can't sell, so we can't profit
            return 0
        globalMax = 0
        currentProfit = 0
        start = 0
        for i, c in enumerate(prices):
            currentProfit = c - prices[start]
            globalMax = max(globalMax, currentProfit)
            if currentProfit < 0: # sink any negative buy-sell periods and reset the buy time to today
                start = i
        return globalMax
    
# alternate approach to running ledger, but starting from the end of the array (from the forum)
# T: O(n)
# S: O(1)
class __Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: # if there's only one day to buy, then we can't sell, so we can't profit
            return 0
        globalMax = 0
        salePrice = prices[-1]
        # loop through reversed list
        # compute current profit
        # set as max if relevant
        # check if we found a better sale price (if current sale price is higher than previous sale price)
        # if so, set that as the new sale price
        for i in reversed(prices):
            globalMax = max(globalMax, salePrice - i)
            if i > salePrice:
                salePrice = i
        return globalMax
            
        

# brute force - gives us TLE
# T: O(n^2)
# S: O(1)
class __Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: # if there's only one day to buy, then we can't sell, so we can't profit
            return 0
        globalMax = 0
        for i, c in enumerate(prices[:-1]): # from start to just before end
            for k, x in enumerate(prices[i+1:]): # from just after current to end
                globalMax = max(globalMax, x - c) # x - c is the local maximum
        globalMax = globalMax if globalMax > 0 else 0 # if we can't profit, don't buy anything
        return globalMax
    
            