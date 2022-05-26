/**
 * @param {string} s
 * @return {boolean}
 */

/*
approach:
    we sink any fully-formed pair we come across
    -> (), [], and {} are fully formed pairs
    -> we would evaluate {([])} as:
        steps 
            1: {([
            2: {([] <- a fully formed pair (open type = closing type, adjacent) -> sink []
            3: {(
            4: {() <- pair -> sink
            5: {
            6: {} <- pair -> sink
    notice this also works when we have adjacent pairs

*/


// Sink Valid Pairs with a stack approach (much faster)
// should be O(n)
var isValid = function(s) {
    let stack = [s[0]];
    let validPairs = ["()", "{}", "[]"];
    // iterate over the array
    let currentPair = "";
    let i = 1;
    while(i < s.length) {        
        // if our cursor is at a valid pair, sink that pair and move the cursor forwards
        currentPair = stack[0]+s[i];
        if(validPairs.includes(currentPair)) {
           // sink the pair (pop stack and move cursor forwards in string)
            stack.shift(); // pop the top off the stack
        } else {
            // if we didn't see a valid pair, push the current string index onto stack
            stack.unshift(s[i]);
        }
        // we have either sunk the pair or added the latest character to the stack
        // so move to the next character in the string
        i++;
    }
    // if stack contains no characters, we sunk everything so all brackets had valid complements
    // if stack still has characters, not all brackets had valid complements
    if(stack.length === 0) {
        return true;
    } else {
        return false;
    }
};


// Sink Valid Pairs approach
// var isValid = function(s) {
//     let idx = 0;
//     let validPairs = ["()", "{}", "[]"];
//     // iterate over the array
//     let i = 0;
//     while(i < s.length) {
        
//         // if our cursor is at a valid pair, sink that pair and move the cursor back by 1
//         if(validPairs.includes(s.slice(i,i+2))) {
//             s = s.slice(0,i).concat(s.slice(i+2)); // sink the pair
//             i -= 1;
//         } else {
//             i++;
//         }
//     }
//     // if s contains no characters, we sunk everything so all brackets had valid complements
//     // if s still has characters, not all brackets had valid complements
//     if(s.length === 0) {
//         return true;
//     } else {
//         return false;
//     }
// };


// half baked solution
// var isValid = function(s) {
//     let stack = s.slice(0,1);
//     s = s.slice(1,s.length);
//     let closing = ["(", "{", "["];
    
//     // on each iteration, pop the first element of the string off and evaluate it
//     for(let i = 0; i < s.length; i++) {
//         // check if we have a closing bracket
//         // if we do, check if it complements the top character of the stack
//         // if it does, sink that pair
//         // if it doesn't, return false
//         if()
//     }
//     // if we got to the end and stack.length > 0, then return false
//     // because not every bracket had a valid complement
// };