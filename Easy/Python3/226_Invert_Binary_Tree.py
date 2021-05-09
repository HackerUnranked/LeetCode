# given the root of a binary tree, invert the tree, and return its root.

#      4             4
#     / \           / \
#   2     7   ->  7     2
#  / \   / \     / \   / \
# 1   3 6   9   9   6 3   1  
#
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        
        def helper(the_root:TreeNode, s_root:TreeNode):
            
            if not the_root:
                return None
            elif not s_root:
                s_root = TreeNode(the_root.val,None,None)
            else:
                s_root.val = the_root.val
                
            s_root.right = helper(the_root.left,s_root.right)
            s_root.left = helper(the_root.right,s_root.left)
            
            return s_root
        
        copy_root = TreeNode(0,None,None)
        copy_root = helper(root,copy_root)
        return copy_root