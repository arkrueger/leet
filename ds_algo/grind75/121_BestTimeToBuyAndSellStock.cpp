/*
approach:
    brute force:
        nested loop
            inner loop has a floor of the index of the outer loop (stay below matrix diagonal)
            compute profit and store if maximum
        return maximum

    hash map:

*/
using namespace std;

class Solution {
 public:
  // better approach (traverse array and keep track of min buy price and max profit)
  // Time: O(n)
  // Space: O(1)
  int maxProfit(vector<int>& prices) {
    int maxProfit = 0;
    int minBuyPrice = prices[0];  // initialize to the first price

    for (int i = 0; i < size(prices); i++) {
      // grab the current profit delta if higher, otherwise keep the existing max
      maxProfit = max(prices[i] - minBuyPrice, maxProfit);
      // we want to track the minimum buy price we see
      // (so that we can use it preferentially over any higher buy prices in the future)
      // it's key to note here that this method disallows traveling backwards in time
      minBuyPrice = min(prices[i], minBuyPrice);  // grab whichever is lower
    }
    return maxProfit;
  }

  // brute force approach (exceeds time limit)
  // Time: O(n^2)
  // Space: O(1)
  // int maxProfit(vector<int>& prices) {
  //     int maxProfit = 0;
  //     int profit = 0;
  //     for(int i = 0; i < size(prices); i++) {
  //         // start k at i so that we don't represent any transations runnig backwards in time
  //         for(int k = i; k < size(prices); k++) {
  //             // store new max if applicable
  //             profit = prices[k] - prices[i];
  //             profit > maxProfit ? maxProfit = profit : maxProfit = maxProfit;
  //         }
  //     }
  //     return maxProfit;
  // }
};