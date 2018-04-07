__author__ = 'venkat'
class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        assert(len(A) == (B-1))
        res = [0]*(B)
        for x in range(B):
            res[x] = x+1
        if "D" not in  A:
            return res
        if "I" not in A :
            res.reverse()
            return res
        start = 1
        end = B
        count = 0
        while count < B and start < end:
            if A[count] is "D":
                res[count] = end
                end -=1
            else:
                res[count] = start
                start += 1
            count +=1
        assert(start == end)
        res[B-1] = start
        return res


s = Solution().findPerm("ID", 3)
print s