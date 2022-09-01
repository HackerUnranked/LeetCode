# Given a binary tree with the following rules:

#     root.val == 0
#     If treeNode.val == x and treeNode.left != null, then 
#     treeNode.left.val == 2 * x + 1
#     
#     If treeNode.val == x and treeNode.right != null, then 
#     treeNode.right.val == 2 * x + 2

# Now the binary tree is contaminated, which means all treeNode.val have been 
# changed to -1.

# Implement the FindElements class:

#     FindElements(TreeNode* root) Initializes the object with a contaminated 
#     binary tree and recovers it.
#     
#     bool find(int target) Returns true if the target value exists in the 
#     recovered binary tree.

# Example 1:

# Input
# ["FindElements","find","find"]
# [[[-1,null,-1]],[1],[2]]
# Output
# [null,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1]); 
# findElements.find(1); // return False 
# findElements.find(2); // return True 

# Example 2:

# Input
# ["FindElements","find","find","find"]
# [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
# Output
# [null,true,true,false]
# Explanation
# FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
# findElements.find(1); // return True
# findElements.find(3); // return True
# findElements.find(5); // return False

# Example 3:

# Input
# ["FindElements","find","find","find","find"]
# [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
# Output
# [null,true,false,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
# findElements.find(2); // return True
# findElements.find(3); // return False
# findElements.find(4); // return False
# findElements.find(5); // return True

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: TreeNode):
        self.unique = {0} # holds the values of the number to find
        self.calculate(root, 0) # calculates the val of each node and store them in unique
        
    # check if the target number is in the set
    def find(self, target: int) -> bool:
        if target in self.unique:
            return True
        
        return False
    
    # calculates the node val and store that val in uniques so we can check if the value exists
    def calculate(self, root, val):
        if not root:
            return 
        # if we have a right then calculate the val and add it to the set then traverse right
        if root.right:
            temp = 2 * val + 2
            self.unique.add(temp)
            self.calculate(root.right, temp)
        # similar to above we check the left child here
        if root.left:
            temp = 2 * val + 1
            self.unique.add(temp)
            self.calculate(root.left, temp)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)