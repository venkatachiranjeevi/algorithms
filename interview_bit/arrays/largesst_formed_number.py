__author__ = 'venkat'
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        if isinstance(A, tuple) is True:
            A = list(A)
        A.sort(reverse=True)
        result = str(A[0])
        for i in range(1, len(A)):
            if int(result) + A[i] is not 0:
                temp_x = result + str(A[i])
                temp_y = str(A[i])+ result
                if int(temp_x) > int(temp_y):
                    result += str(A[i])
                else:
                    result = str(A[i]) + result
        return result

    def compare(self, x,y,result):
        temp_x = result + str(x)
        temp_y = result + str(y)
        return  0 if temp_x>temp_y else 1

# print Solution().largestNumber((89,4,3))


from fractions import Fraction
class Soalution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = sorted(A, key=lambda n: Fraction(n, 10**len(str(n))-1), reverse=True)
        i = 0
        while i < len(A)-1:
            if A[i] != 0:
                break
            else:
                i+=1
        ret = map(lambda x:str(x),A[i:])
        return ''.join(ret)
        # return result
print Soalution().largestNumber([1])

