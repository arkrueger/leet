// passes all tests

// https:  // leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
#include <iostream>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
 public:
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