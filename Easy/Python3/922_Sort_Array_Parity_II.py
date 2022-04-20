from typing import List

# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

# Example 2:

# Input: nums = [2,3]
# Output: [2,3]

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        to_add = []
        
        if nums == None:
            return
        elif len(nums) == 0:
            return
        
        for x in nums:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        
        for y in even:
            to_add.append(y)
            to_add.append(odd.pop())
        
        return to_add
        
class Solution_1:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        beg = 0
        end = len(nums) -1
        
        # first we sort the array to have the evens at the beginning half and the odds at the ending half
        while beg < end:
            # if we are not even
            if nums[beg] %2 != 0:
                # check if the end is even and swap if it is
                if nums[end] %2 == 0:
                    temp = nums[beg]
                    nums[beg] = nums[end]
                    nums[end] = temp
                    beg += 1 # move foward 1
                    end -= 1 # go backwards 1
                else:
                    end -= 1 # the end is odd so we move left to check if that value is even
            # move foward because we are even
            else:
                beg += 1
        
        beg = 1 # start at one because it's the first even number we want to swap
        mid = (len(nums) // 2) # this is the start of the odd half
        
        # loops while the right half hasn't been finished swapping to even and odd pair
        while beg < mid:
            temp = nums[beg] # grab the even to be swapped on the left half
            nums[beg] = nums[mid] # swap the even with the odd on the right half
            nums[mid] = temp # replace the odd with the even from the left half
            beg += 2 # move over 2 so we can skip over 1 even number on the left half to get the even odd pair
            mid += 1 # move over one on the right half because we replaced an odd 
        
        return nums
             