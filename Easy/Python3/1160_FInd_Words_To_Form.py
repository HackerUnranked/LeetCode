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
                