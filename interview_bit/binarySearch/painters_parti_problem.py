__author__ = 'customfurnish'

class Solution:

    def find_num_of_painters(self, A, mid):
        total = 0
        painters = 1
        for x in A:
            total += x
            if total > mid:
                total = x
                painters += 1

        return painters


    def paint(self, A, B, C):
        l = max(C)
        h = sum(C)
        while l < h:
            mid = (l+h)/2
            req_pain = self.find_num_of_painters(C, mid)

            if req_pain <= A:
               h = mid
            else:
                l = mid+1

        return l*B %100033

print Solution().paint(5, 2, [1,10, 20, 40])