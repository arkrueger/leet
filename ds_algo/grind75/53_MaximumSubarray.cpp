
/*
approach:
    nested loops: (dear god, it's so slow it times out on leetcode even with C++)
        outer loop controls the start of the contiguous array (window)
        inner loop keeps track of the largest sum possible given the starting index
        after the loops, return the maximum sum

    zero-out-the-sum:
        loop through once ( so O(n) time)
            on each loop, compute the cumulative sum and store in max if it's higher than max
            if the cumulative sum is less than zero, just zero it out -> this is equivalent to
                resetting the "window" for the potential subarray as starting at the current
                index
            This works because if we already recorded the previous high in max, then by zeroing out
                cumulative sum when the contribution goes below zero,

            what about the edge case where all numbers are negative? well, still works. The subarray
                will be just the first element - all other elements push the cumulative sum lower
                no matter what

    divide and conquer:
        return the max of these three:
            split the array in half (if the length is odd, give the middle to either right or left)
            find the max sums of the right and left halves, where the subarray starts at their
                respective first indices
            take the higher max of those

*/
class Solution {
 public:
  // divide and conquer approach
  // O(n*logn) i.e not the optimal solution
  //     int maxSubArray(vector<int>& nums, int low=0, int high=-1) {
  //         // low and high will not be passed to first func call. Low is trivial but high must be set.
  //         if(high < 0) {
  //             high = nums.size()-1;
  //         }

  //         // if high and low are equal, return early
  //         if(high <= low) {
  //             return nums[low];
  //         }

  //         // split the array, find the max subarray sums of each half
  //         // important, these subarrays should radiate from the center
  //         // that is, computing the left half should start at mid and grow towards index 0
  //         // computing the right half should start at mid and grow towards size() - 1
  //         int mid = (low + high)/2; // truncates, rounds down
  //         int leftMax = simpleMax(nums, mid, low); // always set start=mid, end=low or high to radiate
  //         int rightMax = simpleMax(nums, mid+1, high);
  //         // get the max found by recursing on the halves
  //         int maxRecursive = max(maxSubArray(nums, low, mid), maxSubArray(nums, mid+1, high));

  //         // find the max of
  //         int maxOfAll = max(maxRecursive, leftMax+rightMax);

  //         return maxOfAll;
  //     }
  //     // helper func for finding simple max subarray (no sliding window)
  //     int simpleMax(vector<int>& nums, int start, int end) {
  //         int maxSum = nums[start];
  //         int currSum = 0;
  //         // controlling increment/decrement direction
  //         int incdec = 1; // controls whether to increment or decrement
  //         start < end ? incdec *= 1 : incdec *= -1; // controls direction of subarray growth
  //         // start loop counter just outside of the correct bounds so that it can be incremented
  //         //      before operations in the do-while loop
  //         int i = start - incdec; // loop counter
  //         // find the max subarray
  //         do {
  //             i += incdec; // increment i in the correct direction
  //             currSum += nums[i];
  //             maxSum = max(maxSum, currSum);
  //         } while(i != end);
  //         return maxSum;
  //     }

  // Correct O(n) method from the forum
  /* I was skeptical because this seems unintuitive at first
   but the key piece is that if currSum (i.e. the cumulative sum) falls below 0, it resets currSum
   that is, if the contribution of the current set of numbers causes the sum to zero out, then
      there is no reason to include that (i.e. you can set the beginning of the "window" to
      current index because adding a negative number causes the future cumulative sum to drop,
      which we don't want)
  For example, if we have [5, 5, 5, -16, 1] we will have recorded the max of 15, and upon
      reaching index 3 (-16), we zero out the currentSum.

  */
  //     int maxSubArray(vector<int>& nums) {
  //         int maxSum = nums[0];
  //         int currSum = 0;

  //         for(int n = 0; n < nums.size(); n++) {
  //             if(currSum < 0) {
  //                 currSum = 0;
  //             }
  //             currSum += nums[n];
  //             maxSum = max(currSum, maxSum);
  //         }
  //         return maxSum;
  //     }

  // my original approach, which doesn't work b/c it times out
  // nested loops approach
  // too slow, execution time limit exceeded
  // Time: O(n^2)
  // Space: O(1)
  //     int maxSubArray(vector<int>& nums) {
  //         int currentSum = 0; // must be zero to play nice with the += in the inner loop
  //         int maxSum = nums[0]; //

  //         // loop through the array
  //         // outer loop slides the window forward by moving the inner loop starting value
  //         for(int k = 0; k < nums.size(); k++) {
  //             // change where the subarray starts (i=k) and "walk" the starting index along the array
  //             for(int i = k; i < nums.size(); i++) {
  //                 // if i = k, reset currentSum to the start of the new window
  //                 // otherwise, do the cumulative sum
  //                 i == k ? currentSum = nums[i] : currentSum += nums[i];
  //                 maxSum = max(currentSum, maxSum);
  //             }
  //         }
  //         return maxSum;
  //     }
};