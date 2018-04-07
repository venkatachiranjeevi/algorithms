import sys

__author__ = 'venkat'

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        n = len(A)
        A.sort()
        min_val =A[0] ^ A[1]
        for x in range(2, n):
            min_val = min(min_val, A[x-1] ^ A[x])

        return min_val


print Solution().findMinXor([0,2,5,7])