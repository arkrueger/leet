"""
context:
    from buy and sell stock #1:
        iterate over the list in reverse
            start with the sell price pinned at the last element
            treat the current element as the buy price
                compute profit as current buy minus pinned sell
                keep track of max profit seen
                if current element < pinned sell price, set pinned sell price to current element
        return max sum seen

approach
    since we can buy and sell multiple times, we want to buy the dip and sell the peak
    -> we need an algorithm to find the dips and peaks
        this would work by ...:
    -> or, can we just buy + sell anytime prices conform to (today < tomorrow) ?
        this would work by:
            starting from the first element until second to last element
            compare today < tomorrow, if True:
                buy today, sell tomorrow (add "tomorrow - today" to the cumulative sum)
            otherwise do nothing
        return the cumulative sum
"""
# iterative
# T: O(n)
# S: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, today in enumerate(prices[:-1]):
            tomorrow = prices[i+1]
            if today < tomorrow:
                profit += tomorrow - today
        return profit


# just for context:
# this is roughly the strategy for buy and sell stock question 1 (read left - this is question #2)
class __Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = maxProfit = prices[1]-prices[0]
        sell = prices[-1]
        for buy in reversed(prices):
            if buy > sell:
                sell = buy
                continue
            buy = p
            profit = sell - buy
            maxProfit = max(maxProfit, profit)
        return maxProfit
