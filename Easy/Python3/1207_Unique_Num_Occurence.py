from typing import List

# Given an array of integers arr, return true if the number of occurrences of 
# each value in the array is unique, or false otherwise.

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values 
# have the same number of occurrences.

# Example 2:

# Input: arr = [1,2]
# Output: false

# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        bucket = [0] * 2001 # count the bucket, 
        counts = [False] * 2001 # marker to mark the num occurence as seen
        
        for idx in range(len(arr)):
            # for negatives we map to the second half of the array 
            a = arr[idx]
            if a < 0:
                a = abs(a) + 1000
            # map to index
            bucket[a] += 1
        
        # mark the occurence to True if we seen it
        for idx in range(len(bucket)):
            # we haven't seen this occurence, mark it true
            if bucket[idx] != 0 and counts[bucket[idx]] == False:
                counts[bucket[idx]] = True
            elif bucket[idx] != 0:
                return False # we already seen this occurence
        
        return True # this occurences are unique
            