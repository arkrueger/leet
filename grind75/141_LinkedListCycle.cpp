/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

/*
approaches:
    two pointers, iterate
        move fast 2 positions forward per iteration, slow 1 per iteration
        check for pointer equality between fast and slow
        return true if equality is found
        return false if any node has no next node

*/

class Solution {
 public:
  bool hasCycle(ListNode *head) {
    ListNode *fast = head;  // will move forward 2 nodes per op
    ListNode *slow = head;  // will move forward 1 node per op
    // if there is a cycle, eventually fast will catch up with slow

    // return false if the list is empty
    if (!head) {
      return false;
    }

    while (fast->next) {
      // if there is a tail node, there can't be a cycle so return false
      if (!fast->next->next) {
        return false;
      }
      // otherwise, continue playing chase
      fast = fast->next->next;
      slow = slow->next;
      if (fast == slow) {
        return true;
      }
    }
    // if we exited the while loop because fast->next was nullptr, return false
    return false;
  }
};
