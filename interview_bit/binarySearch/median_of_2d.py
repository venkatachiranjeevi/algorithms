__author__ = 'customfurnish'

class Solution:

    def findMedian(self, A):
        n = len(A)
        if n is 0:
            return 0
        m = []
        for x in A:
            m += x
        m.sort()
        n = len(m)
        if n%2 == 0:
            return (m[n/2] +m[(n-1)/2])/2
        else:
            return m[n/2]


print Solution().findMedian([[1,3,5],[2,6,9], [3,6,9]])