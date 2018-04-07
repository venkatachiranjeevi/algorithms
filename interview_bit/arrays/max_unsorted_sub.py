__author__ = 'venkat'


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        A = list(A)
        n = len(A)
        if n is 0:
            return -1
        i =0
        j = n-1
        while i< n-1:
            if A[i] > A[i+1]:
                break
            i += 1
        if i is n-1:
            return -1
        start = i
        while j > 0:
            if A[j] < A[j-1]:
                break
            j -= 1
        end = j
        r = A[start:end+1]
        min_val = min(r)
        max_val = max(r)
        i = 0
        while i< start:
            if A[i]>min_val:
                start = i
                break
            i += 1
        j = n-1
        while j >= end+1:
            if A[j] < max_val:
                end = j
                break
            j -= 1
        return [start, end]

# a = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
print Solution().subUnsort([ 1, 2, 3 ])