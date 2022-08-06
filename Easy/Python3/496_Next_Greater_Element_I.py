from typing import List

# The next greater element of some element x in an array is the first greater 
# element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where 
# nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
# and determine the next greater element of nums2[j] in nums2. If there is no 
# next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next 
# greater element as described above. 

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so 
#   the answer is -1.
#
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so 
#   the answer is -1.

# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so 
#   the answer is -1.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        a = []
        
        # map the number to the index
        for x, y in enumerate(nums2):
            dic[y] = x
        
        # if the number is in the dictionary, find the biggest
        # number to the right of it
        for b in nums1:
            
            found = False # flag if we found the number
            temp = nums2[dic[b]:] # slice the array to only search the right half
            # loop and find if the biggest to the right
            for c in temp:
                if b < c:
                    found = True
                    a.append(c)
                    break
            # append -1 we didn't find a number bigger
            if found == False:
                a.append(-1)
                           
        return a

    def nextGreaterElement_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # NOTE: the idea of this algorithm is we create a dictionary and map
        # all the numbers in nums1 to -1 where -1 is the bigggest number to the
        # right of nums1[i]
        
        # next we push all the numbers from nums2 into a stack
        # and we check everytime if the previous number we pushed
        # is bigger than the number we're about to push. if it is
        # it means that it's the closest number to the right that is
        # bigger. lastly we check if the previous number is in the dictionary
        # so we can see if we need to add it to the list. if it is
        # then map the it to the number bigger than it in the dictionary.
        # loop the dictionary and return the numbers at the end
        #
        #
        # example: nums1 = [4, 1, 2] nums2 = [1, 3, 4, 2], dic = {4: -1, 1: -1, 2: -1}
        #
        # loop nums2
        # 1. push 1 because there is nothing in the stack
        # 2. check if 1 is less than 3 since 1 is the last item in the stack
        # 3. check if 1 is in the dictionary and map 3 to it if it is
        # 4. push 3 to the stack , repeat 1 - 4
        
        # dic so we can map the nums1 to an index, we start at -1 
        # because there are no number bigger than it on the right 
        # we return -1
        dic = {x : -1 for x in nums1}
        stack = [] # keeps track of all the numbers
        
        # loop all the numbers we have available
        for num in nums2:
            # check if we have anything in the stack and if
            # the current number is bigger than our last number
            while stack and stack[-1] < num:
                # remove the previous number and check if it is in the ditionary
                prev_num = stack.pop()
                if prev_num in dic:
                    dic[prev_num] = num # mapp the previous number to the one closest to it that's bigger
                    
            stack.append(num) # append the number into the stack
            
        return [dic[x] for x in nums1] # loop the dictionary and return the values of then number bigger to the right