import sys

__author__ = 'venkat'

class Solution:
    def reverse(self, A):
        flag= False
        st = str(A)
        if A<0 :
            st = st[1:]
            flag = True
        st = st[::-1]
        res = int(st)
        if res > 2**31:
            return 0
        return -res if flag else res

    def dasd(self, A):
        A = str(A)
        if A[0] == '-':
            A = '-'+A[1:][::-1]
        else:
            A = A[::-1]
        A = int(A)
        if A > 2**31 or A < -2**31:
            return 0
        return A

print Solution().reverse(-1146467285)