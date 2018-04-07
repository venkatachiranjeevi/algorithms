__author__ = 'customfurnish'
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        A= A.split(".")
        B = B.split(".")
        m = len(A)
        n = len(B)
        for i in range(m):
            A[i] = int(A[i])
        for j in range(n):
            B[j] = int(B[j])

        min_index= min(m,n)
        for x in range(min_index):
            if A[x] > B[x]:
                return 1
            if A[x] < B[x]:
                return -1
        if m > n:
            if sum(A[n: ]) > 0:
                return 1
        if m < n:
            if sum(B[m: ]) > 0:
                return -1
        return 0

    def compaareVersion(self, A, B):
        A = A.split('.')
        B = B.split('.')
        lenA = len(A)
        lenB = len(B)
        for i in range(lenA):
            A[i] = int(A[i])
        for i in range(lenB):
            B[i] = int(B[i])
        loopCount = min(lenA, lenB)
        for i in range(loopCount):
            if A[i] > B[i]:
                return 1
            if A[i] < B[i]:
                return -1
        if lenA > lenB:
            if sum(A[lenB:]) > 0:
                return 1
        if lenA < lenB:
            if sum(B[lenA:]) > 0:
                return -1
        return 0

print Solution().compareVersion("1.13", "1.13.4")
print Solution().compaareVersion("1.13", "1.13.4")