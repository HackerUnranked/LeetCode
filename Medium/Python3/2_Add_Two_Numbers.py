
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