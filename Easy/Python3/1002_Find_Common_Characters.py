from typing import List

# Given a string array words, return an array of all characters that show up in 
# all strings within the words (including duplicates). You may return the answer 
# in any order.

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        arr1 = [0] * 26
        arr2 = [0] * 26
        k = 0
        
        # count the occurence
        for letter in A[0]:
            arr1[ord(letter) - 97] += 1
        
        # loop each word and reset the array after capturing the ones
        # that appear in both array
        for word in A[1:]:
            if k % 2 == 0:
                for letter in word:
                    # if they have the same letter then add it to the second
                    # array and substract from the first if we can take it
                    if arr1[ord(letter) - 97]:
                        arr2[ord(letter) - 97] += 1
                        arr1[ord(letter) - 97] -= 1
                arr1 = [0] * 26 # reset the first array because we took all the letters we could from it
            # we do the same for the above except this case handles switching from arr2 back to arr1 because
            # we need to compare the new words with arr2 since we reseted arr1
            else:
                for letter in word:
                    if arr2[ord(letter) - 97]:
                        arr1[ord(letter) - 97] += 1
                        arr2[ord(letter) - 97] -= 1
                arr2 = [0] * 26
                
            k += 1
        
        if k % 2 == 0:
            for l, cnt in enumerate(arr1):
                if cnt != 0:
                      result += chr(l + 97) * cnt 
        else:
            for l, cnt in enumerate(arr2):
                if cnt != 0:
                      result += chr(l + 97) * cnt 
                        
        return result