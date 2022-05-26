// class Solution {
// public:
//     // standard approach4
//     // O(logn) because each operation cuts the array in 2 and we run until there's no array left
//     int search(vector<int>& nums, int target) {
//         int upper = nums.size()-1;
//         int lower = 0;
//         int i = 0;

//         // if target is less than the first index or greater than the last, it's not in the list
//         if((target < nums[0]) || (target > nums[upper])) {
//             return -1;
//         }
//         // check if upper or lower are target; helps with the edge case where array length is 2
//         if(target == nums[lower]) { return 0; }
//         if(target == nums[upper]) { return upper; }

//         while(true) {
//             i = (lower + upper)/2;

//             // return the index if we found a match
//             if(target == nums[i]) { return i; }
//             // if lower and upper are adjacent, we checked everything so return
//             if(upper - lower == 1) { return -1; }

//             // adjust the bounds if no match
//             target > nums[i] ? lower = i : upper = i;
//         }
//         return -1;
//     }
// };
