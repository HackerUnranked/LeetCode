from typing import List

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of 
# size 2 where:

#     answer[0] is a list of all distinct integers in nums1 which are not 
#     present in nums2.
#
#     answer[1] is a list of all distinct integers in nums2 which are not 
#     present in nums1.

# Note that the integers in the lists may be returned in any order. 

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas 
# nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, 
# answer[0] = [1,3].
#
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas 
# nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, 
# answer[1] = [4,6].

# Example 2:

# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since 
# nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

class Solution:
    # Uses a bucket of bools to find the ones that are in either sets
    def findDifference_bool_arr(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # mark the ones we seen
        a = [False] * 2001
        b = [False] * 2001
        
        # capture the ones that are unique
        c = set()
        d = set()
        
        # mark the ones we seen in nums1
        for x in nums1:
            if x < 0:
                a[abs(x) + 1000] = True
            else:
                a[x] = True
        
        # mark the ones we seen in nums2
        for y in nums2:
            if y < 0:
                b[abs(y) + 1000] = True
            else:
                b[y] = True
        
        # loop and add to each set the ones
        # that are found in one but not the other
        for z in range(0,2001):
            if a[z] == True and b[z] == False:
                print(z)
                if z > 1000:
                    c.add(-abs(z - 1000))
                else:
                    c.add(z)
            elif a[z] == False and b[z] == True:
                if z > 1000:
                    d.add(-abs(z - 1000))
                else:
                    d.add(z)
            
        return [c, d]
    
    # Uses a set instead of arrays to find the matching ones and mismatches
    def findDifference_set(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)
        c = set()
        d = set()
        
        for x in nums1:
            if x not in nums2:
                c.add(x)
        
        for y in nums2:
            if y not in nums1:
                d.add(y)
        
        return [c, d]
    
    