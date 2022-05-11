# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
# such that every key of the original BST is changed to the original key plus
# the sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.

#              4   
#          /       \
#         1         6
#       /  \      /   \
#      0     2   5     7
#             \         \
#               3        8
#

#              4 ---becomes 30, 4 + 5 + 6 + 7 + 8 
#          /       \
#         1         6 -- 21, 6 + 7 + 8
#       /  \      /   \
#      0     2   5     7 --15, 7 + 8
#             \         \
#               3        8
#
# Note the question is asking us to change the node values of each node so
# that it becomes the sum of all the nodes that are greater than it plus itself
#
# In the above example above, 5,6,7,8 is greater than 4 so we add them to 4 to
# get 30 for the new root value
#
# for the node where it's value is 1 we would add, 1,2,3,4,5,6,7,8 which gives
# us 36 because all the numbers are greater than 1 besides 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # inorder traversal is visit my left then myself then my right
    # reverse inorder traversal, traverse right then left
    # sum val as we reach the leaf node and go back
    # up the call stack
    # using reverse inorder allows us to see the all the nodes from descending order
    # so we can sum them and add it to each node
    #
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # reverse inorder traversal
        if root.right: 
            self.bstToGst(root.right)
            
        root.val = self.val = self.val + root.val
        
        if root.left: 
            self.bstToGst(root.left)
        
        return root