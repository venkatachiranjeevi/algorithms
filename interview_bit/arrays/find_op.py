__author__ = 'venkat'

# def performOps(A):
#     m = len(A)
#     n = len(A[0])
#     B = []
#     for i in xrange(len(A)):
#         B.append([0] * n)
#         for j in xrange(len(A[i])):
#             B[i][n - 1 - j] = A[i][j]
#     return B
#
#
# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# # B = performOps(A)
# # for i in xrange(len(B)):
# #     for j in xrange(len(B[i])):
# #         print B[i][j]
#
#
#
# class Solution:
#     # @param a : list of integers
#     # @param b : integer
#     # @return a list of integers
#     def rotateArray(self, a, b):
#         ret = []
#         for i in xrange(len(a)):
#             ret.append(a[(i + b)  % len(a)])
#         return ret
#
# A = [1, 2, 3, 4, 5, 6]
# B = 1
# print Solution().rotateArray(A,B)


def perforsmOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in xrange(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B

# print perforsmOps([5, 10, 2, 1])
A = [5, 10, 2, 1]

B = perforsmOps(A)
for i in xrange(len(B)):
    print B[i],

