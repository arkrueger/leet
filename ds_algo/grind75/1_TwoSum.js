/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/*
    approach:
        brute force: O(n^)
            two loops nested, check the sum of each against target
            skip cases where the loop indices are the same (same elem can't be used with itself)
            return early if sum is found
            return nothing otherwise (we assume a solution exists)
        
        hash map: O(n)
            declare a hashmap (dict or obj), which will contain key:value as sumcomplement:index
            loop through the array (only once)
                on each iteration, calculate complement = target - nums[i]
                check if the hashmap already contains the complement
                    if it does, then return the index(dict value) at the complement, and i
                if it does not, then add nums[i] to the hashmap (NOT add the complement)
        
        two pointer: O(n*log(n))
            the O-analysis is valid if we need to return numbers instead of indices
                otherwise, we'll need to search the original array for the indices -> add O(2n)
            create a copy of the array and sort the new array
            create two pointers ("left" and "right")
*/

// HASH MAP APPROACH
var twoSum = function (nums, target) {
  let hash = {};
  let complement; // will be target - nums[i]
  // loop over nums, check if complement is in hash, add nums[i] if not, return if found
  for (let i = 0; i < nums.length; i++) {
    complement = target - nums[i];
    if (hash.hasOwnProperty(complement)) { // if our complement exists, then we have a match
      // hash[complement] contains the index of the complement in nums
      // i is the index of the current element
      return [hash[complement], i];
    } else {
      // if we didn't find a match, store the current element and index in the map
      // this ensures that we will get a match in the hashmap for the current elem's complement when we see it later
      hash[nums[i]] = i;
    }
  }
};

// TWO POINTER APPROACH
// var twoSum = function(nums, target) {
//     // copy the array so we can preserve the original array order
//     sorted = [...nums];
//     sorted.sort((a, b) => a - b); // javascript makes me lose faith in humanity sometimes
//     // set up two "pointers" (in js, these will just be vars representing indices)
//     // "left" will point to the first index, "right" will point to the last index
//     let left = 0;
//     let right = nums.length - 1;
//     // loop while left < right (if they converge and we have not found, then there is no match)
//     do {
//         sum = sorted[left] + sorted[right];
//         // if they sum to target, we have a match so return the indices
//         // if they sum to less than target, then we need larger numbers 
//         // therefore increment left because we already checked the larger numbers right of right
//         // if they sum to greater than target, we need smaller numbers
//         // therefore decrement right because we already checked the smaller numbers left of left
//         // if this doesn't make sense, walk through the first few cases
//         // it should make sense then how we won't "miss" any potential combos
//         if(sum === target) {
//             // since we sorted the array, our indices don't map to the original array
//             // need to find the indices of the original array
//             // this breaks the O(n*logn) but would work in a similar problem where we only return nums, not indices
//             let newLeft = nums.findIndex(elem => elem === sorted[left]);
//             let newRight = nums.findIndex(elem => elem === sorted[right]);
//             // since we might have the same element twice and find will give us the first occurrence, we need to check if left and right are equivalent
//             // if they are, we can find sorted[right] in the subarray from newLeft + 1 onwards
//             if (newLeft === newRight) {
//                 let offset = newLeft + 1;
//                 newRight = offset + nums.slice(offset).findIndex(elem => elem === sorted[right]); 
//             }
//             return [newLeft, newRight];
//         } else if (sum < target) {
//             left++;
//         } else if (sum > target) {
//             right--;
//         }
//     } while (left < right);
// };

// BRUTE FORCE APPROACH
// var twoSum = function(nums, target) {
//     // nested loops
//     for(let i = 0; i < nums.length; i++) {
//         // start the inner loop just ahead of the outer to stay "below the diagonal" (no repeats)
//         for(let k = i+1; k < nums.length; k++) {
//             if(nums[i] + nums[k] === target) {
//                 return [i, k];
//             }
//         }
//     }
// };