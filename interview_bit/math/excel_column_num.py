__author__ = 'venkat'

class Solution:
    def get_excel_num(self, A):
        result = 0
        for x in A:
            num = ord(x.upper()) - 64
            result = result * 26 + num
        return result

    def get_co_title(self, A):
        res = ""
        while A>0:
            mod = A % 26
            if mod is 0:
                res += 'Z'
                A = A/26 -1
            else:
                mod += 64
                res += chr(mod)
                A /= 26

        return res[::-1]
res =  Solution().get_excel_num('AAZZZZA')
print Solution().get_co_title(res)