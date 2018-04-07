__author__ = 'venkat'

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        ret = []
        coef = A%10
        if coef <= 3:
            ret += ["I"*coef]
        elif coef == 4:
            ret += ["IV"]
        elif coef <= 8:
            ret += ["V"+"I"*(coef-5)]
        else:
            ret += ["IX"]
        coef = (A%100)/10
        if coef <= 3:
            ret += ["X"*coef]
        elif coef == 4:
            ret += ["XL"]
        elif coef <= 8:
            ret += ["L"+"X"*(coef-5)]
        else:
            ret += ["XC"]
        coef = (A%1000)/100
        if coef <= 3:
            ret += ["C"*coef]
        elif coef == 4:
            ret += ["CD"]
        elif coef <= 8:
            ret += ["D"+"C"*(coef-5)]
        else:
            ret += ["CM"]
        coef = (A%10000)/1000
        ret += ["M"*coef]
        ret.reverse()
        return "".join(ret)

print  Solution().intToRoman(128)