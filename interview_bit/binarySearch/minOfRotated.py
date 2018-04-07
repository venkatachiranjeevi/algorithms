__author__ = 'customfurnish'

class Solution:

    def min(self, A):
        low = 0
        high = len(A)-1
        n = len(A)
        while low <= high:
            if A[low] <= A[high]:
                return low
            mid = (low + high) / 2
            next = (mid +1)  % n
            prev = (mid + n -1) % n
            if A[mid] <= A[next] and A[mid] <= A[prev]:
                return mid
            elif A[mid] <= A[high]:
                high = mid -1
            else:
                low = mid + 1

        return -1
    def findMin(self, A):
        index= self.min(A)
        if index != -1 :
            return A[index]

        return 0

print Solution().findMin([])