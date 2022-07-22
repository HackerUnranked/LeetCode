from typing import List
import math

# You are given an array points where points[i] = [xi, yi] is the coordinates of 
# the ith point on a 2D plane. Multiple points can have the same coordinates.

# You are also given an array queries where queries[j] = [xj, yj, rj] describes 
# a circle centered at (xj, yj) with a radius of rj.

# For each query queries[j], compute the number of points inside the jth circle. 
# Points on the border of the circle are considered inside.

# Return an array answer, where answer[j] is the answer to the jth query. 

# Example 1:

# Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
# Output: [3,2,2]
# Explanation: The points and circles are shown above.
# queries[0] is the green circle, queries[1] is the red circle, and queries[2] 
# is the blue circle.

# Example 2:

# Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
# Output: [2,3,2,4]
# Explanation: The points and circles are shown above.
# queries[0] is green, queries[1] is red, queries[2] is blue, and queries[3] is 
# purple.

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        arr = [] # array to keep track of the query count 
        
        # use the distance between 2 points formula where x1 and y1
        # is the points and x2 and y2 is where the radius is centered.
        # sqrt((x1 - x1)^2 + (y1 - y2)^2) gets us the distance between 
        # the two points. Check if its greater than or less than the 
        # radius. count to point if it is less than or equal otherwise 
        # it's not in the circle
        
        for query in queries:
            count = 0
            for point in points:
                if math.sqrt(abs(point[0] - query[0])**2 + abs(point[1] - query[1])**2) <= query[2]:
                    count += 1
            arr.append(count)
        
        return arr
                