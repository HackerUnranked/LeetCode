# Given the head of a singly linked list, reverse the list, and return the 
# reversed list.


# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # solution using a list
    def reverseList_list(self, head: ListNode) -> ListNode:
        
        cur = head
        a = []
        
        if not head:
            return None
        
        # push all the nodes into the stack
        while cur:
            a.append(cur)
            cur = cur.next
        
        # get the last idx so we can
        # get the last node
        idx = len(a) - 1
        
        # loop starting at the last node and
        # connect the nodes up
        while idx != 0:
            a[idx].next = a[idx - 1]
            idx -= 1
        
        a[0].next = None # set first node to point to none
        
        return a[-1] # return the last node because it is now the new head
    
    # recursive solution
    def reverseList_recursive(self, head: ListNode, prev = None) -> ListNode:
        # NOTE: we need to reverse all of the direction of the pointer so they
        # point to the previous node and also we need to update head at the same time
        if not head:
            return prev
        
        temp = head.next # temp is the next pointer
        head.next = prev # head next points to the previous to reverse the pointer
        
        # we pass temp as head here it's the next node, we pass
        # head because it gets updated as the previous node when
        # we move along the list
        return self.reverseList(temp, head)
    
    # iterative solution
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        
        while cur:
            tmp = cur.next # temp is the next node
            cur.next = prev # reverse the node to point to the previous
            prev = cur # point the previous to the current node because it is now the new previous
            cur = tmp # move cur over to traverse
            
        return prev