__author__ = 'venkat'

class Solution:
    def rotate(self, A):
        n = len(A)
        if n < 2:
            return A
        for i in range((n/2)):
            for j in range(i,(n-i-1)):
                temp =  A[i][j]
                A[i][j] = A[n-j-1][i]
                A[n-j-1][i] = A[n-i-1][n-j-1]
                A[n-i-1][n-j-1] = A[j][n-i-1]
                A[j][n-i-1] = temp
        return A

a = [[1, 2, 3,4],
  [5, 6,7,8],
  [9,10,11,12],
  [13,14,15,16]]

b = [[6,7], [10,11]]

print Solution().rotate(a)