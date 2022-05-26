// passes all test cases

// https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
#include <iostream>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
 public:
  ListNode *detectCycle(ListNode *head) {
    // if no cycle, we don't bother checking for the cycle start
    if (!hasCycle(head)) {
      return NULL;
    } else {
      // let's do a similar thing to fast and slow
      // let's hold one node steady as a bookmark once fast and slow catch up to each other
      // then let's slowly walk a "guess" node from head outwards, running through the cycle (the bookmark tells us when we go around the cycle)
      // this will be O(n^2) in speed but O(1) in memory

      // since we know there is a loop we can grab just a subset of hasCycle
      ListNode *fast = head->next;
      ListNode *slow = head->next;
      ListNode *bookmark = nullptr;
      ListNode *guess = head;
      while (true) {
        // move fast forward by 2, slow forward by 1
        fast = fast->next;  // first
        fast = fast->next;  // second
        slow = slow->next;  // only once
        // if fast or slow are head again, then the cycle begins at head
        if ((fast == head) || (slow == head)) {
          return head;
        }
        // now that slow and fast are advanced, let's check if they are equal
        if (fast == slow) {
          bookmark = slow;
          break;
        }
      }
      // could have this in the original while loop, but for readability's sake (and to avoid ops on fast) it's separate
      while (true) {
        // keep using slow because we've been advancing it by 1 by convention
        slow = slow->next;
        // if slow hits guess, then we have our cycle start point
        if (slow == guess) {
          return guess;
        }
        // if slow hits bookmark, then we completed a cycle, so move guess forward
        if (slow == bookmark) {
          guess = guess->next;
        }
      }
    }
  }

  bool hasCycle(ListNode *head) {
    // check corner case
    // head does not exist
    // head is the only node
    if (!head || !head->next) {
      return false;
    }
    // first, set both fast and slow to the node after head
    ListNode *fast = head->next;
    ListNode *slow = head->next;

    // begin iterating over the nodes
    // we know it is a cycle if we see head again
    // we know it is a cycle if fast == slow (fast catches up with slow, i.e. came around the loop)
    // we know it is not a cycle if next is null
    while (true) {
      // move fast forward by 2
      if (fast->next) {
        fast = fast->next;
        if (fast->next) {
          fast = fast->next;
          // if tail, there's no cycle
          if (!fast->next) {
            return false;
          }
        } else {
          return false;
        }
      } else {
        return false;
      }
      // move slow forward by 1
      if (slow->next) {
        slow = slow->next;
      } else {
        return false;
      }

      // now that slow and fast are advanced, let's check if they are equal
      if (fast == slow) {
        return true;
      }
      if ((fast == head) || (slow == head)) {
        return true;
      }
    }
  }
};