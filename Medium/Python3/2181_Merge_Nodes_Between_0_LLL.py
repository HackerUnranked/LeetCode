# You are given the head of a linked list, which contains a series of integers 
# separated by 0's. The beginning and end of the linked list will have 
# Node.val == 0.

# For every two consecutive 0's, merge all the nodes lying in between them into 
# a single node whose value is the sum of all the merged nodes. The modified 
# list should not contain any 0's.

# Return the head of the modified linked list.

# Example 1:

# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 3 + 1 = 4.
# - The sum of the nodes marked in red: 4 + 5 + 2 = 11.

# Example 2:

# Input: head = [0,1,0,3,0,2,2,0]
# Output: [1,3,4]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 1 = 1.
# - The sum of the nodes marked in red: 3 = 3.
# - The sum of the nodes marked in yellow: 2 + 2 = 4.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        my_head = head.next
        curr = head
        num = 0
        
        while my_head:
            # we saw a zero
            if my_head.val == 0:
                num += my_head.val
                curr.val = num # set the zero to num sum
                curr.next = my_head # link the nodes
                num = 0 # reset zero
                if my_head.next == None:
                    curr.next = None
                    break
                else:
                    curr = my_head
                
            # we are not a zero so we just increment the sum
            else:
                num += my_head.val
            
            my_head = my_head.next
            
        return head