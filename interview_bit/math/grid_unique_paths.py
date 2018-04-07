__author__ = 'customfurnish'

class Solution:

    def uniquePaths(self, A, B):
        ans = 1
        for x in range(B, A+B-1):
            ans *= x
            ans /= (x-B+1)

        return ans

print Solution().uniquePaths(15, 9)