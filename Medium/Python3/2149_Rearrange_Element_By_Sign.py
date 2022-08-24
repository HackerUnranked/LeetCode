from typing import List

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should rearrange the elements of nums such that the modified array follows the given conditions:

#     Every consecutive pair of integers have opposite signs.
#     For all integers with the same sign, the order in which they were present in nums is preserved.
#     The rearranged array begins with a positive integer.

# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

# Example 1:

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

# Example 2:

# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        vals = [0]*len(nums) # create array size N
        
        idx = 0 # idx for the array
        idx_p = 0 # positive idx
        idx_n = 1 # negative idx
        
        # traverse the array and keep track of where we will insert the positive and negative number
        while idx < len(nums):
            # if i see a positive number
            if nums[idx] > 0:
                vals[idx_p] = nums[idx] # add the positive with where the positive idx is in the new array
                idx_p += 2 # move the positive idx over 2
            # I saw a negative number
            else:
                vals[idx_n] = nums[idx] # add the negative number in the new array 
                idx_n += 2 # move the negative idx
                
            idx += 1 # increment the idx
                
        return vals
    
    # using right half and left half as sorting for positive and negative numbers
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        holder = [0] * len(nums) # sort positives at left half and negatives at right half
        
        start = 0
        end = len(nums) // 2
        
        for x in nums:
            # add at left half
            if x > 0:
                holder[start] = x
                start += 1
            # add at right half
            else:
                holder[end] = x
                end += 1
        
        # add to list traversing from left and right half
        left = 0
        right = len(holder) // 2
        ans = []
        
        while right != len(holder):
            ans.append(holder[left])
            ans.append(holder[right])
            right += 1
            left += 1
        
        return ans
            