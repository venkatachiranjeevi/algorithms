# __author__ = 'venkat'
#
# class Solution(object):
#
#     def sp2(self, A):
#         result = []
#         for i in range(0,A):
#             li = []
#             for j in range(0,A):
#                 li.append(0)
#             result.append(li)
#         left =top = 0
#         bottom = right = A-1
#         dir =0
#         num = 1
#         while top<= bottom and left <= right:
#             if dir is 0:
#                 i = left
#                 while i <= right:
#                     result[top][i] = num
#                     i +=1
#                     num +=1
#                 dir = 1
#                 top += 1
#             elif dir is 1:
#                 i = top
#                 while i<= bottom:
#                     result[i][right] = num
#                     i += 1
#                     num += 1
#                 dir = 2
#                 right -= 1
#             elif dir is 2:
#                 i = right
#                 while i >= left:
#                     result[bottom][i] = num
#                     num += 1
#                     i -= 1
#                 bottom -= 1
#                 dir = 3
#             elif dir is 3:
#                 i = bottom
#                 while i>= top:
#                     result[i][left] = num
#                     num += 1
#                     i -= 1
#                 dir = 0
#                 left += 1
#         return result



class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        result = []
        for i in range(0,A):
            li = []
            for j in range(0,A):
                li.append(0)
            result.append(li)
        left =top = 0
        bottom = right = A-1
        dir =0
        num = 1
        while top<= bottom and left <= right:
            if dir is 0:
                i = left
                while i <= right:
                    result[top][i] = num
                    i +=1
                    num +=1
                dir = 1
                top += 1
            elif dir is 1:
                i = top
                while i<= bottom:
                    result[i][right] = num
                    i += 1
                    num += 1
                dir = 2
                right -= 1
            elif dir is 2:
                i = right
                while i >= left:
                    result[bottom][i] = num
                    num += 1
                    i -= 1
                bottom -= 1
                dir = 3
            elif dir is 3:
                i = bottom
                while i>= top:
                    result[i][left] = num
                    num += 1
                    i -= 1
                dir = 0
                left += 1
        return result

print Solution().generateMatrix(80)
