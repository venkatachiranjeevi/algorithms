__author__ = 'venkat'

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        count = 31
        revesre_num = 0
        while count >= 0:
            bit = ((A & 1<<count) >> count)&1
            revesre_num = revesre_num | bit << (31-count)
            count -= 1

        return revesre_num


print Solution().reverse(31)