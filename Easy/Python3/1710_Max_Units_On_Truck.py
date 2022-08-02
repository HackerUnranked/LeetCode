from typing import List

# You are assigned to put some amount of boxes onto one truck. You are given a 
# 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

#   numberOfBoxesi is the number of boxes of type i.
#   numberOfUnitsPerBoxi is the number of units in each box of the type i.

# You are also given an integer truckSize, which is the maximum number of boxes 
# that can be put on the truck. You can choose any boxes to put on the truck as 
# long as the number of boxes does not exceed truckSize.

# Return the maximum total number of units that can be put on the truck. 

# Example 1:

# Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
# Output: 8
# Explanation: There are:
# - 1 box of the first type that contains 3 units.
# - 2 boxes of the second type that contain 2 units each.
# - 3 boxes of the third type that contain 1 unit each.
# You can take all the boxes of the first and second types, and one box of the 
# third type.
# 
# The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

# Example 2:

# Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
# Output: 91

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        bucket = [0] * 1000 # count the occurence, idx will indicate the units per box and the count indicates how many boxes i have
        
        # truckSize is the max number of boxes that i can have
        # box[x, y] where x is the number of boxes and y is the number of units per box
        #
        # i need to return the max number of units i can but in the truck given the number
        # of boxes
        
        # count the occurence of the boxes
        for box,idx in boxTypes:
            # count the number of boxes per unit
            bucket[idx -1] += box
        
        count = truckSize # counts how many boxes we have
        total = 0 # counts the total num units
        
        # loop list backwards to grab the greatest num units first
        
        for x in range(len(bucket) - 1, -1, -1):
            if count == bucket[x]:
                total += ((x + 1) * bucket[x]) # calculate the total
                count = 0 # set count to zero because we took everything
            # take what we need and leave
            elif count < bucket[x]:
                total += ((x + 1) * count) # take only what we need
                count = 0
            # there is not enough take it all 
            else:
                total += ((x + 1) * bucket[x])
                count -= bucket[x] # substract the difference
            
            # we took all the boxes we needed
            if count == 0:
                break
            
        return total