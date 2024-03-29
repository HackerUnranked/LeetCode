'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit 
signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is 
       '-' or '+'. Read this character in if it is either. This determines if 
       the final result is negative or positive respectively. Assume the result 
       is positive if neither is present.
    3. Read in next the characters until the next non-digit character or the end
       of the input is reached. The rest of the string is ignored.
    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
       If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
       If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
       then clamp the integer so that it remains in the range. Specifically, 
       integers less than -231 should be clamped to -231, and integers greater 
       than 231 - 1 should be clamped to 231 - 1.
       Return the integer as the final result.

Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest 
    of the string after the digits.

 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the 
             current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

'''

class Solution:
    def myAtoi(self, s: str) -> int:
        my_num = []
        num_str = ""
        num_val = 0
        
        for x in s:
            # the character is letter or decimal
            if x.isalpha() or x == ".":
                break
            # if we saw a white space or the character is not a digit    
            elif x == " ":
                if len(my_num) != 0:
                    break      
            # this tells us if the number is positive or negative
            elif x == "-" or x == "+":
                # i dont have anything in the list so it can be the first item
                if len(my_num) == 0:
                    my_num.append(x)
                # we already have something in the list, this is the second time we saw the + or -
                else:
                    break
            # the number is a digit, add it to the list
            if x.isdigit():
                my_num.append(x)
            
        
        if len(my_num) > 1:
            # we just have a positive number
            if my_num[0].isdigit() or my_num[0] == "+":
                num_str = num_str.join(my_num)
                num_val = int(num_str)
                
                # handles biggest 32 bit number case
                if num_val > (2**31) -1:
                    num_val = (2**31) - 1
            else:
                num_str = num_str.join(my_num[1:])
                num_val -= int(num_str)
                
                if num_val < -2**31:
                    num_val = -2**31
                    
        # one item and it is a number
        elif len(my_num) == 1 and my_num[0].isdigit():
            num_val = int(my_num[0])
        
        
        return num_val