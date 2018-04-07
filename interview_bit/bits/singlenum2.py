__author__ = 'venkat'

class Solution:

    def singleNumber(self, A):
        res = 0
        for x in range(31):
            sum = 0
            temp = 1 << x
            for j in range(len(A)):
                if A[j] & temp:
                    sum += 1

            if sum %3:
                res |= temp

        return res


print Solution().singleNumber([1,2,3,1,2,3,1,2,3])