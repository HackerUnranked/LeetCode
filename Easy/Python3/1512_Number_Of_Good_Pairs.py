from typing import List

#Given an array of integers nums.

#A pair (i,j) is called good if nums[i] == nums[j] and i < j.

#Return the number of good pairs. 

#Example 1:

#Input: nums = [1,2,3,1,1,3]
#Output: 4
#Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # this is the fastest solution at 90% speed 
        uniqueOnes={}
        numPairs = 0
        
        for x in nums:
            if not x in uniqueOnes:
                uniqueOnes[x]=0
            uniqueOnes[x]+=1
        
        for y in uniqueOnes:
            appear = uniqueOnes[y]

            #this equation gives us the total numnber of possible pairs
            output+=(appear*(appear-1)//2)
        
        #BRUTE FORCE
        #brute_count = 0
        #for x in range(len(nums)):
        #    for y in range(x+1,len(nums)):
        #        if nums[x] == nums[y]:
        #            brute_count += 1

        return output