# Check if two trees are the same
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # if they are both Null then return true
        if p == q and q == None:
            return True
        # only one of them is None so we return false
        if p == None:
            return False
        if q == None:
            return False
        
        list_1 = []
        list_2 = []
        
        # visit the parent first
        list_1.append(p)
        list_2.append(q)
        
        # User preorder traversal and visit the children node
        # to compare if the trees are the same
        while len(list_1) > 0 and len(list_2) > 0:
            # grab the node in stack to compare
            root_1 = list_1.pop()
            root_2 = list_2.pop()
            
            # the Values don't match return false
            if root_1.val != root_2.val:
                return False
            # the second tree has a right child but the first tree doesn't
            if root_2.right and root_1.right == None:
                return False
            # if the second tree has a left child but the first tree doesn't
            if root_2.left and root_1.left == None:
                return False
            # if the first tree has a right child but the second tree doesn't
            if root_1.right and root_2.right == None:
                return False
            # if the first tree has a left child but the second tree doesn't
            if root_1.left and root_2.left == None:
                return False
            
            # if either of them match then grab the children and append it so we can search
            # and compare
            if root_1.right and root_2.right:
                list_1.append(root_1.right)
                list_2.append(root_2.right)
            if root_1.left and root_2.left:
                list_1.append(root_1.left)
                list_2.append(root_2.left)
                
        return True