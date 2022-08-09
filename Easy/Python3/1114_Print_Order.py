import time

# Suppose we have a class:

# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }

# The same instance of Foo will be passed to three different threads. Thread A 
# will call first(), thread B will call second(), and thread C will call third(). 
# Design a mechanism and modify the program to ensure that second() is executed 
# after first(), and third() is executed after second().

# Note:

# We do not know how the threads will be scheduled in the operating system, even 
# though the numbers in the input seem to imply the ordering. The input format 
# you see is mainly to ensure our tests' comprehensiveness.

# Example 1:

# Input: nums = [1,2,3]
# Output: "firstsecondthird"
# Explanation: There are three threads being fired asynchronously. The input 
# [1,2,3] means thread A calls first(), thread B calls second(), and thread C 
# calls third(). "firstsecondthird" is the correct output.

# Example 2:

# Input: nums = [1,3,2]
# Output: "firstsecondthird"
# Explanation: The input [1,3,2] means thread A calls first(), thread B calls 
# third(), and thread C calls second(). "firstsecondthird" is the correct output.

class Foo:
    def __init__(self):
        self.a = [False]*2 # flags to let us know when one of the thread is finished

    def first(self, printFirst) -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.a[0] = True # we called the first one


    def second(self, printSecond) -> None:
        # loop and wait until the first one has been called
        while self.a[0] != True:
            time.sleep(0.005) # using sleep because it's more effecient
            
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.a[1] = True # set flag second has been called

    def third(self, printThird) -> None:
        # loop and wait until the second one has been called
        while self.a[1] != True:
            time.sleep(0.005) # using sleep because it's more effecient
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        # reset the flags
        self.a[0] = False
        self.a[1] = False