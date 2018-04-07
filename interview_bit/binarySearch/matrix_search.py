__author__ = 'customfurnish'

class Solution:

    def searchMatrix(self, A, B):
        m = len(A)
        # if m is 0:
        #     return 0
        n = len(A[0])
        # if n is 0:
        #     return 0
        i =0
        j =n-1

        while i < m and j >= 0:
            if A[i][j] == B:
                return 1
            if A[i][j] > B:
                j -= 1
            else:
                i += 1

        return 0


A = [
  [22, 32, 67]
]
print Solution().searchMatrix(A,93)