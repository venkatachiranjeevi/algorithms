__author__ = 'customfurnish'




S = "P.......A........H.......N..A." \
    ".P....L....S....I...I....G." \
    "...Y.........I........R"


class Solution:

    def convert(self, A, B):
        n = len(A)
        if n < 3 or B < 2:
            return A
        result = [""]* B
        flag = True
        ra = -1
        for x in range(n):
            if flag:
                ra += 1
            else:
                ra -=1
            if ra >= B-1:
                flag = False
                ra = B-1
            elif ra <= 0 :
                flag = True
                ra = 0
            result[ra] += A[x]
        res = ""
        for x in result:
            res += x
        return res

print Solution().convert("PAYPALISHIRING", 3)