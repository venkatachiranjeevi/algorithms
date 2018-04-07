__author__ = 'venkat'

class Solution():

    def power(self, A):
        res = 1
        c = 0
        while res < int(A):
            res = 2 ** c
            temp = str(res)
            if temp == A:
                return 1
            c += 1
        return 0

    def pow(self, A):
        if A == 0:
            return 0
        while A !=1:
            if A%2 != 0:
                return 0
            A /= 2
        return 1

print Solution().power("127")
# print Solution().pow(128)