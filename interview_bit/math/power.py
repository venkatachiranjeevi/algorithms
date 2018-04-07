__author__ = 'venkat'
class Solution:
    def power(self, A):
        if A is 1:
            return True
        low =2
        sq= int(A ** 0.5)
        while low <= sq:
            i =2
            power = pow(low, i)
            while i<=A and power >0:
                if power == A:
                    return True
                i += 1
                power =pow(low, i)
            low +=1
        return False

    def isPower(self, A):
        if A is 1:
            return 1
        low =2
        sq= int(A ** 0.5)
        while low <= sq:
            p = low
            while p<=A:
                p *= low
                if p is A:
                    return 1
            low +=1
        return 0

    def isPowerO(self, N):
        if N is 0:
            return False
        if N is 1:
            return True
        res = []
        for p in xrange(2,33):
            for A in xrange(2, int(N**(1.0 / p)) + 2):
                if A**p == N:
                    res.append(A)
                    # return True
        print res
        return False

    def isPow(self, N):
        if N is 0:
            return False
        if N is 1:
            return True
        for p in xrange(2,33):
            upper_limit = int(N ** (1.0/p))
            for num in xrange(2, upper_limit+2):
                if num ** p == N:
                    return True
        return False
print Solution().isPow(1240000)



