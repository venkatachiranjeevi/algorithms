__author__ = 'venkat'

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        res = []
        A = A.split('/')
        for a in A:
            if a == '..':
                if len(res) > 0:
                    res.pop()
            elif a == '.':
                continue
            elif len(a) != 0:
                res.append(a)
        return '/'+'/'.join(res)

print Solution().simplifyPath("/a/./b/../../c/")