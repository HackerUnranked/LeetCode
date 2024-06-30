from collections import deque

# Given a binary tree, find its maximum depth. The maximum depth is the number
# of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#   3
#  / \
# 9  20
#    /  \
#   15   7

# return its depth = 3.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        rightSub = self.maxDepth(root.right) + 1
        leftSub = self.maxDepth(root.left) + 1
        
        if rightSub < leftSub:
            return leftSub
        else:
            return rightSub
    
    # Shorter version of the above
    def maxDepthEasy(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

    # Using a queue to find the max depth, this is BFS. BFS visits all the nodes
    # at the current depth before moving on to the nodes at the next depth.
    # Given binary tree [3,9,20,null,null,15,7],
    #
    #   3
    #  / \
    # 9  20
    #    /  \
    #   15   7
    #
    # 9 is visted first then we push its children to the queue,
    # then 20 is visited and its children are pushed to the queue.
    # The depth is incremented as we visit each node. Next we visit 15 and 7.
    # and the process repeats until the queue is empty.  
    #
    def maxDepthQueue(self, root: TreeNode) -> int:    
        if not root:
            return 0   
        queue = deque([(root, 1)])  # Queue of (node, depth)
        max_depth = 0
        
        while queue:
            current_node, depth = queue.popleft()  # Get current node and its depth
            max_depth = max(max_depth, depth)  # Update max depth
            
            # Add children to the queue with incremented depth
            if current_node.left:
                queue.append((current_node.left, depth + 1))
            if current_node.right:
                queue.append((current_node.right, depth + 1))
        
        return max_depth  