from typing import List

# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct 
# string present in arr. If there are fewer than k distinct strings, return an 
# empty string "".

# Note that the strings are considered in the order in which they appear in the 
# array.

# Example 1:

# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned. 

# Example 2:

# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.

# Example 3:

# Input: arr = ["a","b","a"], k = 3
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings
# , we return an empty string "".

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {} 
        
        # map each string to a count for the occurence
        for x in arr:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
        
        count = 0
        
        for x in arr:
            # this string is unique we only seen it once
            if dic[x] == 1:
                count += 1 # increment the order
                # return the string if its the kth string
                if count == k:
                    return x
                
        return "" # there are fewer strings than kth