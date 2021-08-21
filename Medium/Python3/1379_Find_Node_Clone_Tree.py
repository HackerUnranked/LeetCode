# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change the trees or the target node.
# The answer must be a reference to a node in the cloned tree.

# Follow up: Solve the problem if repeated values on the tree are allowed.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        capture = []
        capture.append(target)
        
        def helper(o: TreeNode, c:TreeNode, t, to_return):
            
            if not o:
                return None
            
            if o == t:
                to_return.append(c)
                return 
            
            helper(o.left, c.left, t, to_return)
            helper(o.right, c.right, t, to_return)
            
        helper(original, cloned, target, capture)
        return capture[1]