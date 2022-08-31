# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

# Example 1:

# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

# Example 2:

# Input: tiles = "AAABBC"
# Output: 188

# Example 3:

# Input: tiles = "V"
# Output: 1

class Solution:
    # note this is a permutations of repititions meaning order does matter
    # because based on the order of the characters the string is a different
    # sequence
    def numTilePossibilities(self, tiles: str) -> int:
        arr = [0] * 26 # counts the number of times a character appears
        
        # loop and put in each occurence of the character in a bucket
        for char in tiles:
            arr[ord(char) - 65] += 1
        
        def solve(freq):
            # if we don't have anymore available letters then we return
            if sum(freq) == 0:
                return 0
            
            ans = 0 # counts the number of sequences
            
            # loop each idx and see if we can take a letter
            for idx, letters in enumerate(freq):
                if letters != 0:
                    freq[idx] -= 1 # decrement the character because we are using it
                    ans += solve(freq) + 1 # call the solve function and add 1 for the sequence we already built
                    freq[idx] += 1 # add the letter back so we can use it again
            
            return ans
        
        return solve(arr)
                    