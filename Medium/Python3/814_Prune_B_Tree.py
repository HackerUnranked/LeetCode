# We are given the head node root of a binary tree, where additionally every 
# node's value is either a 0 or a 1. Return the same tree where every subtree
# (of the given tree) not containing a 1 has been removed.

#(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        if root == None:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if root.val:
            return root
        else:
            if root.left or root.right:
                return root
            else:
                return None
        