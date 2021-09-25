# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        a = [] # store the nodes
        temp = head
        
        # push the nodes onto the list
        while temp:
            a.append(temp)
            temp = temp.next
        
        # if we have a list of 0,1,2 we leave because we don't need to reorder
        if len(a) < 3:
            return head
        
        temp = head
        even = True
        half = len(a) // 2 # get the half
            
        if len(a) % 2 != 0:
            even = False
            
        count_me = 0 # counts the halfway mark
        
        while temp:
            
            to_add = a.pop() # get a node

            # on an even list the last pairing is already pointed to correctly
            # we are at the halfway mark and just need to point the last node to
            # None, example:
            # 1 2 3 4 5 6
            # 1 6 pair then 2 4 pair, 3 4 is already paired so we disconnected 4 from 5, point it to None
            if temp.next == to_add:
                to_add.next = None
                break
            
            to_add.next = temp.next # pointer to my current next pointer
            temp.next = to_add # connect second pointer to third
            count_me += 1 # count how many we popped
            
            # if we are at the half
            # for an odd we have the following pairing
            # 1 2 3 4 5 6 7
            # 1 7, 2 6, 3 5, 4 has no one to pair with it stays last, diconnect it from 5
            # 1 7 2 6 3 5 4
            if count_me == half:
                new_me = a.pop()
                new_me.next = None
                break
                
            temp = temp.next.next # move over 2
            
        return head