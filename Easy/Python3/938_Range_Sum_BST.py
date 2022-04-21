# Given the root node of a binary search tree, return the sum of values of all
# nodes with value between L and R (inclusive).

#The binary search tree is guaranteed to have unique values.

# Example 1:

# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# NOTE: need a better solution, currently we are traversing all of the nodes

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        total = []
        self.sums(root,L,R,total)
        return sum(total)
    
    def sums(self,root,L,R,total):
            
        if not root:
            return total
            
        self.sums(root.left,L,R,total)
        self.sums(root.right,L,R,total)
        if root.val >= L and root.val <= R:
            total.append(root.val)

class Solution_1:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        result = 0
        
        if root == None:
            return 0
        # root is smaller than the min so we go right
        if root.val < low:
            result += self.rangeSumBST(root.right,low,high)
        # go both directions and add the values, root is in-between
        elif root.val > low and root.val <= high:
            result += root.val
            result += self.rangeSumBST(root.left,low,high)
            result += self.rangeSumBST(root.right,low,high)
        # root is the lowest value so we go right
        elif root.val == low:
            result += root.val
            result += self.rangeSumBST(root.right,low,high)
        # if root is greater than the high then we go left
        elif root.val > high:
            result += self.rangeSumBST(root.left,low,high)
            
        return result