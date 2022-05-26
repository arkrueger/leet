/**
 * @param {string} s
 * @return {boolean}
 */

/*
approach:
    convert to lowercase and remove spaces, punctuation, etc
    two pointers, left and right
    converge from outer ends of the string
        if they are ever unequal, return false
        the loop should exclude the middle character and stop before the pointers converge
        
    actually, a better approach would be to stop when left < right is false
        looks cleaner and we don't have to do fancy floors to avoid the middle char
*/

var isPalindrome = function (s) {
  s = s.replace(/([^a-zA-Z0-9]+)/g, "");
  s = s.toLowerCase();
  // if the string is empty, it's technically a palindrome
  if (s === "") { return true; }

  // start pointers at opposite ends of the string and check for character equality
  let left = 0;
  let right = s.length - 1;
  while (right > left) {
    if (s[left] != s[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
};