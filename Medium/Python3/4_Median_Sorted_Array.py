from typing import List

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.

# Follow up: The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        
        if len(nums3) == 0:
            return None
        elif len(nums3) == 1:
            return nums3[0]
        else:
            nums3.sort()
            
            if len(nums3)%2 == 0:
                mid = len(nums3)//2
                return (nums3[mid - 1] + nums3[mid])/2
            else:
                return nums3[len(nums3)//2]
                