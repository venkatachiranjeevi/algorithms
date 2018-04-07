__author__ = 'venkat'

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        n = len(A)
        if n <= 3:
            return sum(A)
        A.sort()
        ret = 0
        minDiff = 2147483648
        for i in range(n-1):
            j = i+1
            k = n-1
            while j < k:
                temp = A[i] + A[j] + A[k]
                diff = abs(temp - B)
                if diff == 0 :
                    return temp
                if diff < minDiff:
                   minDiff = diff
                   ret = temp
                if temp < B:
                    j += 1
                else:
                    k -= 1
        return ret

print Solution().threeSumClosest([1,2,3, -5,-1, -4], 4)