__author__ = 'venkat'

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        left = 0
        right = len(A) -1
        qty = 0
        while left < right:
            qty = max(qty, ((right-left) * min(A[left], A[right])))
            if A[left] < A[right]:
                left += 1
            else:
                right -=1

        return qty

print Solution().maxArea([1,5,4,3])


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        n = len(A)
        if n == 0:
            return 0
        i = 0
        j = n - 1
        ret = 0
        while i < j:
            ret = max(ret, (j-i)*min(A[i],A[j]))
            if A[i] < A[j]:
                i += 1
            else:
                j -= 1
        return ret