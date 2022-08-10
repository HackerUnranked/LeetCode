from typing import List

# Given two integer arrays nums1 and nums2, return an array of their 
# intersection. Each element in the result must be unique and you may return the 
# result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2)) # convert both to sets the take the intersection
    
    # another way but we return a set instead, i think this is kind of cheating
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bucket = [False] *  1001 # bucket to mark the ones we already seen
        
        for x in nums1:
            bucket[x] = True
        
        # return a set of the ones that matches
        return set([y for y in nums2 if bucket[y] == True]) 