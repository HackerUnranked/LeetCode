from typing import List

# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the 
# largest pair sum in a list of pairs.

#     For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair 
#     sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

# Given an array nums of even length n, pair up the elements of nums into n / 2 
# pairs such that:

#     Each element of nums is in exactly one pair, and
#     The maximum pair sum is minimized.

# Return the minimized maximum pair sum after optimally pairing up the elements. 

# Example 1:

# Input: nums = [3,5,2,3]
# Output: 7
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

# Example 2:

# Input: nums = [3,5,4,2,4,6]
# Output: 8
# Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
# The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort() # sort the array
        
        # bubble sort
        '''
        for x in range(len(nums)):
            for y in range(0, len(nums) - x - 1):
                if nums[y] > nums[y + 1]:
                    temp = nums[y]
                    nums[y] = nums[y + 1]
                    nums[y + 1] = temp
        '''
        
        right = 0 # right idx
        left = len(nums) - 1 # left idx
        big = 0 # answer to return
        
        # map the smallest and biggest from right to left with
        # each other and take the max
        while right < left:
            big = max(big, nums[right] + nums[left])
            right += 1
            left -= 1
        
        return big
    
    def minPairSum_bucket(self, nums: List[int]) -> int:
        bucket = [0] * max(nums) # create a bucket to count the occurences and map
        
        # count each occurence and map
        for num in nums:
            bucket[num - 1] += 1
        
        right = 0 # right idx
        left = len(bucket) - 1 # left idx
        big = 0 # answer to return
        count = len(nums) # so we know how to exit after we paired all the numbers
        
        # map the smallest and biggest from right to left with
        # each other and take the max 
        while count != 0:
            if bucket[left] == 0:
                left -= 1
            if bucket[right] == 0:
                right += 1
            if bucket[left] != 0 and bucket[right] != 0:
                big = max(big, left + right + 2) # get the max
                count -= 2
                bucket[left] -= 1
                bucket[right] -= 1
                
        return big