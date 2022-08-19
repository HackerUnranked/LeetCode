# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

#     MyHashMap() initializes the object with an empty map.
#
#     void put(int key, int value) inserts a (key, value) pair into the HashMap. 
#     If the key already exists in the map, update the corresponding value.
#     
#     int get(int key) returns the value to which the specified key is mapped, 
#     or -1 if this map contains no mapping for the key.
#     
#     void remove(key) removes the key and its corresponding value if the map 
#     contains the mapping for the key. 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], 
#                         [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the 
#                                                        existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

class TreeNode:
    def __init__(self, val=0, key=0, left=None, right=None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right

# Using TreeMap implementation
class MyTreeMap:

    def __init__(self):
        self.root = None

    def put(self, key: int, value: int) -> None:
        # add the key pair value into the TreeMap
        def helper(some_root, the_key, the_val):
            # create the node and map the key, val pair
            if some_root == None:
                some_root = TreeNode(the_val, the_key)
            # the key is smaller, go left
            elif some_root.key > the_key:
                some_root.left = helper(some_root.left, the_key, the_val)
            # the key is bigger go right
            elif some_root.key < the_key:
                some_root.right = helper(some_root.right, the_key, the_val)
            # we found the key, update the value
            else:
                some_root.val = the_val
            
            return some_root
        
        self.root = helper(self.root, key, value)
        
    
    def get(self, key: int) -> int:
        
        def helper(r, k):
            num = 0
            
            # we didn't find the key, return -1
            if r == None:
                num = -1
            elif k < r.key:
                num = helper(r.left, k)
            elif k > r.key:
                num = helper(r.right, k)
            else:
                num = r.val
                
            return num
        
        return helper(self.root, key)
    
    def remove(self, key: int) -> None:
        def findInorder(root):
            # find the inorder successor
            while root and root.left != None:
                root = root.left
                
            return root
        
        def delete(root,key):
            if root == None:
                return root
            if root.key > key:
                root.left = delete(root.left, key)
            elif root.key < key:
                root.right = delete(root.right, key)
            # we found the key
            else:
                # the key doesn't have any children, set it to null
                # and return
                if root.left == root.right == None:
                    return None
                # we don't have a left so we can just point to
                # our right and return to remove the node
                elif not root.left:
                    return root.right
                # similar to above except we don't have a right
                elif not root.right:
                    return root.left
                # we have a left and right we need to find the inorder successor
                else:
                    # find the inorder successor which is right then all the way left
                    lroot = findInorder(root.right)
                    root.key, root.val = lroot.key, lroot.val # map the new key, val pair
                    root.right = delete(root.right, lroot.key) # delete the inorder successor
                    
            return root
            
        self.root = delete(self.root, key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# bucket map implementation
class MyBucketMap:

    def __init__(self):
        self.bucket = [-1] * ((10**6) + 1) # create a bucket where we map the key to an index

    def put(self, key: int, value: int) -> None:
        self.bucket[key] = value
        

    def get(self, key: int) -> int:
        return self.bucket[key]

    def remove(self, key: int) -> None:
        self.bucket[key] = -1