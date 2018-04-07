__author__ = 'venkat'

def print_spiral(matrix):
    m = len(matrix)
    n= len(matrix[0])
    left = top = 0
    bottom = m-1
    right = n-1
    dir =0
    while left <= right and top <=bottom:
        if dir is 0:
            i = top
            while i<= right:
                print matrix[top][i]
                i += 1
            top +=1
            dir = 1
        elif dir is 1:
            i = top
            while i<= bottom:
                print matrix[i][right]
                i +=1
            right -= 1
            dir = 2
        elif dir is 2:
            i = right
            while i>=left:
                print matrix[bottom][i]
                i -= 1
            bottom -= 1
            dir = 3
        elif dir is 3:
            i = bottom
            while i>= top:
                print matrix[i][left]
                i -= 1
            left += 1
            dir = 0

matrix = [[1, 2, 3], [4,5,6], [7,8,9]]

# print_spiral(matrix)
class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        rows = len(A)
        if rows is 0:
            return result
        columns = len(A[0])
        left = top = 0
        right = columns - 1
        bottom = rows - 1
        direction =0
        while left <= right and top <= bottom:
            if direction ==0:
                index = left
                while index <= right:
                    result.append(A[top][index])
                    index +=1
                direction = 1
                top += 1
            if direction == 1:
                index = top
                while index <= bottom:
                    result.append(A[index][right])
                    index += 1
                direction = 2
                right -= 1
            if direction == 2:
                index = right
                while index >= left:
                    result.append(A[bottom][index])
                    index -=1
                direction = 3
                bottom -= 1
            if direction == 3:
                index = bottom
                while index >= top:
                    result.append(A[index][left])
                    index -= 1
                direction = 0
                left += 1
        ## Actual code to populate result
        return result

sl = Solution()
x = sl.spiralOrder([[1],[2],[3]])
print x

class SOlt:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        rows = len(A)
        if rows is 0:
            return result
        columns = len(A[0])
        left = top = 0
        right = columns - 1
        bottom = rows - 1
        direction =0
        while left <= right and top <= bottom:
            if direction ==0:
                index = left
                while index <= right:
                    result.append(A[top][index])
                    index +=1
                direction = 1
                top += 1
            elif direction == 1:
                index = top
                while index <= bottom:
                    result.append(A[index][right])
                    index += 1
                direction = 2
                right -= 1
            elif direction == 2:
                index = right
                while index >= left:
                    result.append(A[bottom][index])
                    index -=1
                direction = 3
                bottom -= 1
            elif direction == 3:
                index = bottom
                while index >= top:
                    result.append(A[index][left])
                    index -= 1
                direction = 0
                left += 1
        ## Actual code to populate result
        return result

x = SOlt()
res = x.spiralOrder([[1],[2],[3]])
print res