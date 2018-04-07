__author__ = 'venkat'


class Solution:
    def maxset(self, A):
        res = []
        temp = []
        max_sum = 0
        for x in A:
            if x >= 0:
                temp.append(x)
            else:
                count = sum(temp)
                if count >= max_sum:
                    res = temp
                    max_sum = count
                temp = []
        if sum(temp) > max_sum:
            return temp
        return res


a =  [ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]
print Solution().maxset(a)