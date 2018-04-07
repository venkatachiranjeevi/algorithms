
__author__ = 'venkat'
class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        n = len(arr)-1
        res = []
        st = []
        for ele in arr:
            while len(st) != 0 and st[-1] >= ele:
                st.pop()

            if len(st) == 0:
                res.append(-1)
            else:
                res.append(st[-1])
            st.append(ele)

        return res

print Solution().prevSmaller([1,3,0,2,5])