### GRIND 75 SECOND PASS ###

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
approach:
    two pointers / tandem list traversal:
        keep track of two pointers, one for each list, starting at their heads
        keep track of head (set to the lower-valued of the two list heads)
        loop:
            select the lower-valued pointer
            set its next node as the other pointer
            move the pointer forward on the growing list
            move "other" to the candidate node that was not selected (requires a swap variable)
        after looping, point the growing list to other, if other exists (these are guaranteed to be larger)
        return the head
    
    recursion:
        essentially boils down to traversal
        base case is we reach the end of the list and return (we return nothing)
        on each function call, pass the current tail of the growing list, and the other list's current node
"""
# recursive
# T: O(n)
# S: O(1) but maybe O(n) because we create pointers to the lists on each function call?
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # this edge case just makes the code ugly and adds no algorithmic value, why are empty lists even a test case bro
        if not list1:
            return list2
        if not list2:
            return list1
        # determine the start of the list (pick the smaller head, or select list1 if they are equal)
        head = list1 if list1.val < list2.val else list2
        other = list2 if head == list1 else list1
        self.recursive(head, other)
        return head
    
    # helper function
    def recursive(self, merged: Optional[ListNode], other: Optional[ListNode]) -> None:
        # compare natural list's next node with other and point merged towards the lower of the two
        if merged.next: # if the merged list still has natural next components
            # point merged.next to the lower-valued of the two (keep as is if that's merged's natural next node)
            if merged.next.val < other.val:
                # keep as is, just move merged forward
                pass
            else:
                # need a temporary swap pointer for this
                temp = merged.next
                merged.next = other
                other = temp
            # regardless of above, we always move merged forward to the next node (and we know this next node exists)
            merged = merged.next
            self.recursive(merged, other)
        elif other: # if the merged list has reached its natural end, but other still has nodes to attach
            merged.next = other
            return
        else: # if merged has reached its natural end and other is empty
            return


# two pointers/tandem traversal
# T: O(n + m) where n and m are the list lengths
# S: O(1)
class __Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if either list is empty, or if both lists are empty (though not explicit, these cover the latter case)
        if not list1:
            return list2
        if not list2:
            return list1
        # pointer for each list
        head = list1 if list1.val < list2.val else list2 # new head which we will return
        merged = head
        other = list2 if list1 == head else list1
        while merged.next:
            # compare the two candidate nodes and point merged towards the lower one
            if merged.next.val < other.val:
                merged = merged.next
            else:
                temp = merged.next # cache the next one in the merged because we're about to point towards the other list
                merged.next = other # point towards the other list
                merged = merged.next # move the front of the growing list forward
                other = temp # put the now-orphan next node from the other list into other
        # attach the remaining list items if we still have any in the other list
        if other:
            merged.next = other
        return head
            
    def printList(self, head: Optional[ListNode]) -> None:
        while head.next:
            print(head.val, end="->")
            head = head.next
        print(head.val, "->|")
        
        
        
        
        
        
        