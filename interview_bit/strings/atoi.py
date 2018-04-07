
__author__ = 'customfurnish'

class Solution:

    def atoi(self, A):
        A = A.strip()
        length = len(A)
        flag = False
        if A[0] == "-":
            flag = True
            A = A[1:]
            length -=1
        if A[0] == "+":
            A = A[1:]
            length -=1
        res = 0
        for x in range(length):
            if '0' <= A[x] <= '9':
               res =res * 10 + int(A[x])
            else:
                break
        if flag:
            if res > 2147483647:
                return -2147483648
            return -res
        return res if res < 2147483647 else 2147483647


print Solution().atoi(" -88297 248252140B12 37239U4622733246I218  9 1303   44 A")