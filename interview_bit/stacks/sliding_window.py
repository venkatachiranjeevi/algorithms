__author__ = 'venkat'


# [1 3 -1] -3 5 3 6 7	3
# 1 [3 -1 -3] 5 3 6 7	3
# 1 3 [-1 -3 5] 3 6 7	5
# 1 3 -1 [-3 5 3] 6 7	5
# 1 3 -1 -3 [5 3 6] 7	6
# 1 3 -1 -3 5 [3 6 7]	7



class Solution1:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        st = []
        i =0
        res = []
        n = len(A)
        while i < n-(B-1):
            j = i
            while j-i < B and j < n:
                if len(st) == 0:
                    st.append(A[j])
                elif st[-1] < A[j]:
                    st.pop()
                    st.append(A[j])
                j +=1
            res.append(st[-1])
            st.pop()
            i +=1
        return res

from collections import deque
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        queue = deque()
        ret = []
        n = len(A)

        for i in range(B):
            while len(queue) != 0 and i < n and A[i] >= A[queue[-1]]:
                queue.pop()
            queue.append(i)
        for i in range(B,n):
            ret.append(A[queue[0]])
            while len(queue) != 0 and A[i] >= A[queue[-1]]:
                queue.pop()
            while len(queue) != 0 and queue[0] <= i-B:
                queue.popleft()
            queue.append(i)
        ret.append(A[queue[0]])
        return ret

    def sliding_window(self, A, B):
        n = len(A)
        helper = deque()
        res = []
        for i in range(B):
            while len(helper) != 0 and i < n and A[i] >= A[helper[-1]]:
                helper.pop()
            helper.append(i)
        for i in range(B, n):
            res.append(A[helper[0]])
            while len(helper) != 0 and A[i] >= A[helper[-1]]:
                helper.pop()
            while len(helper) !=0 and helper[0] <= i-B:
                helper.popleft()
            helper.append(i)
        res.append(A[helper[0]])
        return res

print Solution().sliding_window([ 648, 614, 490, 138, 657, 544, 745, 582, 738, 229, 775, 665, 876, 448, 4, 81, 807, 578, 712, 951, 867, 328, 308, 440, 542, 178, 637, 446, 882, 760, 354, 523, 935, 277, 158, 698, 536, 165, 892, 327, 574, 516, 36, 705, 900, 482, 558, 937, 207, 368 ], 9)
print Solution().slidingMaximum([ 648, 614, 490, 138, 657, 544, 745, 582, 738, 229, 775, 665, 876, 448, 4, 81, 807, 578, 712, 951, 867, 328, 308, 440, 542, 178, 637, 446, 882, 760, 354, 523, 935, 277, 158, 698, 536, 165, 892, 327, 574, 516, 36, 705, 900, 482, 558, 937, 207, 368 ], 9)

# [648, 614, 775, 775, 876, 876, 876, 876, 876, 876, 876, 951, 951, 951, 951, 951, 951, 951, 951, 951, 882, 882, 882, 882, 935, 935, 935, 935, 935, 935, 935, 935, 935, 892, 892, 892, 900, 900, 900, 937, 937, 937]

# 745 745 775 775 876 876 876 876 876 876 876 951 951 951 951 951 951 951 951 951 882 882 882 882 935 935 935 935 935 935 935 935 935 892 892 892 900 900 900 937 937 937
