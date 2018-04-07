__author__ = 'customfurnish'


class Solution:

    def get_index(self, A, B):
        n = len(A)
        l = 0
        first = -1
        h = n -1
        while l<= h:
            mid = (l+h)/2
            if A[mid] == B:
                first = mid
                h = mid -1

            elif A[mid] > B:
                h = mid - 1
            else:
                l = mid + 1
        return first


    def searchRange(self, A, B):
        first = self.get_index(A, B)

        if first == -1:
            return [-1, -1]
        l = first
        h = len(A)-1
        second  =  -1

        while l <= h:
            mid = (l+h)/2
            if A[mid] == B:
                second = mid
                l = mid + 1
            elif A[mid] > B:
                h = mid - 1
            else:
                l = mid + 1
        return [first, second]

print Solution().searchRange([5, 7, 7, 8, 8, 10], 10)