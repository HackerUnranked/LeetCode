from typing import List

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:

# Input: root = []
# Output: []

# Example 3:

# Input: root = [1]
# Output: [1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        pre = []
        
        def helper(my_root, pre_list):
            if my_root == None:
                return None
            
            pre_list.append(my_root.val)
            helper(my_root.left, pre_list)
            helper(my_root.right, pre_list)
        
        helper(root,pre)
        
        return pre
