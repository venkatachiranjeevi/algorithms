__author__ = 'venkat'

class Solution:
    def diagonal(self, a):
        n = len(a)
        if n < 2 :
            return a
        res = []
        for i in range((2*(n-1))+1):
            temp = []
            for j in range(i+1):
                if j < n and i-j< n:
                    temp.append(a[j][i-j])
            res.append(temp)
        return res
# a = [[1,2,3],[4,5,6],[7,8,9]]
a = [[1,2],[3,4]]
print Solution().diagonal(a)