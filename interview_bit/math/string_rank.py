__author__ = 'customfurnish'


class Solution:

    def findRank(self, A):
        l = len(A)
        if l is 0:
            return 0

        mul = self.fact(l)
        count = 1
        for x in range(l):
            mul /= l - x
            count += self.findLowet(A[x:], A[x]) * mul
        if count > (2**31):
            return count % 1000003
        return count

    def fact(self, num):
        return 1 if num<=1 else num* self.fact(num-1)

    def findLowet(self, S, i):
        count =0
        for x in S:
            if x < i:
                count += 1
        return count

print Solution().findRank("venkat")