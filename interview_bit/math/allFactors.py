import math

__author__ = 'venkat'


class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        if A == 1:
            return [A]
        ret = [1,A]
        st = int(A**0.5)
        for i in range(2,st):
            if A%i == 0:
                ret.append(i)
                ret.append(A/i)
        if A%st == 0:
            ret.append(st)
            if st**2 != A:
                ret.append(A/st)
        ret.sort()
        return ret



print Solution().allFactors(6)