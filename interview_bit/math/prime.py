class Solution:
    # @param A : integer
    # @return an integer
    def sieve(self, A):
        res = []
        if A < 2:
            return res

        i = 1
        res.append(2)
        while (4*i -1) < A:
            num1 = 4*i -1
            num2 = 4*i +1
            flag1 = self.check_is_prime(num1)
            flag2 = self.check_is_prime(num2)
            if flag1 is False:
                res.append(num1)
            if flag2 is False and num2 <= A:
                res.append(num2)
            i += 1
        return res

    def check_is_prime(self, num):
        up = int(num**0.5)
        for i in xrange(2, up + 1):
                if i < num and num % i == 0:
                    return  True
        return False
print Solution().sieve(50000)