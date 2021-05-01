# Given the root of a binary tree, find the maximum absolute value of 
# subtracting the node value of an child node from it's ancestor 

# example tree
#   1
#  / \
# 3   2
#    /
#   3
#
# Some of the examples from the given tree above:
# |1 -3| = 2
# |1 -2| = 1
# |1 -3| = 2
# |2 -3| = 1
#
# We return 2 because that is the max difference 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # this keeps track of the biggest difference between ancestor and node
        self.result = 0
        
        # a helper function
        # max_val is the max ancestor value and min val is the minimum node value
        # that is not an ancestor
        def helper(node, max_val, min_val):
            
            if not node:
                return
            
            # subtract the biggest ancestor from the current node value
            # subtract the smallest ancestor from the node value
            # compare the results of the two above with the self.results and store it
            self.result = max(self.result, abs(max_val-node.val),abs(min_val-node.val))
            
            #update the min and max values if they need to change
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            
            helper(node.left, max_val, min_val)
            helper(node.right, max_val, min_val)
            
        
        helper(root, root.val, root.val)
        return self.result

# let the following be an example of the problem, NOTE we use pre-order traversal hence visting the current root first
#  1
# / \
#3   2
#   /
#  3
#
# 1. On initial we pass helper(root,1,1) because we are at root, self.result is 1
# 2. max_val is 1 and so is min_val
# 3. self.result is 0 because on initial we only have root
# 4. we go left so we have, helper(root.left,1,1)
# 5. self.result = (0, (max_val - 3), (min_val -3))
# 6. we get 3 from the left child, note self.result is now 2 because min_val and max_val is 1
# 7. min_val is 1 from root, and max val is 3 from the left child
# 8. now we look at the right child and repeat the steps, in the end we return self.result