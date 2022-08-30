from typing import List

# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest 
# vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the 
# y-axis (i.e., infinite height). The widest vertical area is the one with the 
# maximum width.

# Note that points on the edge of a vertical area are not considered included in
# the area.

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # grab the x coordinate and sort it then find the adjacent of
        # the sum and return the max with the greatest adjacent sum
        ans = []
        sum_vals = []
        
        for point in points:
            ans.append(point[0])
        
        ans.sort()
        
        # find the width of the adjacent points
        for idx in range(len(ans) - 1):
            sum_vals.append(abs(ans[idx] - ans[idx + 1]))
        
        # return the max sum of the difference for each adjacent points
        return max(sum_vals)
        