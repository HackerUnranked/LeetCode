from typing import List

# Given two string arrays words1 and words2, return the number of strings that 
# appear exactly once in each of the two arrays. 

# Example 1:

# Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
# Output: 2
# Explanation:
# - "leetcode" appears exactly once in each of the two arrays. We count this 
#    string.
#
# - "amazing" appears exactly once in each of the two arrays. We count this 
#    string.
#
# - "is" appears in each of the two arrays, but there are 2 occurrences of it in 
#    words1. We do not count this string.
#
# - "as" appears once in words1, but does not appear in words2. We do not count 
#    this string.
#
# Thus, there are 2 strings that appear exactly once in each of the two arrays.

# Example 2:

# Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
# Output: 0
# Explanation: There are no strings that appear in each of the two arrays.

# Example 3:

# Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
# Output: 1
# Explanation: The only string that appears exactly once in each of the two 
# arrays is "ab".

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a = {}
        b = {}
        
        # get the ones that appear only once in words1
        for x in words1:
            if x not in a:
                a[x] = 1
            else:
                a[x] += 1
        
        # get the ones that appear only once in words2
        for y in words2:
            if y not in b:
                b[y] = 1
            else:
                b[y] += 1
        
        count = 0
        
        # loop one dictionary and check the count, if the count is one
        # and in both then increment count
        for z in a:
            if z in b:
                if a[z] == 1 and b[z] == 1:
                    count += 1
        
        return count