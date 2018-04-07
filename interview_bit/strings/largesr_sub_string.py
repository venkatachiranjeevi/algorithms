__author__ = 'customfurnish'

class Solution:
    def largest_sub_string(self, A):
        n = len(A)
        cur_len = 1
        max_len = 1
        visited = [-1] * 256
        visited[ord(A[0])] = 0
        for x in range(1, n):
            prev = visited[ord(A[x])]
            if prev == -1 or x - cur_len > prev:
                cur_len += 1
            else:
                if max_len < cur_len:
                    max_len = cur_len
                cur_len = x - prev
            visited[ord(A[x])] = x
        if cur_len > max_len:
            return cur_len
        return max_len

print Solution().largest_sub_string("ABCDA")