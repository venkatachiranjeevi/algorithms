__author__ = 'customfurnish'

class Solution:

    def reverseWords(self, A):
        x = A.split()
        n = len(x) - 1
        output = ""
        while n >= 0:
            output += x [n] + " "
            n -= 1
        return output.strip()
print Solution().reverseWords('The     quick brown    fox')