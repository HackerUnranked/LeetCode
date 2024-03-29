# You are given a string s consisting only of letters 'a' and 'b'. In a single 
# step you can remove one palindromic subsequence from s.

# Return the minimum number of steps to make the given string empty.

# A string is a subsequence of a given string if it is generated by deleting 
# some characters of a given string without changing its order. Note that a 
# subsequence does not necessarily need to be contiguous.

# A string is called palindrome if is one that reads the same backward as well 
# as forward. 

# Example 1:

# Input: s = "ababa"
# Output: 1
# Explanation: s is already a palindrome, so its entirety can be removed in a 
# single step.

# Example 2:

# Input: s = "abb"
# Output: 2
# Explanation: "abb" -> "bb" -> "". 
# Remove palindromic subsequence "a" then "bb".

# Example 3:

# Input: s = "baabb"
# Output: 2
# Explanation: "baabb" -> "b" -> "". 
# Remove palindromic subsequence "baab" then "b".

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # NOTE: special cases:
        #
        # 1. the string is size 1, return 1
        #
        # 2. The string is already a palindrome, return 1
        #    because we can remove it in one operation
        #
        # 3. return 2 BECAUSE, a and b by themselves are
        #    palindrome and we can remove a palindrome
        #    subsequence in one step, remove all a's then
        #    remove all b's, this equals 2 steps
        #
        #
        # subsequnce is given by deleting some characters without
        # changing it's order. doesn't need to be contigous.
        #
        # example: string abaaaa
        # we can remove all the a's in any order as 1 step because
        # a is a palindrome. Afterwards we remove b to get 2 steps
        
        l = len(s) - 1
        r = 0
        
        # iterative way to check if string is palindrome using
        # 2 pointers approach
        while r < l:
            if s[r] == s[l]:
                l -= 1
                r += 1
            else:
                break
        
        if l <= r:
            return 1
        return 2