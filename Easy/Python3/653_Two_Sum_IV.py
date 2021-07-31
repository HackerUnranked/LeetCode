from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class my_Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        if not root:
            return False
        
        the_nums = []
        
        self.self_helper(root, the_nums)
        uniques = {}
        
        for x in the_nums:
            if not uniques:
                uniques[x] = k -x
            else:
                if (k -x) in uniques:
                    return True
                else:
                    uniques[x] = k-x
        
        return False
            
    
    def self_helper(self, root: TreeNode, nums: List):
        if not root:
            return
        
        nums.append(root.val)
        self.self_helper(root.left,nums)
        self.self_helper(root.right, nums)

class Solition_1:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self.__findTarget(root, set(), k)

    def __findTarget(self, root: TreeNode, nodes:set, k: int):
        if not root:
            return False
        
        toFind = k - root.val
        if toFind in nodes:
            return True
        
        nodes.add(root.val)
        
        if self.__findTarget(root.left, nodes, k):
            return True
        if self.__findTarget(root.right, nodes, k):
            return True