# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Am N-ary tree is where the root node has N children
#              1
#           /  |  \
#          3   2   4
#        /  \
#       5    6

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root == None:
            return 0
        
        depth = 0
        
        for x in root.children:
            depth = max(depth ,self.maxDepth(x))
                
        return depth + 1

  
    # So for the first test case it'll look like
    # first call is the call with root 1
    # depth = 0 -> second call with child 3 -> 
    # it has 2 children so there'll be two calls from for loop
    # call with child 5 -> sets the for loop with child of 5 which is None (Null)
    # this call hits base case and returns 0
    # the same happens with child 6
    # call to child 6 from the for loop -> child of 6 is None -> returns 0
    # depth = max(0, 0) -> depth = 0
    # return to one level higher -> call to child 5 reaches return statement ->
    # depth = 1
    # call to child 6 reaches return statement and it returns 1 ->
    # current depth is 1 because child 5 set it -> max(1, 1) -> depth = 1
    # return to one more level higher
    # call to child 3 reaches return statement ->
    # depth was equal to 1 now it becomes 2 (depth + 1)
    # now it's turn to children 2 and 4 to be called
    # the story is exactly the same as with 5 and 6 only depth is now 2 ->
    # both 2 and 4 return depth 1 that's why it's rejected by max(2, 1)
    # depth remains 2
    # and finally everything returns to the very first call with root 1 
    # it reaches return statement and returns 2+1=3