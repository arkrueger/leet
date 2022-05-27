/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

/*
approach:
    create a hash map (use an object as a dict-style hashmap) of the characters in first string
        i.e. if we have an e, add a property 'e': '1'
            if we have two e's, increment the value stored in the prop
    loop through the second string and check if each character exists in the hash map and is nonzero
        decrement the value if > 1
        return false if the property doesn't exist
    
    return true after the loop if we didn't return early

*/

// hash map approach
var isAnagram = function (s, t) {
  // if the strings are of unequal length, return early
  if (s.length !== t.length) { return false; }

  // convert both strings to lowercase
  s = s.toLowerCase();
  t = t.toLowerCase();

  // create a hash map on the first string
  let hash = {};
  // initialize the hash with the relevant characters
  for (let i = 0; i < s.length; i++) {
    // init to 1 if new, increment if already exists
    hash.hasOwnProperty(s[i]) ? hash[s[i]]++ : hash[s[i]] = 1;
  }

  // check the second array for compatibility with the hash map
  for (let k = 0; k < t.length; k++) {
    if (hash[t[k]] && (hash[t[k]] > 0)) {
      hash[t[k]]--;
    } else {
      return false;
    }
  }
  // if we didn't return early, then the strings were anagrams
  return true;
};