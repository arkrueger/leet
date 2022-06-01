"""
thinking:
    start with the largest coins
    add them up until before the sum exceeds the target amount
    then move on to the next coin and repeat
    
approach:
    recursive DP:
        
    
    iterative DP:
        big picture view: we make len(coins) passes over range(amount)
        starting with the smallest coin and ending with the largest
        our dp list: dp[i] = min number of coins (so far) that sums to i
        as we iterate down the array, build dp like this:
            check if the coin is relevant (i.e. is coin < i?)
                dp[i] = max(dp[i], dp[i-coin] + 1)
                ^ lemme explain this:
                    dp[i] currently contains the minimum # coins to reach i found on the last pass
                    we also know that dp[i-coin] contains the minimum found to reach, well, i-coin
                    so logically, we know we can reach i by using our current coin (coin) plus the coins we used to reach dp[i-coin]
                    -> how many coins is that? well, that's dp[i-coin] + 1, where 1 represents our current coin
                        again, 1 doesn't represent the coin's value, it represents that we are using a coin
                    in this way, with dp[i] = max(dp[i], dp[i-coin]+1) we are recording a new minimum ONLY if it is possible to use fewer coins by using the coins represented in dp[i-coin] plus the current coin
                    FOR EXAMPLE, if we have coins 1, 2, and 5, consider i=10
                        on the "2 cent" of the loop, dp[i=6] will hold the number 6, i.e. 3 of the 2-cent coins
                        but on the 5-cent pass of the loop, we will see that dp[i-coin = 6-5 = 1] = 1, therefore dp[i-coin]+1 = 2, representing that we can reach 6 by using a 1 cent coin plus a 5 cent coin, so we store the new minimum "2 coins" in dp[6]
            if the coin is larger than the amount we try to reach, don't bother
"""

# Iterative DP
# T: O(amount*coins) because we make a pass over range(amount) for each coin
# O: O(amount) for our DP list
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1) # dp array storing inf (length amount + 1 because unlike when we range over a len(list), we want to include "amount" in the range, not stop before it)
        dp[0] = 0 # takes 0 coins to reach the amount 0
        for coin in coins:
            for amt in range(amount+1):
                if amt-coin >= 0: # don't consider amounts smaller than the current coin
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        if dp[-1] == float('inf'): # if we weren't able to reach amount with any coin combo
            return -1
        return dp[-1] 
            



# basic proof of concept, does not test different combinations
# DO NOT USE
"""
class __Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = sorted(coins, reversed=True)#
        coins.sort(reverse=True)
        total = 0
        count = 0
        for i in range(len(coins)):
            numCurrCoins = (amount - total) // coins[i]
            count += numCurrCoins
            total += numCurrCoins * coins[i]
            # print("total: ", total, " numCurrCoins: ", numCurrCoins, " count: ", count)
        return count
"""
