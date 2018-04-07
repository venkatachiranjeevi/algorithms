__author__ = 'venkat'


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        n = len(A)
        for i in range(0,n-1,2):
            A[i], A[i+1] = A[i+1], A[i]

        return A

# print Solution().wave([2,5,1,6,3, 9,32,45,10,16])

def wave(A):
    i =0
    n = len(A)
    while i+1< n :
        if A[i] < A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
        i = i+2
    return A
print wave([ 5, 1, 3, 2, 4 ])