from typing import List

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city. 

# Example 1:

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

# Example 2:

# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".

# Example 3:

# Input: paths = [["A","Z"]]
# Output: "Z"

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        unique = set()
        
        # add all the paths to the set
        for cities in paths:
            unique.add(cities[0])
        
        # loop the paths again and the destination that isn't
        # in the set doesn't have an outgoing path because it 
        # was not included in the set aka it wasn't an outgoing path
        for cities in paths:
            if cities[1] not in unique:
                return cities[1]