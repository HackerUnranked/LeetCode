
# You are given a phone number as a string number. number consists of digits, 
# spaces ' ', and/or dashes '-'.

# You would like to reformat the phone number in a certain manner. Firstly, 
# remove all spaces and dashes. Then, group the digits from left to right into 
# blocks of length 3 until there are 4 or fewer digits. The final digits are 
# then grouped as follows:

#     2 digits: A single block of length 2.
#     3 digits: A single block of length 3.
#     4 digits: Two blocks of length 2 each.

# The blocks are then joined by dashes. Notice that the reformatting process 
# should never produce any blocks of length 1 and produce at most two blocks of 
# length 2.

# Return the phone number after formatting.

# Example 1:

# Input: number = "1-23-45 6"
# Output: "123-456"
# Explanation: The digits are "123456".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st 
#         block is "123".
# Step 2: There are 3 digits remaining, so put them in a single block of length 
#         3. The 2nd block is "456".
# Joining the blocks gives "123-456".

# Example 2:

# Input: number = "123 4-567"
# Output: "123-45-67"
# Explanation: The digits are "1234567".
# Step 1: There are more than 4 digits, so group the next 3 digits. The 1st 
#         block is "123".
# Step 2: There are 4 digits left, so split them into two blocks of length 2. 
#         The blocks are "45" and "67".
# Joining the blocks gives "123-45-67".

# Example 3:

# Input: number = "123 4-5678"
# Output: "123-456-78"
# Explanation: The digits are "12345678".
# Step 1: The 1st block is "123".
# Step 2: The 2nd block is "456".
# Step 3: There are 2 digits left, so put them in a single block of length 2. 
#         The 3rd block is "78".
# Joining the blocks gives "123-456-78".

class Solution:
    def reformatNumber(self, number: str) -> str:
        num = 0
        idx = 0
        w = ""
        temp = ""
        
        # count how many numbers we have
        # so we know the string size and
        # get only the numbers from the string
        for x in number:
            if x != ' ' and x != '-':
                num += 1
                w += x
        
        while num != 0:
            # check if the string is at the end
            if num == 4:
                temp += w[idx] + w[idx + 1] + '-' + w[idx + 2] + w[idx + 3]
                return temp
            if num == 3:
                temp += w[idx] + w[idx + 1] + w[idx + 2]
                return temp
            if num == 2:
                temp += w[idx] + w[idx + 1]
                return temp
            
            temp += w[idx] + w[idx + 1] + w[idx + 2] + '-'
            num -= 3 # subtract how many we took
            idx += 3 # add the idx we are at
        