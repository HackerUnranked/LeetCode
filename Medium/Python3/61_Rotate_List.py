

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        # NOTE this question is basically asking the new head is the kth from the end of the list
        # given k = 2 and a list [1,2,3,4,5], 4 would be the new head because it is 2 nodes away from the end
        # split the list where the new head is and connect it with the old head
        # split from [4,5] and join with [1,2,3] to get [4,5,1,2,3]
        
        curr = head
        size = 1 # count for num of nodes
        
        # base case if there is no node we can't rotate therefore return none
        if curr == None:
            return None
        # if we only have one node then whatever we rotate we end up with the same
        # answer, just return curr
        if curr.next == None:
            return curr
        
        # loop until the last node and count how many nodes we have
        while curr.next:
            curr = curr.next
            size += 1
        
        # if we know k and the size of the list then we can know how many
        # nodes we have to traverse before we reach the node that is kth from
        # the end of the list
        
        # example: size is 5 and k is 2 therefore we need to traverse 3 nodes to reach the node
        # that is second to last
        
        # k % size == 0 we just return head because we end up back at the original head
        if k % size == 0:
            return head
        # if k is greater than size then we need to calculate how many nodes we have
        # to traverse to get to k
        # take the mod which gives us how many away from the end then subtract it from size
        # to get how many nodes we are to traverse
        if k > size:
            size = size - (k % size)
        # if the k is smaller then we just need to subtract it from size
        else:
            size = size - k
        
        # we make a circular linked list so we can disconnect easily
        curr.next = head
        
        # keep traversing until we reached the kth node from the end
        while size != 0:
            curr = curr.next
            size -= 1
        
        # update head it is the next node
        head = curr.next
        curr.next = None # disconnect the list from being circular to singular
        
        return head