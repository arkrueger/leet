# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
approach:
    recursive:
        recursively find the end of the list
        then as we uwind the recursion, reverse the direction of the list
        
    iterative:
        loop through the list (e.g. a->b->c->d->e->f)
        on each iteration we see a window, e.g. c->d->e or prev->curr->next
            store next
            point curr to prev
            store curr in prev
            store next in curr
            exit when curr has no next and return curr as the new head
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # trivial cases
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None: 
            tail = head.next
            head.next = None
            tail.next = head
            return tail
        
        # head will be tail, so set its next variable to None
        first = head
        second = head.next
        first.next = None
        # recurse
        return self.helper(first, second)
    
    def helper(self, c: Optional[ListNode], n: Optional[ListNode]) -> Optional[ListNode]:
        # c means current and n means next, f will hold n.next
        # this gives c -> n -> f, which we will turn into c <- n | f
        # then recurse with n and f, i.e. helper(n, f)
        # how can we recurse without using lots of memory? -> link and then recurse
        
        # if n is the last node, link and return the last node
        if n.next is None:
            n.next = c
            return n
        
        f = n.next # f means future (i.e. next next)
        # point n to c
        n.next = c
        # recurse forward
        return self.helper(n, f)
    
    def printList(head: Optional[ListNode]) -> None:
        print("[ ", head.val, end =" ")
        node = head
        while node.next is not None:
            node = node.next
            print(node.val, end =" ")
        print(" ]")
        

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # trivial cases
#         if head is None:
#             return None
#         if head.next is None:
#             return head
#         if head.next.next is None: 
#             tail = head.next
#             head.next = None
#             tail.next = head
#             return tail
        
#         # init vars
#         p = head # prev
#         c = p.next # curr
#         p.next = None # prev (head) is now the tail, so point at nothing
#         n = c.next # next
        
#         while(c is not None):
#             n = c.next # store next
#             c.next = p # point curr to prev            
#             # preparing for the next iteration
#             p = c # move p forward
#             c = n # move c forward
#         return p
        
#     def printList(head: Optional[ListNode]) -> None:
#         print("[ ", head.val, end =" ")
#         node = head
#         while node.next is not None:
#             node = node.next
#             print(node.val, end =" ")
#         print(" ]")
        
        
