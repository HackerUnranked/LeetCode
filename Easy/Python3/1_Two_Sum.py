from typing import List

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dic = {}
        
        for x,y in enumerate(nums):
            if target - y not in my_dic:
                # keep the value as the key and the index and the value
                # if we don't have it in the dictionary yet
                my_dic[y] = x
            # we have it in the dictionary
            else:
                return [my_dic[target-y],x]
                