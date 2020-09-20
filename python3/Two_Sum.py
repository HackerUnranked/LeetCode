from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment not in hash_table:
                hash_table[nums[i]] = i
            else:
                return [hash_table[compliment], i]