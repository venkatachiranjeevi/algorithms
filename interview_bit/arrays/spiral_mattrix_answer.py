__author__ = 'venkat'
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