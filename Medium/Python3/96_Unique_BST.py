class Solution:
    def numTrees(self, n: int) -> int:
        # if we have 1 node we can only make 1 tree
        # if we have 0 node we can only make 1 tree
        # if we have any 2 nodes we can make 2 trees
        # if we have 3 nodes we can make 5 trees
        # NOTE it doesn't matter what the nodes are, with 3 nodes we can always make only 5 trees
        # Example: nodes, 1,2,3
        #
        #     1        1        2         3    3
        #      \        \      /  \      /    / 
        #       2        3    1    3    2    1
        #        \      /              /      \
        #         3    2              1        2
        #
        # given n nodes we have to consider than each n is a node for each combination
        
        # an array to keep track of the number of combinations
        # for 0 nodes that is 1 tree.
        # we can have 1 tree for every n values because every 1-n value can be a tree
        numTree = [1] * (n + 1)
        
        # we start at 2 because we already fill 0, 1 above intializing
        # this is the number of nodes to work with
        for nodes in range(2, n+1):
            total = 0 # this keeps track of the total i think?!?!
            # loop from 1 to nodes, this says that each node from that range can be root and we have nodes number of nodes
            for root in range(1, nodes +1):
                left = root - 1 # this gives us the left subtree, anything less than root is on the left
                right = nodes - root # this gives us the right subtree, anything more than root is on the right
                total += numTree[left] * numTree[right] # we multiply the left and right together to get the permutation
            numTree[nodes] = total # store the total in the number of unique trees based off the total
        
        # numTree is a look up table, consider nodes = 2,and root is 1-3
        # initial, root = 1
        # root = 1
        # left = 1-1, = 0, there is no left subtree for root = 1
        # right is 2 - 1, there is 1 node on the right
        # total = number of nodes on the left * nodes on right, which gives us nodes[1] = 1, total = 0 + 1
        #
        # root is 2
        # left = 2 - 1 = 1 node on the left
        # right is 2 - 2, = 0 no nodes on the right
        # total = 1 from previous plus, 1 * 1 which gives us 2
        # 2 nodes there are 2 unique trees
        #
        # consider nodes = 3 then the following, root 1-4
        # root is 3
        # total is 3 from above, because n 1 is 1 and n 2 is 2, 2 + 1 = 3
        # left = 3 - 1 = 2
        # right = 3 - 3 = 0
        # total = 3, then lookup[0] * lookup[2] = 2, 3 + 2 = 5
        # if n = 3 then the number of unique permutaions is 5
    
        return numTree[n] # return our calculation
    
    # This solution is O(n^2) time and O(n) space