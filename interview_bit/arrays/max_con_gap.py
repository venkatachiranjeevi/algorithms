import sys

__author__ = 'venkat'

class Solution:
    def maximumGap(self, A):
        n = len(A)
        if n < 2:
            return 0
        max_val = max(A)
        min_val = min(A)
        b_min = [sys.maxint] * n
        b_max = [-sys.maxint] * n
        gap = (max_val -min_val-1)/(n-1) + 1
        if gap == 0 :
            return 0
        for x in range(n):
            id = (A[x]-min_val) /gap
            b_max[id] = max(b_max[id], A[x])
            b_min[id] = min(b_min[id], A[x])

        max_gap = -sys.maxint
        prev = min_val
        for x in range(n):
            if b_max[x] == -sys.maxint and b_min[x] == sys.maxint:
                continue
            else:
                max_gap = max(max_gap, b_min[x] - prev)
                prev = b_max[x]
        return max_gap
        #     for y in range(x, n-1):
        #         pass

print Solution().maxGap( [ 100, 100, 100, 100, 100 ])