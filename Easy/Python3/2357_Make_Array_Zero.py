from typing import List

# You are given a non-negative integer array nums. In one operation, you must:

#     Choose a positive integer x such that x is less than or equal to the 
#     smallest non-zero element in nums.
#
#     Subtract x from every positive element in nums.

# Return the minimum number of operations to make every element in nums equal to 
# 0. 

# Example 1:

# Input: nums = [1,5,0,3,5]
# Output: 3
# Explanation:
# In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
# In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
# In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

# Example 2:

# Input: nums = [0]
# Output: 0
# Explanation: Each element in nums is already 0 so no operations are needed.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        bucket = [False] * 101 # keeps track of the uniques
        count = 0 # count how many uniques we have
        
        # we don't care about duplicates because two same numbers
        # will take the same number of moves to make zero. We return
        # the number of uniques because each unique number needs x moves
        # to get to zero and if we traverse from small to big we are essentially
        # doing process of elimination removing the next smallest one and so on
        #
        #
        # example: a = [1,4,2,3,4]
        # 1. remove 1 to get [3,1,2,3] hence we removed the smallest from
        # 2. next remove the next smallest, [2,1,2] #we removed 1, do it again
        # 3. [1,1]
        # 4. next do it again, [0], since the number is a duplicate it still
        # uses one move
        # total 4 moves which is equal to the number of uniques, 
        
        for x in nums:
            # if we have seen the character, mark it as seen
            if bucket[x] == False and x != 0:
                bucket[x] = True
                count += 1
        
        return count # return how many are unique
            