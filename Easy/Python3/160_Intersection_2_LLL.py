from typing import List

# Given the heads of two singly linked-lists headA and headB, return the node at
# which the two lists intersect. If the two linked lists have no intersection at
# all, return null. For example, the following two linked lists begin to 
# intersect at node c1:

# 1 -> 2 -> 3 -> 4 -> 5
#     /
#    /
# a ->
#
# Return 2 because that's where they intersect

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        my_set = set()
        
        head_a = headA
        head_b = headB
        
        while head_a:
            my_set.add(head_a)
            head_a = head_a.next
        
        while head_b:
            if head_b in my_set:
                return head_b
            
            head_b = head_b.next
        
        return None