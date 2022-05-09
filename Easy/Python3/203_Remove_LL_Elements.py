# Remove all occurence of an element from a linked list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy
        
        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt # set dummy node to equal new head the first go round
            else:
                prev = curr # we just point it to previous because it doesn't matcht he value to be removed
            
            curr =curr.next # move over
        
        return dummy.next
                