from typing import List

# You are given an array target and an integer n.

# In each iteration, you will read a number from list = [1, 2, 3, ..., n].

# Build the target array using the following operations:

#     "Push": Reads a new element from the beginning list, and pushes it in the 
#      array.
#
#     "Pop": Deletes the last element of the array.
#     If the target array is already built, stop reading more elements.

# Return a list of the operations needed to build target. The test cases are 
# generated so that the answer is unique. 

# Example 1:

# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: 
# Read number 1 and automatically push in the array -> [1]
# Read number 2 and automatically push in the array then Pop it -> [1]
# Read number 3 and automatically push in the array -> [1,3]

# Example 2:

# Input: target = [1,2,3], n = 3
# Output: ["Push","Push","Push"]

# Example 3:

# Input: target = [1,2], n = 4
# Output: ["Push","Push"]
# Explanation: You only need to read the first 2 numbers and stop.

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        prev = 1 # keeps track of number we are at
        a = [] # the array to return
        idx = 0 # idx of the array
        
        # loop while the index is less than the length of the list
        while idx < len(target):
            # push the number the pop if we are less
            # note we cannot pop consecutively so this means
            # after every push we have to pop if we are smaller
            # than the target value
            if prev < target[idx]:
                a.append('Push')
                a.append('Pop')
            else:
                a.append('Push') # add the item to the list we are equal
                idx += 1 # move the idx over one
                
            prev += 1 # incrememnt the count
        
        return a

    # similar to the solution above except O(n^2) since we are
    # appending the push and pop using the difference of the
    # previous idx instead of loop the with incremental n + 1 per
    # iteration 
    def buildArray_2(self, target: List[int], n: int) -> List[str]:
        prev = 1 # keeps track of number we are at
        a = [] # the array to return
        idx = 0 # idx of the array
        
        # loop while the index is less than the length of the list
        while idx < len(target):
            # push the number the pop if we are less
            # note we cannot pop consecutively so this means
            # after every push we have to pop if we are smaller
            # than the target value
            if prev < target[idx]:
                # special case if the list is empty we need to
                # push until we reach the targeted number
                if a == []:
                    for x in range(target[idx] - prev):
                        a.append("Push")
                        a.append("Pop")
                # if the list isn't empty we just push and pop from the numbers
                # in between, this means we don't include the last number
                else:
                    for x in range((target[idx] - prev) - 1):
                        a.append("Push")
                        a.append("Pop")
            
            a.append('Push')
                
            prev = target[idx]
            idx += 1
        
        return a