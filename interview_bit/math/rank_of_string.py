__author__ = 'customfurnish'

# def fact(n):
#     if n <= 1:
#         return 1
#     return fact(n-1) * n


def popIn(temp, str):
    for x in str:
        temp[ord(x)] += temp[ord(x)]+1

    for x in range(1, 256):
        temp[x] += temp[x-1]
    return temp


def updateCount(li, limit):
    for x in range(limit, 256):
        li[x] -= 1
    return li

def find_rank(s):
    # mul = fact(len(s))
    mul = 0
    n = len(s)
    rank =1
    temp = [0]*256
    temp = popIn(temp, s)
    for x in range(n):
        mul /= n-x
        rank += temp[ord(s[x])-1] * mul
        temp = updateCount(temp, ord(s[x]))

    print rank



# S = "STRING"
# find_rank("ashole")
# print fact(5)

class Solution:

    def fact(self, n):
        if n <= 1:
            return 1
        return self.fact(n-1) * n

    def findLowet(self, S, i):
        count =0
        for x in S:
            if x < i:
                count += 1
        return count

    def find_repititive(self, S):
        count = 1
        temp = [0] *256
        for x in S:
            temp[ord(x)] += 1
        for a in S:
            count *= self.fact(temp[ord(a)])
            temp[ord(a)] = 1
        return count

    def findRank(self, A):
        n = len(A)
        rank = 1
        fact_val = self.fact(n)
        for x in range(n):
            fact_val /= n-x
            less = self.findLowet(A[x+1:], A[x])
            repe =self.find_repititive(A[x:])
            temp= (fact_val *less)/repe
            rank += temp

        if rank > 1000003:
            return rank % 1000003
        return rank

print Solution().findRank("asasdsdsadasdadsadasdsa")