# Implement a first in first out (FIFO) queue using only two stacks. 
# The implemented queue should support all the functions of a normal queue 
# (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may 
# simulate a stack using a list or deque (double-ended queue) as long as you use
# only a stack's standard operations.
 
# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    # add items to the stack
    def push(self, x: int) -> None:
        self.stack1.append(x)
        print(self.stack1)
        print(self.stack2)

    def pop(self) -> int:
        # remove from this first because it has the elements that came first
        if len(self.stack2)!= 0:
            return self.stack2.pop()
        # the second list is empty we need to push all of the items in the first list
        # into the second one
        elif len(self.stack1):
            for x in reversed(self.stack1):
                self.stack2.append(x)
            # empty the first stack because we pushed it all into the second
            self.stack1 = []
        
        return self.stack2.pop()

    def peek(self) -> int:
        # we have something in the second list, return the item because it is
        # more recent than the first list
        if len(self.stack2) != 0:
            return self.stack2[-1]
        else:
            return self.stack1[0]

    def empty(self) -> bool:
        if len(self.stack1) or len(self.stack2):
            return False
        return True