# Given two integers left and right, return the count of numbers in the 
# inclusive range [left, right] having a prime number of set bits in their 
# binary representation.

# Recall that the number of set bits an integer has is the number of 1's present 
# when written in binary.

#     For example, 21 written in binary is 10101, which has 3 set bits. 

# Example 1:

# Input: left = 6, right = 10
# Output: 4
# Explanation:
# 6  -> 110 (2 set bits, 2 is prime)
# 7  -> 111 (3 set bits, 3 is prime)
# 8  -> 1000 (1 set bit, 1 is not prime)
# 9  -> 1001 (2 set bits, 2 is prime)
# 10 -> 1010 (2 set bits, 2 is prime)
# 4 numbers have a prime number of set bits.

# Example 2:

# Input: left = 10, right = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# 5 numbers have a prime number of set bits.

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # we have a set of prime numbers
        # we stop at 13 because the biggest the number can
        # be is 10^6 which means at most we have 19 bits of 1's
        prime = {2, 3, 5, 7, 11, 13, 17, 19}
        total = 0 # keeps track of the total numbers with prime bits
        
        # loop the number via range and
        # count the bits of ones
        for num in range(left, right + 1):
            count = 0 # counts the 1's bits
            temp = num
            while temp != 0:
                # if the last digit is a zero then count it
                if temp & 1 == 1:
                    count += 1
                # shift left 1 so we can do the next number
                temp = temp >> 1
            # prime number of bits so incrememnt it
            if count in prime:
                total += 1
        
        return total