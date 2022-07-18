# You are given a positive integer num consisting only of digits 6 and 9. Return 
# the maximum number you can get by changing at most one digit 
# (6 becomes 9, and 9 becomes 6). 

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.

# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.

# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.

class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        
        # this is 6xxx add 3k and return
        if num // 1000 == 6 :
            return num + 3000
        else:
            temp = num % 1000 # get the hundreds place val
        
        # check if it is a 6 and return by adding 300 to change it to a 9
        if temp // 100 == 6:
            return num + 300
        else:
            temp = temp % 100 # get the 10s place
        
        # check if the tens place is a 6 and add 30 to change it to 90 
        if temp // 10 == 6:
            return num + 30
        else:
            temp = temp % 10 # get the ones place
        
        # if i am a six return and add 3 otherwise just return num
        if temp < 9:
            return num + 3
        
        return num