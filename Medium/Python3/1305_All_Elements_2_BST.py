from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        # inorder traversal to get all the nodes from each tree in ascending order
        def inorder(roota, l):
            
            if not roota:
                return
            
            inorder(roota.left, l)
            l.append(roota.val)
            inorder(roota.right, l)
        
        l1 = [] # list of root1 nodes from ascending order
        l2 = [] # list of root2 nodes from ascending order
        
        # traverse the 2 trees via inorder
        inorder(root1, l1)
        inorder(root2, l2)
        
        # if one of the tree's is empty the return the other list
        # because it is already sorted and we don't have to merge them
        if l1 == []:
            return l2
        if l2 == []:
            return l1
        
        # idx to keep track while we traverse to merge the two lists in the new one
        idx1 = 0
        idx2 = 0
        
        # the new list in sorted order to return
        l3 = []
        
        # loop while the idx has not reached the end of either lists
        while idx1 < len(l1) or idx2 < len(l2):
            
            if idx1 == len(l1):
                l3.append(l2[idx2])
                idx2 += 1
            elif idx2 == len(l2):
                l3.append(l1[idx1])
                idx1 += 1
            else:
                # if l1 is smaller then add it first
                if l1[idx1] < l2[idx2]:
                    l3.append(l1[idx1])
                    idx1 += 1
                # l2 is smaller
                elif l2[idx2] < l1[idx1]:
                    l3.append(l2[idx2])
                    idx2 += 1 
                else:
                    l3.append(l1[idx1])
                    l3.append(l2[idx2])
                    
                    idx1 += 1
                    idx2 += 1
        return l3