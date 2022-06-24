# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        # helper function where we do inorder traversal to determin if the tree
        # is symmetrical  
        def helper(root_l, root_r):
            
            if not root_l and not root_r:
                return True
            # one is null and the other is a child, return False
            if root_l and not root_r:
                return False
            # same as the case above
            if root_r and not root_l:
                return False
            # the values don't match
            if root_r.val != root_l.val:
                return False
            
            l = helper(root_l.right, root_r.left)
            r = helper(root_l.left, root_r.right)
            
            return l & r 
        
        return helper(root,root)
    
    def isSymmetric_iterative(self, root: TreeNode) -> bool:
        
        stack = [root,root]
        
        while stack:
            # grab the roots to compare
            l = stack.pop()
            r = stack.pop()
            
            # in the case where root only exists for one node or vice versa then
            # we return false. being symettrical means either both nodes exists 
            # or don't via the opposite children
            if l and not r:
                return False
            if r and not l:
                return False
            # both nodes exists for opposite children, we meed to check of the
            # values they carry are the same
            if r and l:
                if r.val != l.val:
                    return False
                else:
                    # we are at the beginning
                    # append only the left and right
                    if l == root:
                        stack.append(l.left)
                        stack.append(r.right)
                    # append the childrens where each opposite child is mapped to
                    # the other
                    else:
                        stack.append(l.right)
                        stack.append(r.left)
                        stack.append(l.left)
                        stack.append(r.right)
            
        return True