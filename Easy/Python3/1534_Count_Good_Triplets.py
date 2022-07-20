from typing import List

# Given an array of integers arr, and three integers a, b and c. You need to 
# find the number of good triplets.

# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are 
# true:

#     0 <= i < j < k < arr.length
#     |arr[i] - arr[j]| <= a
#     |arr[j] - arr[k]| <= b
#     |arr[i] - arr[k]| <= c

# Where |x| denotes the absolute value of x.

# Return the number of good triplets.

# Example 1:

# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

# Example 2:

# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        # brute force method, where we use nested for loop to check the permutation of
        # triplets in the list to see if it satisfies the condition
        
        count = 0 # count to count the triplets that match
        for x in range(len(arr)): # loop the starting array at idx 0 - len(nums)
            for y in range(x + 1, len(arr)): # loop the rest of the array from x + 1 to len
                for z in range(y + 1, len(arr)): # loop the third array from y + 1
                    # see if the condition is satisfied and incrememnt if so
                    if abs(arr[x] - arr[y]) <= a and abs(arr[y] - arr[z]) <= b and abs(arr[x] - arr[z]) <= c:
                        count += 1
        
        return count