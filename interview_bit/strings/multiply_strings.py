__author__ = 'venkat'

class Solution():

    def multipler(self, number, n):
        l = len(number)
        count = 0
        res = 0
        while count < l:
            res *= 10
            res += int(number[count]) * n

            count += 1
        return res

    def multiply(self, A, B):
        l1 = len(A) -1
        l2 = len(B)
        res = []
        result = 0
        c = 0
        while l1 >=0:
            result += self.multipler(B, int(A[l1])) * (10 ** c)
            c += 1
            l1 -= 1
        return result

print Solution().multiply("99999", "99999")

# [899991,899991,899991,899991, 899991]