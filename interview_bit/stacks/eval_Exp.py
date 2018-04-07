__author__ = 'venkat'

# ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        operators = ['+', '-', '*', '/']
        n = len(A)
        res = []
        for x in A:
            if x not in operators:
                res.append(x)
            elif x in operators:
                val1 = res.pop()
                val2 = res.pop()
                if x == '+':
                    res.append(int(val1) + int(val2))
                elif x == '-':
                    res.append(int(val2) - int(val1))
                elif x == '*':
                    res.append(int(val1) * int(val2))
                elif x == "/":
                    res.append(int(val2) / int(val1))

        return res.pop()
print Solution().evalRPN([ "5", "1", "2", "+", "4", "*", "+", "3", "-" ])