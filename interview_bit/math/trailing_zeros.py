__author__ = 'customfurnish'

class Solution:
    def trailingZeroes(self, A):
        i = 5
        count = 0
        while(A/i >= 1):
            count += A/i
            i *= 5
        return count

print Solution().trailingZeroes(24)