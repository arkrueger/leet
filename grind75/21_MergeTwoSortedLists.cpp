/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

/*
approach:
    start with the lower val head
    while(we have not yet reached the tail on BOTH lists)
        have a concept of "next node" for each list
        have a concept of "tail" (i.e. current node) of the newly merged list
            compare nexts, select the lower (if equal, select first)
            link tail to lower val node
            designate lower as new tail
            designate new tail -> next as next node for that list
        
*/

// Time: O(n+m) where n and m are the list lengths
// Space O(1)
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // we will use this to keep track of the current node (last merged node)
        ListNode * tail;
        // call the new list merged (points to merged list head)
        ListNode * merged;
        
        // check if the lists even exist
        if(!list1) { return list2; }
        if(!list2) { return list1; }
        // compare head node values, start the new list at the lower val (or equal) head
        if (list1->val > list2->val) {
            merged = list2; 
            list2 = list2->next;
        } else {
            merged = list1;
            list1 = list1->next;
        }
        // merged stores the head, tail will be moving forward along the new list
        tail = merged;
        
        while(list1 && list2) {
            // point the list to the next lowest val node
            // move that list forward along the chain
            if (list1->val < list2->val) {
                tail->next = list1; // point tail to the lower val next node
                list1 = list1->next; // move lower val node forward
                tail = tail->next; // move tail forward
            } else {
                tail->next = list2; 
                list2 = list2->next;
                tail = tail->next;
            }
        }
        // if either list (there should only be one) still has more nodes ahead, point to that list
        list1 ? tail->next = list1 : tail->next = list2;
        return merged;
    }
};