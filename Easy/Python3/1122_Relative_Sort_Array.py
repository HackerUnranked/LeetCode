from typing import List

# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all 
# elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are 
# the same as in arr2. Elements that do not appear in arr2 should be placed at 
# the end of arr1 in ascending order. 

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

# Example 2:

# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        # bucket to map where we map num to the idx and occurence to arr[idx]
        bucket = [0] * (max(arr1) + 1)
        
        # counting the occurence
        for y in range(len(arr1)):
            bucket[arr1[y]] += 1
        
        
        bob = [] # array to create 
        
        # loop arr2 and find the amount
        # of occurence then add it to the array
        for x in arr2:
            if bucket[x] != 0:
                # create a list of size bucket[x] with the element [x] 
                # then append it to bob
                bob += ([x] * bucket[x]) 
                bucket[x] = 0 # set the count to zero for later we can loop and get the missing ones in order
        
        # loop and append the missing ones
        for a, b in enumerate(bucket):
            if b != 0:
                bob += ([a] * bucket[a])
        
        return bob
        
        