import sys

__author__ = 'customfurnish'

A = [ "abcd", "abcd", "efgh" ]
B = ["geeksforgeeks", "geeks",
                    "geek", "geekzer"]
C = [

  "abcdefgh",

  "aefghfgh",

  "abcefgh"
]
class Solution:

    def find_minimum(self, A):
        min = sys.maxint
        for x in A:
            if len(x) < min:
                min = len(x)
        return min

    def isCommon(self, A, st, low, high):
        for x in A:
            if st != x[low:high+1]:
                return False
        return True

    def longestCommonPrefix(self, A):
        n = len(A)
        prefix = ""
        if n is 0:
            return 0
        high = self.find_minimum(A)
        low = 0
        while low <= high:
            mid = low + (high-low) / 2
            if self.isCommon(A, A[0][low:mid+1], low, mid):
                prefix += A[0][low:mid+1]
                low = mid + 1
            else:
                high = mid -1
        return prefix
print Solution().longestCommonPrefix(C)