__author__ = 'customfurnish'


class Solution:

    def sqrt(self, A):
        if A is 0 or A is 1:
            return A
        x = A
        y =1
        while x > y:
            x = (x+y)/2
            y =  A/x
        # result = 1
        # i = 1
        # while result < A:
        #     if result == A:
        #         return result
        #     i += 1
        #     result = i * i

        return int(x)

print Solution().sqrt(2)