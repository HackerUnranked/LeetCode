# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes. Only nodes itself may be
# changed.

# Example 1:

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            current.next = second
            first.next = second.next
            second.next = first
            current = current.next.next
        return dummy.next

# Note this is without dummy node
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        current = head
        prev = head
        
        while current:
            # example in the beginning we have 1 2 3 4 where head is 1 and current
            if current == head:
                # example 1 2 3 4
                # head, current = 1
                head = head.next # move head over one because it should be 2 after we swap
                # head = 2
                # current = 1
                
                current.next = head.next # current's next pointer now points to 3 since we will swap 1 and 2
                # head = 2
                # current = 1
                # current.next = 3
                # 2 3 4
                #   |
                #   1
                
                head.next = current # head which is 2 now, it's next pointer will now point to current which is 1
                # head = 2
                # current = 1
                # current.next = 3
                # 2 1 3 4
                # head.next = 1
                
                prev = current # current is the previous node, which is 1
            else:
                # we are at the last node and it has no adjacent to swap, just return
                if current.next == None:
                    return head
                
                prev.next = current.next # 1 points to 4, 2 1 3 4, current is 3
                # head = 2
                # 2 1 4 -
                #     |
                #     3
                #
                
                temp = current.next # hold the next pointer, in this case it's 4
                current.next = current.next.next # disconnect from 3 and connect to none
                # 2 1 4
                # 3
                #
                #
                
                temp.next = current # 4 next pointer points to 3
                # 2 1 4 3
                prev = current # prev is 3 in this case 
                
            current = current.next # move to the next pair to swap
                
        return head