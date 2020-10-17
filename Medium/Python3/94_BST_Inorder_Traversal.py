from typing import List

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
#
#  1
#   \
#    2
#   /
#  3
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
   # recursively
    def inorderTraversal(self, root:TreeNode):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root:TreeNode, res:List[int]):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)