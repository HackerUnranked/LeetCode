
# Design a stack-like data structure to:
#  1. Push elements to the stack
#  2. Pop the most frequent element from the stack.
#  3. On a tie Pop the closest element to the top

# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

 

# Example 1:

# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
#Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]

# Explanation
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, 5 is most freq. The stack becomes [5,7,5,7,4].
# freqStack.pop();   // return 7, 5 and 7 is most freq, but 7 is closest to top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is most frequent. The stack becomes [5,7,4].
# freqStack.pop();   // return 4, as 4,5 7 is the most frequent, but 4 is closest to top. The stack becomes [5,7].

class FreqStack:

    def __init__(self):
        self.the_list = []
        self.dic = {}

    def push(self, val: int) -> None:
        
        # add to list at the end
        self.the_list.append(val)
        
        # count the occurence
        if val not in self.dic:
            self.dic[val] = 1
        else:
            self.dic[val] += 1
    
    def pop(self) -> int:
        
        # there is nothing in the list
        if self.the_list == []:
            return None
        
        # get the max value of appearance, this is O(n)
        count = max(self.dic.values())
        
        # there is only 1 thing in the list
        if len(self.the_list) == 1:
            to_return = self.the_list[0]
            self.the_list = []
            return to_return
        
        found = False
        x = len(self.the_list) - 1

        # loop the list backwards and find the key that matches the value then remove it
        while x > 0:
            if self.dic[self.the_list[x]] == count:
                found = True
                break
            x = x - 1
        
        # we found it, delete it and return
        if found == True:
            print("returning ", self.the_list[x])
            return_me = self.the_list[x]
            self.dic[self.the_list[x]] -= 1
            del self.the_list[x]
         
            return return_me