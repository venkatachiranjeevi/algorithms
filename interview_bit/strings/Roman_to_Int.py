__author__ = 'customfurnish'

class Solution:

    def value(self, r):
        if (r == 'I'):
            return 1
        if (r == 'V'):
            return 5
        if (r == 'X'):
            return 10
        if (r == 'L'):
            return 50
        if (r == 'C'):
            return 100
        if (r == 'D'):
            return 500
        if (r == 'M'):
            return 1000
        return -1

    def romanToInt(self, A):
        n = len(A)
        if n is 0:
            return 0
        i = 0
        res = 0
        while i < n:
            s1 = self.value(A[i])
            if i+1 < n:
                s2 = self.value(A[i+1])
                if s1 >= s2:
                    res += s1
                    i += 1
                else:
                    res = res+ s2 -s1
                    i += 2
            else:
                res += s1
                i += 1

        return res

print Solution().romanToInt("XIV")
