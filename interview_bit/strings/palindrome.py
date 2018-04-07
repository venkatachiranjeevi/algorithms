__author__ = 'customfurnish'

class Solution:

    def isPalindrome(self, A):
        n = len(A)
        if n is 0 or n is 1:
            return 1
        l = 0
        h = len(A) -1
        A= A.lower()
        while l<= h:
            while l !=n and (A[l] == " " or not A[l].isalnum()):
                l += 1
                if l is n:
                    return 1
            while h != 0 and (A[h] == " " or not A[h].isalnum()):
                h -= 1
                if h is 0:
                    return 1
            if A[l] != A[h]:
                return 0
            l += 1
            h -= 1

        return 1


print Solution().isPalindrome(".,")