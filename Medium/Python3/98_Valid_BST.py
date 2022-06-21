# Definition for a binary tree node.

#Given the root of a binary tree, determine if it is a valid binary search tree (BST).

#A valid BST is defined as follows:

#    The left subtree of a node contains only nodes with keys less than the node's key.
#    The right subtree of a node contains only nodes with keys greater than the node's key.
#    Both the left and right subtrees must also be binary search trees.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def validate(node, left, right):
            if not node:
                return True
            # this means root is greater than the right and smaller than the left
            # which we know not to be true since a BST left is always smaller than the root
            # and the right is greater, therefore we return False
            if not(node.val < right and node.val > left):
                return False
            
            # we go left so we leave the left boundary the same but change the right boundary
            # because for a left child it has to be smaller than root
            left = validate(node.left, left, node.val)
            
            # the opposite is said for going right, the right must be greater than root
            # so we change the right boundary
            right = validate(node.right, node.val, right)
            
            return left and right
        
        # we use - infinity and infinity as the left right boundary where
        # -inf < root < inf where -inf become node.val if we are going left since
        # all of the left nodes are smaller than root. also let inf become node.val where
        # going right because the right nodes are greater than root
        return validate(root, float("-inf"), float('inf'))
            