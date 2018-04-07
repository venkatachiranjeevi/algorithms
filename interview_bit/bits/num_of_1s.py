__author__ = 'venkat'

class Solution():

     def numSetBits(self, A):
        count = 0
        while A:
            A &= (A-1)
            count += 1

        return count

print Solution().numSetBits(1235)