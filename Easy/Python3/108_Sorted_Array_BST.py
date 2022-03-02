from typing import List

# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two 
# subtrees of every node never differs by more than one.

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
#
#       0
#     /   \
#   -3     9
#  /     / 
#-10    5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.root = None
        
        def helper(root,a_nums):
            if not a_nums:
                return None
            mid = len(a_nums) //2
            a_root = TreeNode()
            a_root.val = a_nums[mid]
            a_root.right = helper(a_root.right,a_nums[mid+1:])
            a_root.left = helper(a_root.left,a_nums[:mid])
            
            return a_root
        
        self.root = helper(self.root,nums)
        return self.root