class Solution:
    # @param A : integer
    # @return an integer
    def primesum(self, A):
        res = []
        if A < 2:
            return res

        i = 1
        res.append(2)
        while (4*i -1) < A:
            num1 = 4*i -1
            # if num1 + num1 == A:
            #     return [num1, num1]
            flag = self.check_is_prime(A-num1)
            if flag is False:
                temp = A-num1
                if temp+ num1 == A:
                    return [num1, temp]
            num2 = 4*i +1
            # if num2 + num2 == A:
            #     return [num2, num2]
            flag = self.check_is_prime(A-num2)
            if flag is False:
                temp = A-num2
                if temp+ num2 == A:
                    return [num2, temp]
            i += 1
        return []

    def check_is_prime(self, num):
        up = int(num**0.5)
        for i in xrange(2, up + 1):
                if i < num and num % i == 0:
                    return  True
        return False

print Solution().primesum(5)