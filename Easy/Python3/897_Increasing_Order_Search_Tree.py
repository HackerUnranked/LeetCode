# Given the root of a binary search tree, rearrange the tree in in-order so that 
# the leftmost node in the tree is now the root of the tree, and every node has 
# no left child and only one right child.

# Example 1:

# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

# Example 2:

# Input: root = [5,1,7]
# Output: [1,null,5,null,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = [] # store all the nodes inorder
        
        # inorder traversal to store the nodes
        # from least to greatest in the list
        def inorder(r):
            if not r:
                return
            
            inorder(r.left)
            l.append(r)
            inorder(r.right)
            
        inorder(root)
        
        # connect the nodes bit stop at the last one so we can
        # disconnect it since it doesn't have any children
        for x in range(len(l) - 1):
            l[x].right = l[x + 1] # point the left child to the next node
            l[x].left = None
        
        # set the children of the last node to none since it's a leaf node
        l[len(l) - 1].right = None
        l[len(l) - 1].left = None
        
        return l[0]