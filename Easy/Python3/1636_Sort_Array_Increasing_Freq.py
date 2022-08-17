from typing import List

# Given an array of integers nums, sort the array in increasing order based on 
# the frequency of the values. If multiple values have the same frequency, sort 
# them in decreasing order.

# Return the sorted array.

# Example 1:

# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a 
# frequency of 3.

# Example 2:

# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in 
# decreasing order.

# Example 3:

# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        bucket1 = [ [] for x in range(len(nums) + 1)] # map each appearance to a 
                                                      # list of numbers since 
                                                      # different numbers can 
                                                      # appear the same ammount 
                                                      # of times
        bucket2 = [0] * 201 # holds how many times a number appears
        holder = []
        
        # count the occurence of each number
        for num in nums:
            idx =  num
            if num < 0:
                idx = abs(num) + 100
                
            bucket2[idx] += 1
        
        # map each occurence to the amount via bucket
        for x, y in enumerate(bucket2):
            if y != 0:
                temp = x
                if x > 100:
                    temp = -(x - 100)
                    
                if bucket1[y] == []:
                    bucket1[y] = [temp]
                else:
                    bucket1[y].append(temp)
        
        # sort the items
        for idx2, things in enumerate(bucket1):
            if things != []:
                if len(things) > 1:
                    # bubble sort to sort the list because there are 2 numbers with the same occurence
                    for idx3 in range(len(things)):
                        for idx4 in range(0, len(things)- idx3 - 1):
                            # swap if the current element is greater than the next element
                            if things[idx4] > things[idx4 + 1]:
                                temp = things[idx4]
                                things[idx4] = things[idx4 +1]
                                things[idx4 + 1] = temp
        
        # create the array
        for idx1, val in enumerate(bucket1):
            # if there is only 1 thing in the list then add it
            if len(val) == 1:
                holder += val * idx1 # add the number x times where idx tells us how many times it appears
            # we need to loop and add
            elif len(val) > 1:
                # loop backwards because we need the numbers in decreasing vals as the problem suggested
                for idx2 in reversed(val):
                    holder += [idx2] * idx1
                
                
        return holder