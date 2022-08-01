from typing import List

# Given the root of an n-ary tree, return the preorder traversal of its nodes' 
# values.

# Nary-Tree input serialization is represented in their level order traversal. 
# Each group of children is separated by the null value (See examples)

# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]

# Example 2:

# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        stack = [root]
        arr = []
        
        if root == None:
            return []
        
        while stack:
            curr = stack.pop()
            arr.append(curr.val)
            stack.extend(curr.children)

        return arr[::-1]
            
            # root = 3
            # arr [3]
            # children = 4,5,6
            # stack now contains nodes 4 5 and 6
            # next we pop 6 and add all of it's children
            #
            # in the end we get arr = [3,6,5,4] but
            # we want post order so we visit the left vist and to do this
            # we just reverse the list by returning arr[::-1] to get
            # arr = [4,5,6,3]
        
        return arr[::-1]
        