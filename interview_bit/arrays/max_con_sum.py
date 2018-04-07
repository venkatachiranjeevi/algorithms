__author__ = 'venkat'


a = [-1871, -23]

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        if n is 0:
            return 0
        if n is 1:
            return A[0]
        max_sum = A[0]

        temp = 0
        for x in A:
            temp += x
            if temp < x:
                temp = x
            if max_sum < temp:
                max_sum = temp

        return max_sum


print Solution().maxSubArray(a)