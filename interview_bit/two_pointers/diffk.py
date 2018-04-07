__author__ = 'venkat'

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        i = 0
        j = 1
        while i < n and j < n:
            if A[j]-A[i] == B and i != j:
                return 1
            elif A[j] - A[i] <B:
                j += 1
            else:
                i += 1

        return 0


print Solution().diffPossible([ 1, 2, 2, 3, 4 ], 0)