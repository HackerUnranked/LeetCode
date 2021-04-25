# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:

        def find_tree_depth(node:TreeNode):

            if not node:
                return 0
        
            leftval = find_tree_depth(node.left) + 1
            rightval = find_tree_depth(node.right) + 1

            if leftval > rightval:
                return leftval
            else:
                return rightval
    
        def find_depth_leave_sum(root:TreeNode, depth_count:int):
 
            if not root:
                return 0
        
            if depth == depth_count:
                self.ans += root.val

            find_depth_leave_sum(root.left, depth_count+1)
            find_depth_leave_sum(root.right,depth_count+1)
        
        depth = find_tree_depth(root)
        # 1 is the depth count for starting
        self.ans = 0
        depth = find_depth_leave_sum(root,1)
        return self.ans
    