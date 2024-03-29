from typing import List

# Write a function that reverses a string. The input string is given as an array
# of characters char[]. Do not allocate extra space for another array, you must 
# do this by modifying the input array in-place with O(1) extra memory. You may
# assume all the characters consist of printable ascii characters.

# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = 0
        left = len(s) -1
         
        while right < left:
            right_holder = s[right]
            s[right] = s[left]
            s[left] = right_holder
            right += 1
            left -= 1
        
        return s