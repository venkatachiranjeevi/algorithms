__author__ = 'customfurnish'

class Solution:
    def countSay(self, A):
        if A is 1:
            return "1"
        if A is 2:
            return "11"
        res = "11"
        for x in range(3, A):
            res += "@"
            l = len(res)
            temp = ""
            count = 1
            for x in range(1, l):
                if res[x] != res[x-1]:
                    temp += str(count)
                    temp += res[l-1]
                    count = 1
                else:
                    count += 1
            res += temp
        return res

    def countAndSay(self, A):
        if A == 1:
            return "1"
        pre = "1"
        result = ""
        while A > 1:
            result = ""
            i = 0
            while i < len(pre):
                j = i + 1
                c = 1
                while j < len(pre) and pre[j] == pre[j-1]:
                    c += 1
                    j += 1
                i = j
                result += str(c) + pre[j-1]
            pre = result
            A -= 1
        return result

    def countNSay(self, A):
        if A is 1:
            return "1"
        pre = "1"
        res = ""
        while A > 1:
            res = ""
            l = len(pre)
            i = 0
            while i < l:
                j = i + 1
                c = 1
                while j < l and pre[j] == pre[j-1]:
                    j += 1
                    c += 1
                i = j
                res += str(c)+ pre[j-1]
            pre = res
            A -= 1
        return res

print Solution().countAndSay(5)
print Solution().countNSay(5)
