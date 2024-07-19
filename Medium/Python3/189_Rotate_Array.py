# Given an integer array nums, rotate the array to the right by k steps, where k
# is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3 Output: [5,6,7,1,2,3,4] Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6] rotate 2 steps to the right:
# [6,7,1,2,3,4,5] rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2 Output: [3,99,-1,-100] Explanation: rotate
# 1 steps to the right: [99,-1,-100,3] rotate 2 steps to the right:
# [3,99,-1,-100]

 

# Constraints:

#     1 <= nums.length <= 105 -231 <= nums[i] <= 231 - 1 0 <= k <= 105

 

# Follow up:

#     Try to come up with as many solutions as you can. There are at least three
#     different ways to solve this problem. Could you do it in-place with O(1)
#     extra space?

from typing import List
 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {}
        l = len(nums)
        k = k % l  # Ensure k is within the bounds of the array length

        # Correctly calculate new_idx for each element and store in dictionary
        for idx, num in enumerate(nums):
            new_idx = (idx + k) % l  # Correct formula to calculate new index
            dic[new_idx] = num

        # Update the original array with the rotated values from the dictionary
        for key, value in dic.items():
            nums[key] = value
    
    # Tthis is the recursive solution
    def rotate_recursion(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l  # Ensure k is within the bounds of the array length
        self.helper(0, nums[0], nums, 0, k)
    
    def helper(self, idx, num, arr, num_item, k):
        if num_item > len(arr):
            return
        new_idx = (idx + k) % len(arr) # get the new index of the number
        temp = arr[new_idx] # store the number we are replacing
        arr[new_idx] = num # update the new idx with the current number
        num_item += 1 # increment count
        self.helper(new_idx, temp, arr, num_item, k)

