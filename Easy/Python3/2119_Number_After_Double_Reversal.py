# Reversing an integer means to reverse all its digits.

#     For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the 
#     leading zeros are not retained.

# Given an integer num, reverse num to get reversed1, then reverse reversed1 to 
# get reversed2. Return true if reversed2 equals num. Otherwise return false. 

# Example 1:

# Input: num = 526
# Output: true
# Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals 
# num.

# Example 2:

# Input: num = 1800
# Output: false
# Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not 
# equal num.

# Example 3:

# Input: num = 0
# Output: true
# Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num) # turn the int into a string
        s = int(s[::-1]) # reverse and turn the string back into an int
        
        # compare if the num matches the int after we reverse the int
        # by changing it back into string then int
        if num != int(str(s)[::-1]):
            return False
        
        return True
    
    # better solution withouth using int() and str()
    def isSameAfterReversals_2(self, num: int) -> bool:
        # if num is zero the return True otherwise
        # check if num has leading zeros by moding
        # by 10. Anyhting with a leading zero will
        # not equal after reversing.
        #
        # example n = 1800, 2 leading zero
        #
        # reverse 0081, 81
        #
        # reverse again and 18 does not equal 1800
        return num == 0 or num % 10 