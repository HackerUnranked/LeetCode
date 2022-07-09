class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] # note this holds tuple pairs (a, b) where a is the val
                        # and b is the min value in the list

    def push(self, val: int) -> None:
        small = val
        
        # check if there is a stack and if so grab the
        # min
        if self.stack:
            # grab the min
            small = self.stack[-1][1]
            
            # check if the previous small is greater than the current
            # if it is then we have a new small 
            
            if small > val:
                small =  val
        # add the pair to the list
        self.stack.append((val, small))

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()