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

# no dummy node
class Solution_1:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        prev = None
        
        while curr:
            if curr.val == val:
                if curr == head: # if current is pointing at head
                    head = head.next # move head over because we have a new head
                    prev = head # point prev to headhead it is the new previous
                else:
                    prev.next = curr.next # have previous disconnect from the current node
            else:
                prev = curr # we just point it to previous because it doesn't match he value to be removed
            
            curr = curr.next # move over
        
        return head

class Solution_2:
    def removeElements(self, ListNode, val: int) -> ListNode:
        # Don't use dummy node and keep changing head if the value of head
        # matches val
        while head and head.val == val:
            if head.val == val:
                head = head.next
        
        # return none if head is none. We reach this case if all the nodes are equal to val
        if not head:
            return None

        # No we loop the list starting where head is because we made sure head
        # is not equal to val
        current = head

        while current.next:
            # If my next is equal to the val then I change my next pointer to skip it
            # example:
            #
            # head is 4, val is 3
            # 4 -> 3 -> 7
            #
            # change 4 to point to 7:
            # 4 -> 7
            #
            # Proceed to check if 
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head 