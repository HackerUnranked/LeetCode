
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

class Solution:
    def addTwoNumbers(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
        
        head = None
        def helper(l_head: ListNode, list_1: ListNode, list_2: ListNode, carry: int):
            
            if list_1 == None and list_2 == None:
                if carry == 1:
                    l_head = ListNode(1, None)
                    return l_head
                else:
                    return None
                return None
            # there is only the 1 list remaining
            elif list_1 == None:
                # is there a carry over?
                if carry == 1:
                    # there is another carry over
                    if list_2.val == 9:
                        l_head = ListNode(0, None)
                        l_head.next = helper(l_head.next, list_1, list_2.next, 1)
                    else:
                        l_head = ListNode(list_2.val+1, None)
                        l_head.next = helper(l_head.next, list_1, list_2.next, 0)
                else:
                    l_head = ListNode(list_2.val, None)
                    l_head.next = helper(l_head.next, list_1, list_2.next, 0)
            # list 2 is remaining            
            elif list_2 == None:
                # is there a carry over?
                if carry == 1:
                    # there is another carry over
                    if list_1.val == 9:
                        l_head = ListNode(0, None)
                        l_head.next = helper(l_head.next, list_1.next, list_2, 1)
                    else:
                        l_head = ListNode(list_1.val+1, None)
                        l_head.next = helper(l_head.next, list_1.next, list_2, 0)
                else:
                    l_head = ListNode(list_1.val, None)
                    l_head.next = helper(l_head.next, list_1.next, list_2, 0)
                
            else:
                to_add = carry + list_1.val + list_2.val
                
                if to_add > 10:
                    mods = (to_add) % 10
                    l_head = ListNode(mods, None)
                    l_head.next = helper(l_head.next, list_1.next, list_2.next, 1)
                elif to_add ==  10:
                    l_head = ListNode(0, None)
                    l_head.next = helper(l_head.next, list_1.next, list_2.next, 1)
                else:
                    l_head = ListNode(to_add, None)
                    l_head.next = helper(l_head.next, list_1.next, list_2.next, 0)
                
            return l_head
        
        head = helper(head, l1, l2, 0)
        return head 

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1 = l1
        c2 = l2
        carry = 0
        
        #helper to traverse and calculate the carry
        def helper(temp2,acarry):
            
            while temp2:
                
                temp2.val += acarry
                
                # if we are 10 then set us to 0
                if temp2.val == 10:                    
                    temp2.val = 0
                    
                    if temp2.next == None and acarry == 1:
                        temp2.next = ListNode(1)
                        break
                else:
                    acarry = 0
                        
                temp2 = temp2.next
        
        while c1 or c2:
            
            # calculate
            carry, val = divmod(c1.val+c2.val+carry, 10)
            c1.val = val
            c2.val = val
            
            # both are at the last node
            if c1.next == None and c2.next == None:
                if carry == 1:
                    c1.next = ListNode(1)
                    
                return l1
            
            # we are at the last node of c1
            elif c1.next == None and c2.next:
                c1.next = c2.next # point the next pointer of the ending node to wherever c2 is
            
                if carry == 1:
                    helper(c2.next,carry)
                
                return l1
            
            # we are at the node of c2
            elif c1.next and c2.next == None:
                c2.next = c1.next # point me to c1
            
                # loop the rest of the list in case there is a carry on
                if carry == 1:
                    helper(c1.next,carry)
                
                return l2 # here we return l2 because l1 ended first
            
            c1 = c1.next
            c2 = c2.next
    
    # This solution is the simplest
    def addTwoNumbers3(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 # if l1 is not None then get the value of l1
            val2 = l2.val if l2 else 0 # if l2 is not None then get the value of l2
            total = val1 + val2 + carry # add the values of l1 and l2 and the carry
            carry = 1 if total > 9 else 0 # get the carry if the total is greater than 9 then carry is 1 else 0
            current.next = ListNode(total % 10) # get the remainder of the total and add it to the next node
            current = current.next
            
            # move to the next node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
    
    # This solution is the same as the previous one but it is more optimized for
    # space
    def addTwoNumbers4(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        carry = 0
        
        # Loop through the nodes of l1 and l2
        while l1 and l2:
            carry, l1.val = divmod(l1.val + l2.val + carry, 10) # get the carry and the remainder of the sum of l1 and l2
            # if both nodes have a next pointer then we keep moving to the next node
            if l1.next and l2.next:
                l1 = l1.next # move to the next node
                l2 = l2.next # move to the next node
            # break beacause we might have reached the end of l1 or l2 or both
            else:
                break
        
        # if l2 has more nodes than l1 then we point the next node of l1 to the
        # next node of l2 otherwise we do nothing because l1 has more nodes than l2
        if l2.next:
            l1.next = l2.next
        
        # loop through the remaining nodes of l1 nodes if there are any, please
        # note that we might have switched l1 and l2 from the logic above
        while l1.next:
            l1 = l1.next
            carry, l1.val = divmod(l1.val + carry, 10) # get the carry and the remainder of the sum of l1 and the carry
        
        # if there is a carry then we add a new node to the end of the list, the
        # last node has a value of 1 if there is a carry
        if carry:
            l1.next = ListNode(carry)
        
        return head