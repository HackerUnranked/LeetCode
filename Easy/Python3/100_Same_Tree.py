# Check if two trees are the same
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p == None and q == None:
            print("hello word")
            return True
        if p == None:
            return False
        if q == None:
            return False
        
        a_root = []
        b_root = []
        
        a_root.append(p)
        b_root.append(q)

        # we use preorder traversal in iterative form, first visit the parent
        # then the children        
        while len(a_root) > 0 and len(b_root) > 0:
            a = a_root.pop()
            b = b_root.pop()
            
            if a.val != b.val:
                return False
            if a.right and b.right:
                a_root.append(a.right)
                b_root.append(b.right)
            if b.left and a.left:
                a_root.append(a.left)
                b_root.append(b.left)
            
            # b has a right but a doesnt
            if b.right and a.right == None:
                return False
            # b has a left but a doesnt
            if b.left and a.left == None:
                return False
            # a has a right but b doesnt
            if a.right and b.right == None:
                return False
            # a has a left but be doesnt
            if a.left and b.left == None:
                return False
                   
        return True