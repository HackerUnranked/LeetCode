# Check if two trees are the same
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using a stack and dfs! Iterative solution!
# Space O(n)
# Time  O(n)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        stacks = [p,q]
        
        while stacks:
        
            r1 = stacks.pop()
            r2 = stacks.pop()

            # these are cases where the node exists only for one and not both,
            # return false            
            if r1 and not r2:
                return False
            if r2 and not r1:
                return False
            if r1 and r2:
                # return false if the values don't match
                if r1.val != r2.val:
                    return False
                else:
                    # append the children
                    stacks.append(r1.right)
                    stacks.append(r2.right)
                    stacks.append(r1.left)
                    stacks.append(r2.left)
        
        return True

    # recursive solition
    # space O(1)
    # time O(n) 
    def isSameTree_recursive(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        if p.val != q.val:
            return False
            
        r = self.isSameTree(p.right, q.right)
        l = self.isSameTree(p.left, q.left)
            
        return l & r