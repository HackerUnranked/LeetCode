from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # give the following tree:
    #      3
    #     /  \
    #    9   20
    #       /  \
    #      15   7
    #
   
    # 
    # Inorder:
    #
    # inorder array  [9, 3, 15, 20, 7] -> left, root, right
    # 
    # 1. The left subtree is always left of root, 9 is the left subtree
    # 2. The right subtree is always right of root, 15 is the right subtree
    #
    # Preorder:
    #
    # preorder array [3, 9, 20, 15, 7] -> root, left, right
    #
    # 1. root is always the first node in the array
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder or not inorder:
            return None
        
        def build(start:int, end:int):
            
            nonlocal preIdx
            
            # This is our end case
            if start > end:
                return None
            
            # we're at the last node for the subtree
            elif start == end:
                node = TreeNode()
                node.val = preorder[preIdx]
                preIdx += 1
                
                return node
            
            rootVal = preorder[preIdx] # get the value of the preorder array
            rootIdx = in_dic[rootVal] # see where in the inorder array the value from preorder is
            root = TreeNode()
            root.val = rootVal
            preIdx += 1
            
            # for the left tree, it is from the beginning up to root
            root.left = build(start, rootIdx -1)
            
            # similar above the right subtree is always right of root for an inorder
            # we want all the values from root + 1 up until the end of the array 
            root.right = build(rootIdx+1, end)
            
            return root
        
        
        in_dic = {}
        preIdx = 0 # this is the index of the preorder array
        
        # store a hash table of where everthing is in the inoder array
        
        for idx,val in enumerate(inorder):
            in_dic[val] = idx
        
        return build(0, len(inorder)-1)
            
        
        