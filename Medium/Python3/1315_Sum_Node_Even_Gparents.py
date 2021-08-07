# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.ans = 0
        
        def preorder (r: TreeNode, gparent: TreeNode, parent: TreeNode):
            
            if gparent and (gparent.val%2 == 0):
                self.ans += r.val
            
            if r.left:
                preorder(r.left,parent, r)
            
            if r.right:
                preorder(r.right, parent, r)
        
        if root:
            preorder(root, None, None)
    
        return self.ans