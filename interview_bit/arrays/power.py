
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return float(1.0/self.my_pow_util(x,-n))
        return self.my_pow_util(x, n)

    def my_pow_util(self, x, n):
        if int(n) is 0:
            return 1
        temp = self.my_pow_util(x, n/2)
        if n %2 is 0:
            return temp * temp
        else:
            if n > 0:
                return x *temp*temp
            else:
                return temp*temp /x
# print pow(34.00515, -3)
print Solution().myPow(34.00515, -3)