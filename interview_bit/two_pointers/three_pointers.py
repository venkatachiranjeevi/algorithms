import sys


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        i = j = k =0
        len1 = len(A)
        len2 = len(B)
        len3 = len(C)
        diff = sys.maxint

        while i < len1 and j < len2 and k < len3:
            min_val = min(A[i],B[j],C[k])
            max_val = max(A[i], B[j], C[k])

            if max_val - min_val < diff:
                x = i
                y = j
                z = k
                diff = max_val - min_val

            if min_val == A[i]:
                i += 1
            elif min_val == B[j]:
                j += 1
            else:
                k += 1

        return max(abs(A[x]-B[y]), abs(B[y]-C[z]), abs(C[z]-A[x]))

print Solution().minimize([1, 4, 10], [2, 15, 20], [10,12])