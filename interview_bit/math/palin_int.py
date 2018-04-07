__author__ = 'venkat'

class Solution:
    def intPalin(self, A):
        temp = []
        if A < 0:
            return False
        while(A>0):
            temp.append(A%10)
            A /= 10
        i =0
        last = len(temp)-1
        while(i <=last):
            if temp[i] != temp[last]:
                return False
            i += 1
            last -=1
        return True

    def opti(self, A):
        count = 0
        temp = A
        while(temp>0):
            count +=1
            temp /=10
        tempCount = count
        temp = A
        while(tempCount > 0):
            limit = 10 **(count-1)
            start = temp / limit
            end = A%10
            if start != end:
                return False
            count -= 1
            tempCount -= 2
            A /=10
            temp %= limit
        return True
print Solution().opti(0)