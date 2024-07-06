# You are given two integer arrays nums1 and nums2, sorted in non-decreasing 
# order, and two integers m and n, representing the number of elements 
# in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be 
# stored inside the array nums1. To accommodate this, nums1 has a length of 
# m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length
#  of n.

# Constraints:

#    nums1.length == m + n
#    nums2.length == n
#    0 <= m, n <= 200
#    1 <= m + n <= 200
#    -10^5 <= nums1[i], nums2[j] <= 10^5

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # This solution uses 3 pointers. we are looping the arrays backwards and putting the biggest number  towards
        # the end of the of array. p1 keeps track of where we are at for the big array half, p2 keeps track of where we are at for the
        # small array and end_idx helps us loop from beginning to end and insertion for the big array.

        # Initialize pointers
        p1 = m - 1 # start at end of the array but before the 0's start
        p2 = n - 1 # start at the end of the small array, this has no zeros it is literally the end
        end_idx = m + n - 1 # the end of the big array where the biggest number goes

        # loop from the end of the array on both of the array
        # for the big array we will start at idx m because that is the end of the first array. The rest of the
        # array is for storage
        while p1 >= 0 and p2 >= 0:
            # shift my last number to the end of the big array. it is the biggest number
            # this check organizes the nums1 area
            if nums1[p1] > nums2[p2]:
                nums1[end_idx] = nums1[p1]
                p1 -= 1 # move along the aray
            # number in nums1 is equal or smaller than nums2, This check organizes the num2 array
            else:
                # take the number from the small array and insert it where the end is
                nums1[end_idx] = nums2[p2]
                p2 -= 1 # move along the small array
            end_idx -= 1 # shift the end array

        # If there are remaining elements in nums2, copy them. We have this case if all or some of the numbers
        # in big array is bigger than the small array. This causes us to shift all the big to the left then we need
        # to insert the rest of the small array into the array.
        while p2 >= 0:
            nums1[end_idx] = nums2[p2]
            p2 -= 1
            end_idx -= 1