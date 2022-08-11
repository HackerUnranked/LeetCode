from typing import List

# Given an array of distinct integers arr, find all pairs of elements with the 
# minimum absolute difference of any two elements.

# Return a list of pairs in ascending order(with respect to pairs), each pair 
# [a, b] follows

#     a, b are from arr
#     a < b
#     b - a equals to the minimum absolute difference of any two elements in arr

# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with 
# difference equal to 1 in ascending order.

# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]

# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort() # sort the array
        small = float('inf')
        b = []
        
        # bubble sort, swap the elements if
        # the ones adjacent to it is bigger
        '''
        for x in range(len(arr)):
            for y in range(len(arr) - x - 1):
                if arr[y] > arr[y + 1]:
                    temp = arr[y]
                    arr[y] = arr[y +1]
                    arr[y + 1] = temp
        '''
        
        
        # selection sort, find the smallest and swap it to the
        # current idx
        
        '''
        for x in range(len(arr)):
        # loop the elements from [x....n]
            for y in range(x+1,len(arr)):
            # if element x is bigger than y then we swap 
                if arr[x] > arr[y]:
                    q = arr[x]
                    arr[x] = arr[y]  # swap 4 and 1
                    arr[y] = q # [1,20,4,21,22,3,24,100]
        '''
        
        # find the minimum difference
        for a in range(len(arr) - 1):
            if abs(arr[a] - arr[a + 1]) < small:
                small = abs(arr[a] - arr[a + 1])
        
        # add the numbers that make the min difference into the
        # matrix
        for c in range(len(arr) - 1):
            if abs(arr[c] - arr[c + 1]) == small:
                b.append([arr[c], arr[c + 1]])
        
            
        return b # return