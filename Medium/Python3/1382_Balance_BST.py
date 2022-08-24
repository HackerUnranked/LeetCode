# Given the root of a binary search tree, return a balanced binary search tree 
# with the same node values. If there is more than one answer, return any of 
# them.

# A binary search tree is balanced if the depth of the two subtrees of every 
# node never differs by more than 1. 

# Example 1:

# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

# Example 2:

# Input: root = [2,1,3]
# Output: [2,1,3]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # NOTE: This question is the same as 108
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        inorderArr = [] # helps us sort the numbers in ascending value
        
        # call the function to create a balanced BST
        self.inorder_traversal(root, inorderArr)
        
        # helper function to create balanced BST
        def helper(a_root, a_nums):
            
            if not a_nums:
                return None
            
            mid = len(a_nums) // 2 # get the mid of the list
            
            a_root = TreeNode(a_nums[mid]) # create a new node
            a_root.right = helper(a_root.right,a_nums[mid+1:]) # traverse right with right half of array
            a_root.left = helper(a_root.left,a_nums[:mid]) # traverse left with left half of array
            
            return a_root # return root
        
        result = helper(None, inorderArr)
        
        return result 
    
    # inorder traversal so we can get the array sorted
    def inorder_traversal(self, root, arr):
        if not root:
            return
        
        self.inorder_traversal(root.left, arr)
        arr.append(root.val)
        self.inorder_traversal(root.right, arr)
        
    '''
    Find largest
    def find(self, root) -> int:
        if not root.right:
            return root.val
        
        right = 0
        left = 0
        
        if root.right:
            right = self.find(root.right)
        else:
            left = self.find(root.left)
        
        if right < left:
            return left
        
        return right
    '''