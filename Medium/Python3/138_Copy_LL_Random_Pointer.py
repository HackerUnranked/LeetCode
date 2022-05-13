# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its 
# corresponding original node. Both the next and random pointer of the new nodes
# should point to new nodes in the copied list such that the pointers in the
# original list and copied list represent the same list state. None of the 
# pointers in the new list should point to nodes in the original list.


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# iterative solution
class Solution:
    def copyRandomList(self, head: Node) -> Node:
        dummy = Node(0)
        bob = dummy
        head1 = head
        dic = {} # holds all the nodes and pairs
        
        if not head:
            return None
        
        while head1:
            bob.val = head1.val
            dic[head1] = bob # map the equivalent of the original node to the deep copied node
            
            if head1.next:
                bob.next = Node(0)
        
            bob = bob.next
            head1 = head1.next
        
        head1 = head
        bob = dummy
        
        while head1:
            # if the random pointer points to nothing then we don't allocate new obj
            if head1.random not in dic:
                bob.random = None
            else:
                bob.random = dic[head1.random] # we found what the random pointer points to so we get the matched pair to point to it
            
            bob = bob.next
            head1 = head1.next
            
        return dummy
        
# recursive solution
class Solution:
    def copyRandomList(self, head: Node) -> Node:
        dic = {} # holds all the nodes and pairs
        dummy = None
        
        def helper(dum,temp_head,a_dic):
            if not temp_head:
                return None
            
            dum = Node(temp_head.val) # create a new node to copy
            a_dic[temp_head] = dum # map the node we seen to the equvilant of the one we deep copied so we can use it to determine what the random pointer points to
            
            dum.next = helper(dum.next,temp_head.next,a_dic) # call recursive
            
            # set the random pointer to none if it doesn't point to anything 
            if temp_head.random == None:
                dum.random = None
            # grab the random pointer and set it
            else:
                dum.random = a_dic[temp_head.random]
            
            return dum
        
        dummy = helper(dummy,head,dic)
        
        return dummy 