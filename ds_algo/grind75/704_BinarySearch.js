/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

// standard approach
var search = function (nums, target) {
  let upper = nums.length - 1;
  let lower = 0;
  let i = 0;

  // if target is less than the first index or greater than the last, it's not in the list
  if ((target < nums[0]) || (target > nums[upper])) {
    return -1;
  }

  while (upper > lower) {
    i = Math.floor(upper + lower) / 2;
    // return the index if we found a match
    if (target === nums[i]) { return i; }

    // adjust the bounds if no match
    target > nums[i] ? lower = i : upper = i;
  }
  return -1;
};