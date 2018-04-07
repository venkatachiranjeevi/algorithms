
__author__ = 'venkat'
import sys
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        if n < 2:
            return []
        res = [0] * n
        i =0
        for x in A:
            if x is "1":
                res[i] = -1
            else:
                res[i] = 1
            i += 1
        final = 0
        best = 0
        l = 0
        i = 0
        temp = [-32, 32]
        while i < n:
            if best+ res[i] < 0:
                l = i+1
                best = 0
            else:
                best += res[i]
            if best > final:
                final = best
                temp[0] = l
                temp[1] = i
            i += 1

        if temp[0] == -sys.maxint:
            return []
        return [temp[0]+1, temp[1]+1]


print Solution().flip("001")