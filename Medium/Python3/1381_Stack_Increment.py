# Design a stack which supports the following operations.

# Implement the CustomStack class:

#     CustomStack(int maxSize) Initializes the object with maxSize which is the 
#     maximum number of elements in the stack or do nothing if the stack reached 
#     the maxSize.
#     
#     void push(int x) Adds x to the top of the stack if the stack hasn't 
#     reached the maxSize.
#     
#     int pop() Pops and returns the top of stack or -1 if the stack is empty.
#     void inc(int k, int val) Increments the bottom k elements of the stack by 
#     val. If there are less than k elements in the stack, just increment all 
#     the elements in the stack.

# Example 1:

# Input
# ["CustomStack","push","push","pop","push","push","push","increment",
# "increment","pop","pop","pop","pop"]
# 
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# 
# Output
# [null,null,null,2,null,null,null,null,null,103,202,201,-1]
# Explanation
# CustomStack customStack = new CustomStack(3); // Stack is Empty []
# customStack.push(1);                          // stack becomes [1]
# customStack.push(2);                          // stack becomes [1, 2]
# customStack.pop();                            // return 2 --> Return top of 
#                                                  the stack 2, stack becomes [1]
# customStack.push(2);                          // stack becomes [1, 2]
# customStack.push(3);                          // stack becomes [1, 2, 3]
# customStack.push(4);                          // stack still [1, 2, 3], Don't 
#                                                  add another elements as size 
#                                                  is 4
# customStack.increment(5, 100);                // stack becomes [101, 102, 103]
# customStack.increment(2, 100);                // stack becomes [201, 202, 103]
# customStack.pop();                            // return 103 --> Return top of 
#                                                  the stack 103, stack becomes 
#                                                  [201, 202]
# customStack.pop();                            // return 202 --> Return top of 
#                                                  the stack 102, stack becomes 
#                                                  [201]
# customStack.pop();                            // return 201 --> Return top of 
#                                                  the stack 101, stack becomes []
# customStack.pop();                            // return -1 --> Stack is empty 
#                                                  return -1.

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize # max size of stack
        self.stack = [] # stack initialization

    def push(self, x: int) -> None:
        if len(self.stack) != self.maxSize: # only add if we have room
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) != 0: # pop the top only if we have something in the stack
            return self.stack.pop()
        
        return -1 # return -1 the stack is empty

    def increment(self, k: int, val: int) -> None:
        idx = 0 # idx to traverse the stack
        
        # incrememnt the bottom of the stack by val
        while idx != len(self.stack) and k != 0:
            self.stack[idx] += val
            idx += 1
            k -= 1

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)