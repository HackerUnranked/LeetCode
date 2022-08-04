# You are given the root of a binary tree where each node has a value 0 or 1. 
# Each root-to-leaf path represents a binary number starting with the most 
# significant bit.

#     For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could 
#     represent 01101 in binary, which is 13.

# For all leaves in the tree, consider the numbers represented by the path from 
# the root to that leaf. Return the sum of these numbers.

# The test cases are generated so that the answer fits in a 32-bits integer. 

# Example 1:

# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

# Example 2:

# Input: root = [0]
# Output: 0

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode, val=0) -> int:
        if not root:
            return 0
        
        # multiply by 2 which shifts left and we add the root val which can be a 0 or 1
        # example val = 2 which is 0010 in binary and the next value is 0, shift 1 to get
        # 0100 then we need to add root, if root is 1 then we get 0101 if root is 0 we stay
        # the same
        val = val * 2 + root.val
        
        # we are at the leaf node, return the val
        if root.left == None and root.right == None: 
            return val
        
        # return the sum
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)