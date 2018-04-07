__author__ = 'venkat'

class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        result = []
        for a in A:
            result.insert(0,a)
        return ''.join(result)

print Solution().reverseString("abcd")