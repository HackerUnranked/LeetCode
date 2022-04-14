# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

#            3
#          /   \
#         5      1
#        / \    / \
#       6   2  9   8
#          / \ 
#         7   4


#       3                3 
#     /   \            /   \
#    5     1          5      1
#   / \   / \        / \    / \
#  6   2  9  8      6   2  9   8
#     / \              / \ 
#    7   4            7   4

# For example, in the given tree above, the leaf value sequence is (5, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root0 and root2 are leaf-similar.

# Input: root0 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = []
        l2 = []
        
        def traverse(a_root, a_list):
            if not a_root:
                return
            if a_root.right == None and a_root.left == None:
                a_list.append(a_root.val)
            
            traverse(a_root.left, a_list)
            traverse(a_root.right, a_list)
            
        traverse(root1, l1)
        traverse(root2, l2)
        
        if len(l1) != len(l2):
            return False
        
        for x in range(0,len(l1)):
            if l1[x] != l2[x]:
                return False
            
        return True