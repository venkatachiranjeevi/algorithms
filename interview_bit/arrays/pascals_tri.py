__author__ = 'venkat'


class Solution:

    def generate(self, A):
        res = []
        for x in range(A):
            res.append(self.getRow(x))
        return res

    def getRow(self, A):
        A +=1
        res = []
        i = 1
        C = 1
        res.append(C)
        while( i< A):
            C = (C * (A-i))/i
            res.append(C)
            i +=1
        return res

print Solution().generate(5)