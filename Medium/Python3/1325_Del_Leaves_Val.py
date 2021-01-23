# Given a binary tree root and an integer target,
# delete all the leaf nodes with value target.
# Note that once you delete a leaf node with value target, if it's parent node 
# becomes a leaf node and has the value target, it should also be deleted 
# (you need to continue doing that until you can't).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root:
            root.left = self.removeLeafNodes(root.left,target)
            root.right = self.removeLeafNodes(root.right,target)
            
            if (root.val) == target and (root.right == None) and (root.left == None):
                return None
            return root