import sys

__author__ = 'venkat'
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        n = len(A)
        if n is 0:
            return 0
        res = 0
        max1 = max2 = -sys.maxint
        min1 = min2 =  sys.maxint
        for i in range(n):
            max1 = max(max1, A[i]+i)
            max2 = max(max2, A[i]-i)
            min1 = min(min1, A[i]+i)
            min2 = min(min2, A[i]-i)

        res = max(res, max2-min2)
        return max(res, max1-min1)
print Solution().maxArr([1 ,3,-1])