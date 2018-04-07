__author__ = 'customfurnish'
def reqPainters(A, mid):
    total = 0
    numPainters = 1
    for i in range(len(A)):
        total += A[i]
        if (total > mid):
            total = A[i]
            numPainters += 1
    return numPainters

class Solutison:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        lo = max(A)
        hi = sum(A)
        n = len(A)

        if B > n:
            return -1

        while lo < hi:
            mid = lo+(hi-lo)/2
            requiredPainters = reqPainters(A, mid)

            if requiredPainters <= B:
                hi = mid
            else:
                lo = mid + 1
        return lo




class Solution:

    def find_req_st(self, A, mid):
        total = 0
        num_of_st = 1
        for st in A:
            total += st
            if total > mid:
                total = st
                num_of_st += 1
        return num_of_st

    def books(self, A, B):
        low = max(A)
        high = sum(A)
        n = len(A)
        if n < B:
            return -1

        while low < high:
            mid = low + (high-low)/2
            req_num = self.find_req_st(A, mid)
            if req_num <= B:
                high = mid
            else:
                low = mid+1
        return low

print Solution().books([12, 34, 67, 90],2)