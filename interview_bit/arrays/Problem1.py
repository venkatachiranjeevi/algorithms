__author__ = 'venkat'
def coverPoints(self, X, Y):
    ret = 0
    n = len(X)
    if n ==0:
        return ret
    curr = (X[0], Y[0])

    for i in range(1,n):
        stepsX = abs(curr[0] - X[i])
        stepsY = abs(curr[1] - Y[i])
        ret += max(stepsX, stepsY)
        curr = (X[i], Y[i])
    return ret


class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        result = 0
        n = len(X)
        if n is 0:
            return result
        curr = (X[0], Y[0])
        for i in range(1, n):
            x = abs(curr[0] - X[i])
            y = abs(curr[1] - Y[i])
            result += max(x,y)
            curr = (X[i], Y[i])
        return result