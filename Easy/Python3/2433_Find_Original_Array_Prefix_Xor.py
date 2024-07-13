# You are given an integer array pref of size n. Find and return the array arr 
# of size n that satisfies:
# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

# Note that ^ denotes the bitwise-xor operation.

# It can be proven that the answer is unique. 

# Example 1:

# Input: pref = [5,2,0,3,1]
# Output: [5,7,2,3,2]
# Explanation: From the array [5,7,2,3,2] we have the following:
# - pref[0] = 5.
# - pref[1] = 5 ^ 7 = 2.
# - pref[2] = 5 ^ 7 ^ 2 = 0.
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

# Example 2:

# Input: pref = [13]
# Output: [13]
# Explanation: We have pref[0] = arr[0] = 13. 

# Constraints:

#    1 <= pref.length <= 105
#    0 <= pref[i] <= 106
from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # We are given the cumulative xor of the array
        # We need to find the original array such that pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
        #

        # 1. Understanding XOR**: The XOR (exclusive OR) operation has a unique
        #    property: if you XOR any number with itself, the result is 0. Also,
        #    if you XOR any number with 0, you get the number back. This 
        #    property is crucial for understanding how the original value is 
        #    retrieved.

        # 2. Prefix XOR: The prefix XOR at any index x in an array is the result
        #    of XORing all the elements from the start of the array up to index 
        #    For example, if the array is `[a, b, c]`, the prefix XOR at index 2
        #    would be `a ^ b ^ c`.

        # 3. Retrieving the Original Value: Let's say pref[x] holds the prefix 
        #    XOR up to index x,x. If you have the prefix XOR up to index x-1 
        #    (let's call this prev), you can retrieve the original value at 
        #    index x by XORing pref[x] with prev. This works because 
        #    pref[x] is a ^ b ^ ... ^ previousValue ^ originalValue, and prev is
        #    a ^ b ^ ... ^ previousValue. XORing these two cancels out 
        #    everything up to previousValue, leaving you with originalValue.

        # Here's a simplified example:

        # Original array: [1, 2, 3]
        # Prefix XOR array: [1, 3, 0] (where 1 is 1, 3 is 1^2, and 0 is 1^2^3)
        # To find the original value at index 2 (which is 3), you take the 
        # prefix XOR at index 2 (0) and XOR it with the prefix XOR at index 1 (3). 
        # The result is 0 ^ 3 = 3, which is the original value.
        # In summary, the line pref[x] = prev ^ pref[x] retrieves the original 
        # value at index x by XORing the prefix XOR at index x with the prefix 
        # XOR up to index x-1. This leverages the XOR operation's properties to 
        # "cancel out" all the previous values, leaving only the original value 
        #  at index x.

       # if we xor the pref[x] with the previous value we get the original value
       # at that index. This works because of the properties of XOR. If c = a ^ b
       # and we need to find a, we can do a = c ^ b. Example: if a = 5, b = 7,
       # and we xor them we get c = 2. If we need to find a, we can do a = 2 ^ 7 = 5
       # or b = 2 ^ 5 = 7. This is because XOR is reversible.

       # Say the pref array is [5, 7, 2, 3, 2]. To find the original array, we can
       # do the following: to get 5 we use 5 ^ 0 because 5 ^ 0 = 5. Then we do 7 ^ 5
       # to get 2. Then we do 2 ^ 7 to get 5. Then we do 2 ^ 3 to get 1. Finally
       # we do 3 ^ 2 to get 2. This is the original array is [5,2,5,1,1]
        prev = 0
        for x in range(len(pref)):
            temp = pref[x] # Get the current value
            pref[x] = prev ^ pref[x] # Get the original value
            prev = temp
        return pref