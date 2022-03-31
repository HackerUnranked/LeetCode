# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        val_mapped = set()
        pairs = {}
        count = 0
        split_me = s.split()
        
        # the number of words must match the length of the patter string
        # because each pattern is a key to a word
        # example:
        # pattern: abba
        # string: "dog cat cat dog"
        # let a is a key for dog and b is a key for cat
        
        if len(pattern) != len(split_me):
            return False
        
        for x in pattern:
            # the key has not been mapped to a word yet
            if x not in pairs:
                # check if the word has been mapped already
                if split_me[count] not in val_mapped:
                    val_mapped.add(split_me[count])
                    pairs[x] = split_me[count]
                # the word has already been mapped, this means the key is new and mapped
                # to an old word therfore we need to return false because each key is mapped
                # only to a single word
                # example: patter = "abbc", string = "dog cat cat dog"
                else:
                    return False
            # the key is already mapped to a word, check if the mapped word matches what the key has in the dictionary
            else:
                if pairs[x] != split_me[count]:
                    return False
            count += 1
                
        return True
            