__author__ = 'customfurnish'


class Solution:

    def __init__(self, A):
        self.A = A
        self.rows = len(A)
        self.columns = len(A[0])

    def paths_finder(self):
        self.print_paths(0, 0, "", [])
        x = 10

    def print_paths(self, m ,n, path, temp):
        if m == self.rows -1:
            for i in range(n, self.columns):
                path += "-" + str(self.A[m][i])
            print path
            return
        if n == self.columns -1:
            for i in range(m, self.rows):
                path += "-" + str(self.A[i][n])
            print path
            return
        path = path + "-" + str(self.A[m][n])
        self.print_paths(m+1, n , path, temp)
        self.print_paths(m, n+1, path, temp)
        pass



A = [[1,2,3], [4,5,6],[7,8,9]]

Solution(A).paths_finder()