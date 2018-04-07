__author__ = 'venkat'

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res = A[0]
        for num in range(1, len(A)):
            res = res ^ A[num]

        return res

print Solution().singleNumber([1,2,2,3,3,4,4])