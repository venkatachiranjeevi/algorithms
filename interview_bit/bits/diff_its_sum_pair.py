class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        ans = 0
        M = 1000000007
        for i in range(32):
            count = 0
            for x in range(len(A)):
                if (A[x] &(1 << i)) :
                    count += 1

            ans += (count *(len(A) - count) * 2) % M
            if ans > M:
                ans -= M

        return ans
print Solution().cntBits([1,3,3,5])