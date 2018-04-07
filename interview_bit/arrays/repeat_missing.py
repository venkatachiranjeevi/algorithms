__author__ = 'venkat'


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        sum = ((n) * (n+1))/2
        li = [0] *(n+1)
        for i in range(n):
            sum -=A[i]
            li[A[i]] += 1
        for i in range(len(li)):
            if li[i] > 1:
                return [i, sum+i]
        return [-1, sum]


def repeat(A):
    x1 = A[0]
    x2 =1
    for i in range(1, len(A)):
        x1 = x1^ A[i]
    for i in range(2, len(A)+2):
        x2 = x2 ^ i

    print x1 ^ x2

repeat([1, 2,3, 4, 5, 6])