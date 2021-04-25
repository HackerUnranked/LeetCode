# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        # if both exist than we will merge the two values together
        if root1 and root2:
            
            # here we create a new node
            root = TreeNode(root1.val + root2.val)
            
            # traverse left and right 
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            
            return root
        
        # return the value that exists
        else:
            return root1 or root2