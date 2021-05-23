import typing
from typing import List

# Consider all the leaves of a binary tree, from left to right order, the values
# of those leaves form a leaf value sequence.For example, in the given tree 
# above, the leaf value sequence is (6, 7, 4, 9, 8).

#      3
#    /   \
#   5     1
#  / \   / \
# 6   2 9   8
#    / \
#   7   4

# Two binary trees are considered leaf-similar if their leaf value sequence 
# is the same. Return true if and only if the two given trees with head nodes
# root1 and root2 are leaf-similar.

# Example 1:
#      3              3
#    /   \          /   \
#   5     1        5     1
#  / \   / \      / \   / \
# 6   2 9   8    6   7 4   2
#    / \                  / \  
#   7   4                9   8
# 
# root1 = [6,7,4,9,8]
# root2 = [6,7,4,9,8] 
# Output = true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        root_list1 = []
        root_list2 = []
        answer = True
        
        def find_all_leaves(a_root: TreeNode, some_list: List):
            
            if a_root:
                
                # this is a leaf node
                if not a_root.left and not a_root.right:
                    some_list.append(a_root.val)
                
                find_all_leaves(a_root.left,some_list)
                find_all_leaves(a_root.right,some_list)
            else:
                return None
        
        
        find_all_leaves(root1,root_list1)
        find_all_leaves(root2,root_list2)
        
        if len(root_list1) != len(root_list2):
            answer = False
            return answer
        else:
            for x in range(len(root_list1)):
                if root_list1[x] != root_list2[x]:
                    answer = False
                    break
        
        return answer
              