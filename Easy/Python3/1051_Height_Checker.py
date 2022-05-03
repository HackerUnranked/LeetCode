from typing import List

# A school is trying to take an annual photo of all the students. The students 
# are asked to stand in a single file line in non-decreasing order by height. 
# Let this ordering be represented by the integer array expected where 
# expected[i] is the expected height of the ith student in line.

# You are given an integer array heights representing the current order that the
# students are standing in. Each heights[i] is the height of the ith student in 
# line (0-indexed).

# Return the number of indices where heights[i] != expected[i].

# Example 1:

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

# Example 2:

# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]
# All indices do not match.

# Example 3:

# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]
# All indices match.

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        my_list = []
        
        # copy the list so we can compare
        for z in heights:
            my_list.append(z)
    
        # implementing bubble sort
        for x in range(len(heights)):
            for y in range(0,len(heights) - x - 1):
                if heights[y] > heights[y+1]:
                    temp = heights[y]
                    heights[y] = heights[y+1]
                    heights[y+1] = temp
        
        count_me = 0
        for v in range(len(heights)):
            if heights[v] != my_list[v]:
                count_me += 1
        
        return count_me