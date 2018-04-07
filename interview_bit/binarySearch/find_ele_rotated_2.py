__author__ = 'customfurnish'

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer

    def search(self, A, B):
        n = len(A)
        l = 0
        h = n - 1
        mid = -1
        while l <= h:
            mid = (l+h)/2
            next = (mid+1)%n
            prev = (mid+n-1)%n
            if A[l] <= A[h]:
                mid = l
                break
            elif A[mid] <= A[prev] and A[mid] <= A[next]:
                mid = mid
                break
            elif A[mid] <= A[h]:
                h = mid - 1
            elif A[mid] >= A[l]:
                l = mid + 1
        if mid == -1:
            return -1
        # if A[mid] is B:
        #     return mid
        # if B >=A[0] and B<= A[mid-1]:
        #     res =  self.find_ele(A[0:mid], B)
        #     if res != -1:
        #         return res
        # else:
        #     res = self.find_ele(A[mid+1:], B)
        #     if res != -1:
        #         return mid+1+res
        l = 0
        h = mid-1
        while l <= h:
            mid = (l+h)/2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                l = mid + 1
            else:
                h = mid - 1
        l = mid
        h = n - 1
        while l <= h:
            mid = (l+h)/2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                l = mid + 1
            else:
                h = mid - 1
        return -1

print Solution().search([ 1, 7, 67, 133, 178 ], 1)