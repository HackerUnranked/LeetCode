from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # The horizontal distance between two points is
        # x1 - x1
        #
        # The vertical distance between two points is
        # y1 - y2
        #
        # if we combine these we get the max time visiting all points
        #
        # example a = [[1,2], [4,7]]
        #
        #
        # max horizontal distance is 3 where x1 = 1 and x2 = 3, 1 - 3 = 3
        # max verticle distance is 5 where x1 = 2 and x2 = 7, 7 - 2 = 5
        #
        # given the above, if we wanted to get from [1,2] to [4,7] we would
        # need to move horizontal 3 times and verticle 5 times which gives
        # us a total of 8 moves.
        # vertical [1,2] -> [1,3] -> [1,4] -> [1,5] -> [1,6] -> [1,7] # 5 moves vertical
        # 
        # horizontal [1,7] -> [2,7] -> [3,7] -> [4,7] # 3 moves
        #
        #
        # 3 + 5 = 8 moves max
        
        #
        # We can cheat by moving diagonal which lets us move verticle and horizontal
        # at the same time instead of going horizontal then veritcal as 2 moves.
        # In order to move diagonal we get the following:
        #
        #
        # diagonal [1,2] -> [2,3] -> [3,4] -> [4,5] # 3 moves
        #
        # vertical [4,5] -> [4,6] -> [4,7] # 2 moves
        #
        # 2 + 3 = 5 moves
        #
        # conclusion 5 moves = max(abs((x1 - x2), (y1 - y2))
        #
        # so the rule is in order to move from one point to the other
        # with minimum you need to move atleast m distance which is
        # the max(abs(x1 - x2), (y1 - y2))
        
        total = 0 # total distance
        
        # start at 1 so we can compare with previous
        for x in range(1, len(points)):
            total += max(abs(points[x - 1][0] - points[x][0]), abs(points[x - 1][1] - points[x][1]))
        
        return total