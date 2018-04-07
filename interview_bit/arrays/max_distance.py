__author__ = 'venkat'

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        Lmin =[0] *n
        Rmax = [0] * n
        Lmin[0] = A[0]
        Rmax[n-1] = A[n-1]
        for i in range(1, n):
            Lmin[i] = min([Lmin[i-1], A[i]])

        j = n-2
        while j >= 0:
            Rmax[j] = max([Rmax[j+1], A[j]])
            j -= 1

        i =0
        j =0
        max_diff = 0
        while i < n and j < n:
            if Lmin[i] <= Rmax[j]:
                max_diff = max(max_diff, j-i)
                j = j+1
            else:
                i = i+1

        return max_diff

a= [ 100, 100, 100, 100, 100 ]
print Solution().maximumGap(a)