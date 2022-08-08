# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
 
# Example 1:

# Input: n = 5
# Output: 2
# Explanation: The square triples are (3,4,5) and (4,3,5).

# Example 2:

# Input: n = 10
# Output: 4
# Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

class Solution:
    def countTriples(self, n: int) -> int:
        
        # get the squares
        sqr = set(num**2 for num in range(1, n + 1))
        answer = 0
        
        # loop to get a^2
        for a in range(1, n+1):
            # loop to get b^2
            for b in range(a + 1, n + 1):
                # make sure we are not bigger than the max
                # this also helps us find c
                if a**2 + b ** 2 <= n ** 2:
                    # check if c is in the set
                    c = (a ** 2) + (b ** 2)
                    if c in sqr:
                        answer += 2
        return answer