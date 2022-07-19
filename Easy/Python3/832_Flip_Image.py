from typing import List

# Given an n x n binary matrix image, flip the image horizontally, then invert 
# it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.

#     For example, flipping [1,1,0] horizontally results in [0,1,1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

#     For example, inverting [0,1,1] results in [1,0,0]. 

# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

# Example 2:

# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for idx in range(len(image)):
            rev = image[idx] # get the row
            first = 0 # right half
            second = len(rev) - 1 # left half
            
            # reverse the list
            while first < second:
                temp = rev[first]
                rev[first] = rev[second]
                rev[second] = temp
                first += 1
                second -= 1
            
            # replace 1 with 0 and 0 with 1
            for val in range(len(rev)):
                if rev[val] == 1:
                    rev[val] = 0
                else:
                    rev[val] = 1
            
            # set the image
            image[idx] = rev
        
        return image