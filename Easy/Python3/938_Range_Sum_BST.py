# Given the root node of a binary search tree, return the sum of values of all
# nodes with value between L and R (inclusive).

#The binary search tree is guaranteed to have unique values.

# Example 1:

# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# NOTE: need a better solution, currently we are traversing all of the nodes

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        total = []
        self.sums(root,L,R,total)
        return sum(total)
    
    def sums(self,root,L,R,total):
            
        if not root:
            return total
            
        self.sums(root.left,L,R,total)
        self.sums(root.right,L,R,total)
        if root.val >= L and root.val <= R:
            total.append(root.val)