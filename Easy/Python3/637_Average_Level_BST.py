from typing import List
from collections import defaultdict, deque

# Given the root of a binary tree, return the average value of the nodes on each 
# level in the form of an array. Answers within 10-5 of the actual answer will 
# be accepted.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, 
# and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:

# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # iterative solution using a dictionary 
    def averageOfLevels_dic(self, root: TreeNode) -> List[float]:
        dic = defaultdict(list)
        q = deque([(root, 0)])
        
        # bfs traversal using deque
        while q:
            node, level = q.popleft() # gets the to the left of the queue
            dic[level].append(node.val) # map the level to then node val
            
            # add the node and level to the queue
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        # sort the dictionaries by k value and sum the list values then return the average
        return [ sum(dic[x]) / len(dic[x]) for x in sorted(dic.keys())]

    # this is using a bucket so we don't have to sort, still iterative solution
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        bucket = [0] * (10 ** 4)
        q = deque([(root, 0)])
        
        # bfs traversal using deque
        while q:
            node, level = q.popleft() # gets the to the left of the queue
            
            if bucket[level] == 0:
                bucket[level] = (node.val, 1) # tuple of the node vale and how many we have
            else:
                # get the count and total of the elements
                amount, counts = bucket[level]
                amount += node.val
                counts += 1
                bucket[level] = (amount, counts)
            
            # add the node and level to the queue
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        return [x[0] / x[1] for x in bucket if x != 0] 