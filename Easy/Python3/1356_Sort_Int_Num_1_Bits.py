from typing import List

# You are given an integer array arr. Sort the integers in the array in 
# ascending order by the number of 1's in their binary representation and in 
# case of two or more integers have the same number of 1's you have to sort them 
# in ascending order.

# Return the array after sorting it. 

# Example 1:

# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]

# Example 2:

# Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
# Output: [1,2,4,8,16,32,64,128,256,512,1024]
# Explantion: All integers have 1 bit in the binary representation, you should 
# just sort them in ascending order.

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        a = [] # store (x,y) tuple where x is the num 1s and y is the integer 
        
        # loop the array and count the 1s
        for x in arr:
            bit_p = 0 # bit position shift count
            count = 0 # count the 1s
            temp = x # temp so we can shift and retain x
            while bit_p != 32:
                count += temp & 1
                bit_p += 1
                temp = temp >> 1
            
            a.append((count, x)) # append the count and integer
        
        a.sort() # sort the array of tuples
        
        # swap and only keep the integer from the sorted values
        for idx in range(len(a)):
            a[idx] = a[idx][1] # swap and just keep the second val from the tuple
        
        return a