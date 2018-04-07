__author__ = 'customfurnish'

class Solution:

    def rearrange(self, A):
        l = len(A)
        temp = [0] * l
        i = 0
        while(i< l):
            temp[i] = A[A[i]]
            i += 1
        return temp

    def arrange(self, A):
        n = len(A)
        temp = [0]*n
        for i in range(n):
            temp[i] = A[i]
        for i in range(n):
            A[i] = temp[temp[i]]
        return A
# print Solution().res([1,5,0,4,2,3])
print Solution().arrange([4, 0, 2, 1, 3])