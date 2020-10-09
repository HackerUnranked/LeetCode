# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 2^31.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y  # this leaves us with the bits that are different
        count = 0
        for _ in range(32): # 32bit number
            count += xor & 1 # count if it's a one
            xor = xor >> 1 # shift left to keep counting
        return count