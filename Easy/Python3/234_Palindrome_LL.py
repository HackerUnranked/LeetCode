# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node_vals = []
        
        curr = head
        # push all the nodes in an array so we can loop it
        while curr:
            node_vals.append(curr.val)
            curr = curr.next
        
        right = 0
        left = len(node_vals) - 1
        
        
        while right < len(node_vals) and left != 0:
            if node_vals[right] != node_vals[left]:
                return False
            right+= 1
            left -= 1
        
        return True