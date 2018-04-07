__author__ = 'venkat'


def add_number(a):
    n = len(a)
    if n is 0:
        return [1]
    i = n-1
    num = a[i] + 1
    carry = 0
    while i >=0:
        num = a[i] + 1 + carry
        if num <= 9:
            carry = 0
            a[i] = num
            break
        else:
            a[i] = 0
            carry = num - 9
        i -= 1
    if carry != 0:
        return [carry] + a
    return  a

print add_number([9])

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)
        if n is 0:
            return [1]
        num = A[n-1] + 1
        carry = 0
        i = n-1
        while i>=0:
            if num < 10:
                A[i] = num
                carry = 0
                break
            else:
                A[i] = 0
                carry = 1
            i -= 1
            num = A[i] + 1

        if carry !=0:
            return [carry] + A
        while A[0] ==0:
            A.pop(0)
        return  A

x = Solution()
print x.plusOne([0,0,9])


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if n is 0:
            return [1]
        num = digits[n-1] + 1
        carry = 0
        i = n-1
        while i>=0:
            if num < 10:
                digits[i] = num
                carry = 0
                break
            else:
                digits[i] = 0
                carry = 1
            i -= 1
            num = digits[i] + 1

        if carry !=0:
            return [carry] + digits
        while digits[0] ==0:
            digits.pop(0)
        return  digits