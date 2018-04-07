__author__ = 'customfurnish'

class Solution:

    def cpFact(self, A, B):
        res = []
        i = A
        res.append(2)
        res.append(1)
        while i > 0:
            if A%i is 0:
                if self.gcd(i, B) is 1:
                    return i
            i -= 1
        return 1

    def gcd(self, a, b):
        if (b == 0):
            return a
        else:
            return self.gcd(b, a%b)

    def lar(self, A, B):

        while(self.gcd(A, B) != 1):
            A = A/ self.gcd(A, B)
        return A
print Solution().lar(30, 12)