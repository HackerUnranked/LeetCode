# Given the head of a singly linked list where elements are sorted in ascending 
# order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in 
# which the depth of the two subtrees of every node never differ by more than 1. 

# Example 1:

# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the 
# shown height balanced BST.

# Example 2:

# Input: head = []
# Output: []
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # NOTE this question is the same as 108 except this is a linked list
        # so first we will push all the nodes in to a list then use the same
        # approach
        
        arr = [] # holds all the nodes of linkedlist
        
        cur = head
        
        # push all the nodes into the list
        while cur:
            arr.append(cur)
            cur = cur.next
        
        # create a balanced tree from the list
        def helper(root, the_arr):
            if not the_arr:
                return None
            
            mid = len(the_arr) // 2
            root = TreeNode(the_arr[mid].val)
            root.right = helper(root.right, the_arr[mid + 1:])
            root.left = helper(root.left, the_arr[:mid])
            
            return root
        
        result = helper(None, arr)
        
        return result