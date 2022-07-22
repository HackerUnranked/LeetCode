# Given the root of a binary tree, return the number of nodes where the value of 
# the node is equal to the average of the values in its subtree.

# Note:

#     The average of n elements is the sum of the n elements divided by n and 
#     rounded down to the nearest integer.
#
#     A subtree of root is a tree consisting of root and all of its descendants. 

# Example 1:

# Input: root = [4,8,5,0,1,null,6]
# Output: 5
# Explanation: 
# For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
# For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
# For the node with value 0: The average of its subtree is 0 / 1 = 0.
# For the node with value 1: The average of its subtree is 1 / 1 = 1.
# For the node with value 6: The average of its subtree is 6 / 1 = 6.

# Example 2:

# Input: root = [1]
# Output: 1
# Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        stack = []
        count = 0
        
        # counts how many nodes there are
        def count_nodes(a):
            if not a:
                return 0    
            return 1 + count_nodes(a.right) + count_nodes(a.left)
        
        # push all the nodes to stack
        def add_stack(s, r):
            if not r:
                return
            stack.append(r)
            add_stack(s, r.right)
            add_stack(s, r.left)
        
        # gets the sum of the nodes for the substree
        def sum_nodes(r1):
            if not r1:
                return 0
            
            return r1.val + sum_nodes(r1.left) + sum_nodes(r1.right)
        
        # add all the nodes to a stack
        add_stack(stack, root)
        
        # compute the average for each subtree using the nodes
        # on the stack and increment a count of the average is
        # equal to the val of the root subtree
        while stack != []:
            root_a = stack.pop()
            num = count_nodes(root_a) # count the number of nodes
            sum_node = sum_nodes(root_a)
            
            if sum_node // num == root_a.val:
                count += 1
        
        return count