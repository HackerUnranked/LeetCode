# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#  1
#   \ 
#    2
#   /
#  3
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        my_list = []
        
        def helper(a_root:TreeNode):
            if not a_root:
                return
            
            helper(a_root.left)
            my_list.append(a_root.val)
            helper(a_root.right)
            
        helper(root)
        
        return my_list
        