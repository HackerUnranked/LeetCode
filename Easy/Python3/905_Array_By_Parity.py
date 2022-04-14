from typing import List

# Given an array A of non-negative integers, return an array consisting of all 
# the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

#Example 1:

#Input: [3,1,2,4]
#Output: [2,4,3,1]
#The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        
        for x in A:
            if x%2 == 0:
                evens.append(x)
            else:
                odds.append(x)
        
        evens.extend(odds)
        return evens
      # One liner solution below
      # return [i for i in A if i % 2 ==0]+[i for i in A if i % 2 != 0]
class Solution_1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        my_list = []
        
        for x in nums:
            if x % 2 == 0:
                my_list.insert(0,x)
            else:
                my_list.append(x)
        
        return my_list

# Modify in-space, O(1) space and O(n) time complexity
class Solution_2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        beg = 0
        end = len(nums) -1
        
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
        
        return nums
                    