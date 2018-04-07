__author__ = 'venkat'

class Solution:

    def maxone(self, A, B):
        left = right = 0
        bestLeft = 0
        bestLength = 0
        count  = 0
        if A[right] == 0:
            count += 1
        n = len(A)
        res = []
        while right < n:
            if count <= B :
                right += 1
                if right < n and A[right] == 0:
                    count += 1


            if count > B :
                if A[left] == 0:
                    count -= 1
                left += 1
            if right >=n :
                if n-1-left > bestLength - bestLeft:
                    bestLength = n-1
                    bestLeft = left
            elif right - left > bestLength- bestLeft:
                bestLength = right
                bestLeft = left

        if bestLength > n-1:
            bestLength = n-1

        return range(bestLeft, bestLength +1)


Solution().maxone([1, 0, 0, 1, 1, 0, 1, 0, 1, 1 ],2)