from typing import List

# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # Brute Force method
        nums = []
        dummy = ListNode(0)
        head = dummy
        for x in lists:
            while x:
                nums.append(x.val)
                x = x.next
        
        for x in sorted(nums):
            head.next = ListNode(x)
            head = head.next
        
        return dummy.next