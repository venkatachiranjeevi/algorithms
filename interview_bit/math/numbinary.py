__author__ = 'venkat'


class Solution:

    def findDigitsInBinary(self, A):
        res = ""

        while A is not 0:
            res += str(A%2)
            A /=2

        res = res[::-1]
        return res

print Solution().findDigitsInBinary(0)