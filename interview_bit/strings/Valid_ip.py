__author__ = 'customfurnish'

class Solution:

    def restoreIpAddresses(self, A):
        n = len(A)
        if n < 4 or n > 12:
            return []
        res = []
        i =1
        while i <= 3 and i < n:
            j = i+1
            while j <= i + 3 and j < n:
                k = j + 1
                while k <= j + 3 and k < n:
                    first = int(A[:i])
                    second = int(A[i:j])
                    third = int(A[j:k])
                    fourth = int(A[k:])
                    if (A[0] == '0' and (i > 1or first != 0)) or (A[i] == '0' and (j > i+1 or second != 0)) or (A[j] == '0' and (k > j + 1 or third != 0)) or (A[k] == '0' and (n > k+1 or fourth != 0)):
                        # Do Nothing
                        k += 1
                        continue
                    elif first <= 255 and first >= 0 and second <= 255 and second >= 0 and third <= 255 and third >= 0 and fourth <= 255 and fourth >= 0:
                        res.append(A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:])
                    k += 1
                j += 1
            i += 1
        return res

# print Solution().restoreIpAddresses("0000")

def IpValid(A):
    n = len(A)
    if n <4 or n > 12:
        return []
    res = []
    i =1
    while i <= 3 and i < n:
        j = i+1
        while j <= i + 3 and j < n:
            k = j + 1
            while k <= j + 3 and k < n:
                first = int(A[:i])
                second = int(A[i:j])
                third = int(A[j:k])
                fo = int(A[k:])
                if (A[0] == '0' and (i >1 or first !=0)) or (A[i] == '0' and (j > i+1 or second != 0)) or (A[j] == '0' and (k>j+1 or third != 0)) or (A[k] == '0' and (n > k+1 or fo !=0)):
                    k += 1
                    continue
                elif first <= 255 and first >= 0 and second <= 255 and second >= 0 and third <= 255 and third >= 0 and fo >= 0 and fo <= 255:
                    res.append(A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:])
                    k += 1
            j += 1
        i += 1
        return res

print IpValid("0000")