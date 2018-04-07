__author__ = 'venkat'

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSum(self, A):
        n = len(A)
        if n == 0 :
            return []
        A.sort()
        ret = []
        for i in range(n-1):
            if i == 0 or A[i] > A[i-1]:
                j = i+1
                k = n-1
                while j < k:
                    temp = A[i] + A[j] + A[k]
                    if temp == 0 :
                       ret.append([A[i], A[j], A[k]])
                       j += 1
                       k -= 1
                       while j <k and A[k] == A[k+1]:
                           k -= 1
                       while j <k and A[j] == A[j-1]:
                           j += 1

                    elif temp < 0:
                       j += 1
                    else:
                       k -= 1
        return ret

print Solution().threeSum( [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ])

# [-5 0 5 ] [-5 1 4 ] [-4 -1 5 ] [-4 0 4 ] [-4 1 3 ] [-3 -2 5 ] [-3 -1 4 ] [-3 0 3 ] [-2 -1 3 ] [-2 1 1 ] [-1 0 1 ] [0 0 0 ]
# -5 -2 -1 1 2 3
# [-5, 0, 5], [-5, 1, 4], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-2, -1, 3], [-2, 1, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [0, 0, 0]]
