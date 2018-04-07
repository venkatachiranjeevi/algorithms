__author__ = 'venkat'

class Solution:
    def find_duplicate(self,A):
        n = max(A)
        m = len(A)
        li = [0] *(n+1)
        for i in range(0,m):
            li[A[i]] += 1
        i = 0
        while i< n+1:
            if li[i]> 1:
                return i
            i +=1

        return -1

print Solution().find_duplicate([ 1, 1 ])