__author__ = 'customfurnish'

class Solution:

    def lengthOfLastWord(self, A):
        A = A.strip()
        n = len(A)
        if n < 1:
            return 0
        i = 0
        res = 0
        while i < n:
            if A[i] != " ":
                res += 1
            else:
                res = 0
            i += 1

        return res

print Solution().lengthOfLastWord("Wordl   ")
