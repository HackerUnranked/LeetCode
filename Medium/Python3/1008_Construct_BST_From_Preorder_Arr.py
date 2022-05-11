from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        root = TreeNode(preorder[0])
        my_stack = [root]
        idx = 1
        
        while idx != len(preorder):
            # if the value is less than what is in the stack then it is the left child
            if preorder[idx] < my_stack[-1].val:
                my_stack[-1].left = TreeNode(preorder[idx]) # connect as left child
                my_stack.append(my_stack[-1].left) # this is the new parent
            # pop from the stack while it is smaller than the last item, we stop when it is bigger, this means it's the right child of
            # the last item we popped
            else:
                while my_stack and my_stack[-1].val < preorder[idx]:
                    last = my_stack.pop()
                last.right = TreeNode(preorder[idx]) # connect the right child
                my_stack.append(last.right) # this is the new parent, push to stack
                
            idx += 1
   
        return root