__author__ = 'customfurnish'


class Solution:
    def get_ele_index(self, A, B):
        left = 0
        right = len(A)-1
        ele = (left + right) / 2
        while left <= right:
            if A[ele] == B:
                return ele
            elif A[ele] > B:
                right = ele -1
            else:
                left = ele + 1
            ele = (left + right) / 2

        return -1

    def findCount(self, A, B):
        rIndex =lIndex = self.get_ele_index(A, B)
        if rIndex is -1:
            return 0
        count = 1
        lIndex -=1
        while lIndex >= 0 and A[lIndex] == B:
            count += 1
            lIndex -=1
        rIndex += 1
        while rIndex != len(A) and A[rIndex] == B:
            count +=1
            rIndex +=1
        return count

print Solution().findCount( [ ], 10)