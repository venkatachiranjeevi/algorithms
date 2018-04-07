__author__ = 'customfurnish'

class Solution:

    def cal_pow(self, x, n):
        if n is 0:
            return 1
        temp = self.cal_pow(x, n/2)
        if n%2 is 0:
            return temp*temp
        else:
            return x*temp*temp

    def power(self, x, n, d):
        power = self.cal_pow(x , n)
        return power%d
    def pow(self, A, B, C):
        result = 1
        base = A % C
        while B > 0:
            if B % 2 == 1:
                result = (result*base) % C
            B = B >> 1
            base = (base*base)%C
        return result%C

    def cal(self, x,n,d):
        res = 1
        base = x %d
        while n > 0:
            if n % 2 == 1:
                res = (base * res) % d
            n = n >> 1
            base = (base*base) %d
        return res%d
print Solution().cal(2,5,3)