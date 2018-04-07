__author__ = 'venkat'

def next_permutation(s):
  for i in reversed(xrange(len(s))):
    if s[i] > s[i-1]:
      break
  else:
    return []
  i -= 1
  for j in reversed(xrange(i + 1, len(s))):
    if s[j] > s[i]: break
    t = s[i]
    s[i] = s[j]
    s[j] = t
    s[i + 1:] = reversed(s[i + 1:])
  return s

# print next_permutation([1,3,2])

# print next([1,2,3])

class Solution:
    
    def nextPermutation(self, A):
        i = len(A) - 2
        while not (i < 0 or A[i] < A[i+1]):
            i -= 1
        if i < 0:
            A.sort()
            return A
        # else
        j = len(A) - 1
        while not (A[j] > A[i]):
            j -= 1
        A[i], A[j] = A[j], A[i]        # swap
        A[i+1:] = reversed(A[i+1:])
        # reverse elements from position i+1 till the end of the sequence
        return A

A = [1,2,3,6,5,4]
print Solution().nextPermutation([1,3,2])