# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).

 

# Example 1:

# Input: x = 123 Output: 321

# Example 2:

# Input: x = -123 Output: -321

# Example 3:

# Input: x = 120 Output: 21

 

# Constraints:

#     -231 <= x <= 231 - 1


class Solution:
    # NOTE: This solution is not valid because we cannot store a 64-bit integer
    def reverse(self, x: int) -> int:
        # The range of 32-bit signed integer is [-2^31, 2^31 - 1]
        INT32_MIN = -2147483648
        INT32_MAX = 2147483647

        # if x is negative 
        if x < 0:
            # reverse the string
            # example -123 -> 321-
            bw = str(x)[::-1].lstrip('0') # remove the leading zeros
            # remove the negative sign so it becomes 321
            bw = bw[:len(bw) -1]
            # convert the string to integer and get the negative value,
            # example: 321 - 321 * 2 = -321 
            num = int(bw) - int(bw) * 2
            # if the number is less than the minimum value of 32-bit signed integer
            # return 0
            if num < INT32_MIN:
                return 0
            # return the number
            return num
        # if x is 0 return 0
        elif x == 0:
            return 0
        # if x is positive
        else:
            # reverse the string
            a = int(str(x)[::-1])
            
            # if the number is greater than the maximum value of 32-bit signed integer
            if a > INT32_MAX:
                return 0
            return a # return the number
    
    def reverse2(self, x: int) -> int:
        INT32_MIN_STR = '2147483647'
        INT32_MAX_STR = '2147483648'

        # we are smaller than 0
        if x < 0:
            bw = str(x)[::-1].lstrip('0') # remove the leading zeros if there are any
            bw = bw[:len(bw) -1] # remove the negative sign
            # Bigger string means we are a bigger number
            if len(bw) > len(INT32_MIN_STR):
                return 0
            # if the length is the same, we need to compare the string
            elif len(bw) == len(INT32_MIN_STR):
                if bw > INT32_MIN_STR:
                    return 0
            # calculate the negative number
            num = 0 - int(bw)
            return num
        # return 0 because there is no reverse
        elif x == 0:
            return 0
        else:
            a = str(x)[::-1].lstrip('0') # reverse the string
            # if the number is bigger than the maximum value of 32-bit signed integer
            if len(a) > len(INT32_MAX_STR):
                return 0
            # if the length is the same, we need to compare the string
            elif len(a) == len(INT32_MAX_STR):
                if a > INT32_MAX_STR:
                    return 0
            return int(a)
