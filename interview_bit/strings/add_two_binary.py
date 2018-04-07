__author__ = 'venkat'


class Solution():

    def addBinary(self, A, B):
        len1 = len(A) - 1
        len2 = len(B) - 1
        rem = 0
        res = ""
        while len1 >= 0 and len2 >= 0:
            temp = int(A[len1]) + int(B[len2]) + rem
            rem = temp / 2
            ans = temp % 2
            res += str(ans)
            len1 -= 1
            len2 -= 1

        while len1 >=0 :
            temp = int(A[len1]) + rem
            rem = temp / 2
            ans = temp % 2
            res += str(ans)
            len1 -= 1
        while len2 >=0 :
            temp = int(B[len2]) + rem
            rem = temp / 2
            ans = temp % 2
            res += str(ans)
            len2 -= 1

        if rem !=0:
            res += str(rem)

        return res[::-1]


print Solution().addBinary("11", "1110")