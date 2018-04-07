__author__ = 'venkat'

class Solution:
    def primesum(self, n):
        for i in xrange(2, n):
            if self.check_is_prime(i) and self.check_is_prime(n - i):
                return i, n - i

    def check_is_prime(self, num):
        if num < 2:
            return False
        up = int(num**0.5)
        for i in xrange(2, up + 1):
                if i < num and num % i == 0:
                    return  False
        return True

print Solution().primesum(4)