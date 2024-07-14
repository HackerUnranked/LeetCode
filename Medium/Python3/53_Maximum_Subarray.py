#Given an integer array nums, find the subarray with the largest sum, and return
# its sum. 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4] Output: 6 Explanation: The subarray
# [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1] Output: 1 Explanation: The subarray [1] has the largest sum
# 1.

# Example 3:

# Input: nums = [5,4,-1,7,8] Output: 23 Explanation: The subarray [5,4,-1,7,8]
# has the largest sum 23.

# Constraints:

#     1 <= nums.length <= 105
#     -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # This is using Kadane's algorithm. It is a dynamic prgramming approach
        current = 0 # the current sum
        max_sum = None # this is the current max, for initial we set it to None

        for num in nums:
            # Calculates the maximum of current + num and num itself. This step
            # decides whether to add num to the current subarray sum (current +
            # num) or start a new subarray with num as its first element (just
            # num). This decision is crucial because it ensures that current
            # always represents the maximum sum of a subarray ending at the
            # current position. If num is greater than the sum of the current
            # subarray, it means that the current subarray is not worth keeping.
            #
            # Example [-2, 1, -3, 4]  current = 0, num = -2, current = -2 for
            # the first iteration. current = max(-2, -2) = -2. For the second
            # iteration current = max(-2 + 1, 1) = 1. Since 1 is greater than
            # -1, we keep 1 as the current sum.
            current = max(current + num, num) 
            # set max sum if we are initial
            if max_sum == None:
                max_sum = current
            else:
                max_sum = max(current, max_sum) # get the max sum we have seen so far
        return max_sum