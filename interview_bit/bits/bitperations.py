__author__ = 'venkat'

class Solution:

    def add(self, x, y):
        a = x & y
        b = x ^ y
        x = a << 1
        y = b
        while a:
            a = x & y
            b = x ^ y
            x = a << 1
            y = b
        return b

    def subtract(self, x , y):
        flag = False
        if y > x:
            temp = x
            x = y
            y = temp
            flag = True
        while y:
            borrow = (~x) & y
            x = x^y
            y = borrow << 1
        if flag:
            return -x
        return x

    def division(self, A, B):
        ret = 0
        p = abs(A)
        q = abs(B)
        while p >= q:
            count = 0
            while p >= (q<<count):
                count += 1
            ret += 1 << (count-1)
            p -= q << (count-1)
        if A == -2147483648 and B == -1:
            return 2147483647
        if A*B < 0:
            return -ret
        return ret

    def divide(self, dividend, divisor):
        num1 = abs(dividend)
        num2 = abs(divisor)
        result = 0
        while num1 >= num2:
            count = 0
            while num1 >= (num2 << count):
                count += 1

            result += 1 << (count -1)
            num1 -= num2 << (count -1)

        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if dividend*divisor < 0:
            return -result
        return result

    def max_con_one(self, A):
        count = 0
        while A!= 0:
            A = (A & A<< 1)
            count += 1

        return count

print Solution().max_con_one(14)