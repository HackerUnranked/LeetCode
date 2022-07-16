from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        count_me = 0
        
        # loop through the words
        for word in words:
            dic = {}
            
            # create a dictionary to count the letters available to use
            for letters in chars:
                if letters not in dic:
                    dic[letters] = 1
                else:
                    dic[letters] += 1
            
            # loop through the letters of the word
            
            found = True
            for letter in word:
                # if the letter is in the dictionary, see if we can take
                if letter in dic:
                    if dic[letter] != 0:
                        dic[letter] -= 1
                    # there are no more letters
                    else:
                        found = False
                        break
                # we didn't have the letter 
                else:
                    found = False
                    break
            
            if found == True:
                count_me += len(word)
        
        return count_me
    
    # this is the solution using buckets instead of a dictionary
    def countCharacters_array(self, words: List[str], chars: str) -> int:
        
        count = 0
        
        for word in words:
            bucket = [0] * 26
            
            # count the letters in the words
            for letters in word:
                bucket[122 - ord(letters)] += 1
            
            # subtract the chars
            for letters in chars:
                # the letter is a match so we subtract
                if bucket[122 - ord(letters)] > 0:
                    bucket[122 - ord(letters)] -= 1
            
            zero = True
            
            # if a string is all 0 it means we can see create the word so add the count
            for num in bucket:
                if num != 0:
                    zero = False
                    break
            
            if zero == True:
                count += len(word)
        
        return count