# Given the root of a binary tree, return the leftmost value in the last row of the tree.
# NOTE they are not asking about a node that is on the left, they are asking for 
# the leftmost on the last row

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        
        for node in queue:
            queue += filter(None, (node.right, node.left))
        
        return node.val

# BFS meaning we visit every level first before visiting the next level
# Give the tree Below:
#        1
#      /   \
#     2     3
#
# Example 1 :
# queue is [1]
# Using filter we add 2 and 3 into the list
# queue is now [1,3,2]
# next we look at 3 the the right child and filter returns None because it doesn't have any children
# next we look at 2 and filter returns none because it's left and right doesn't have any children
# we are at the end of the list and we return 2 because that was the last node we looked at
#  

# Example 2:
# 1, queue is [1]
# we just return 1 because it is the last node we looked at and has no children 
# 
# Example 3:
#   1
#  / 
# 3
# first we have 1 in the queue then we add 3 because it has no right child
# next we look at 3 and don't add anything to the queue because it has no child
# return 3, it is the last node we looked at
# 
# Example 4:
#     2
#   /   \ 
#  1     4
#         \
#          5
# In example above we return 5 because it is the last row

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        
        for node in queue:
            queue += filter(None, (node.right, node.left))
        
        return node.val
        
        